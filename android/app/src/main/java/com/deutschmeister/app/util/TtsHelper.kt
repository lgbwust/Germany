package com.deutschmeister.app.util

import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.MediaPlayer
import android.net.ConnectivityManager
import android.net.NetworkCapabilities
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.util.Log
import android.widget.Toast
import com.deutschmeister.app.data.StorageManager
import java.io.File
import java.io.FileOutputStream
import java.net.HttpURLConnection
import java.net.URL
import java.net.URLEncoder
import java.security.MessageDigest
import java.util.Locale
import java.util.concurrent.Executors

class TtsHelper(private val context: Context) : TextToSpeech.OnInitListener {
    companion object {
        private const val TAG = "TtsHelper"
    }

    private var tts: TextToSpeech? = null
    private var isTtsInitialized = false
    private var isLocalGermanAvailable = false
    private var mediaPlayer: MediaPlayer? = null
    private val mainHandler = Handler(Looper.getMainLooper())
    private val executor = Executors.newSingleThreadExecutor()

    private val cacheDir: File = File(context.cacheDir, "german_audio_cache").apply {
        if (!exists()) mkdirs()
    }

    private var hasShownFallbackToast = false

    init {
        try {
            tts = TextToSpeech(context.applicationContext, this)
        } catch (e: Exception) {
            Log.e(TAG, "Error initializing TextToSpeech", e)
        }
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            val result = tts?.setLanguage(Locale.GERMANY)
            if (result == TextToSpeech.LANG_AVAILABLE ||
                result == TextToSpeech.LANG_COUNTRY_AVAILABLE ||
                result == TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE
            ) {
                isLocalGermanAvailable = true
                isTtsInitialized = true
                tts?.setSpeechRate(StorageManager.getSpeechRate())
                Log.d(TAG, "Native German TTS initialized successfully!")
            } else {
                Log.w(TAG, "Native German TTS language not supported/missing on this device (status: $result). Online German speech fallback will be used.")
                isLocalGermanAvailable = false
                isTtsInitialized = true
            }
        } else {
            Log.e(TAG, "TextToSpeech init failed with status: $status")
            isLocalGermanAvailable = false
            isTtsInitialized = false
        }
    }

    fun isLocalGermanTtsAvailable(): Boolean = isLocalGermanAvailable

    fun openSystemTtsSettings() {
        try {
            val intent = Intent("com.android.settings.TTS_SETTINGS").apply {
                flags = Intent.FLAG_ACTIVITY_NEW_TASK
            }
            context.startActivity(intent)
        } catch (e: Exception) {
            try {
                val intent = Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA).apply {
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK
                }
                context.startActivity(intent)
            } catch (e2: Exception) {
                Toast.makeText(context, "无法打开系统TTS设置，请在手机系统设置中搜索'文字转语音'安装德语包", Toast.LENGTH_LONG).show()
            }
        }
    }

    fun speak(text: String, rateMultiplier: Float = 1.0f) {
        val trimmed = text.trim()
        if (trimmed.isEmpty()) return

        stop()

        // 1. If local German TTS engine is available and ready, use it first
        if (isTtsInitialized && isLocalGermanAvailable && tts != null) {
            val currentRate = StorageManager.getSpeechRate() * rateMultiplier
            tts?.setSpeechRate(currentRate)
            val result = tts?.speak(trimmed, TextToSpeech.QUEUE_FLUSH, null, "utt_${System.currentTimeMillis()}")
            if (result == TextToSpeech.SUCCESS) {
                return
            }
            Log.w(TAG, "Local TTS speak returned $result, attempting online audio fallback...")
        }

        // 2. Fallback to online German audio stream with disk cache
        playOnlineGermanAudio(trimmed)
    }

    private fun playOnlineGermanAudio(text: String) {
        if (!hasShownFallbackToast) {
            hasShownFallbackToast = true
            mainHandler.post {
                Toast.makeText(context, "手机未装离线德语语音包，正在使用在线母语高清发音", Toast.LENGTH_SHORT).show()
            }
        }

        executor.execute {
            try {
                val cacheFile = getCacheFileFor(text)
                if (cacheFile.exists() && cacheFile.length() > 500) {
                    playFile(cacheFile)
                    return@execute
                }

                // Download from high-availability German audio APIs
                val downloaded = downloadAudio(text, cacheFile)
                if (downloaded && cacheFile.exists() && cacheFile.length() > 500) {
                    playFile(cacheFile)
                } else {
                    mainHandler.post {
                        Toast.makeText(context, "请检查网络连接以获取在线德语发音", Toast.LENGTH_SHORT).show()
                    }
                }
            } catch (e: Exception) {
                Log.e(TAG, "Failed playing online audio for: $text", e)
                mainHandler.post {
                    Toast.makeText(context, "发音失败，可在设置中安装系统德语语音包", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }

    private fun downloadAudio(text: String, destFile: File): Boolean {
        val encoded = URLEncoder.encode(text, "UTF-8")
        val urls = listOf(
            // Source 1: Youdao German pronunciation engine (extremely fast and reliable in Asia & globally)
            "https://dict.youdao.com/dictvoice?audio=$encoded&le=de",
            // Source 2: Google TTS endpoint
            "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=de&q=$encoded"
        )

        for (urlStr in urls) {
            try {
                val url = URL(urlStr)
                val conn = url.openConnection() as HttpURLConnection
                conn.connectTimeout = 5000
                conn.readTimeout = 8000
                conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36")
                conn.connect()

                if (conn.responseCode == HttpURLConnection.HTTP_OK) {
                    conn.inputStream.use { input ->
                        FileOutputStream(destFile).use { output ->
                            input.copyTo(output)
                        }
                    }
                    if (destFile.length() > 500) {
                        return true
                    }
                }
            } catch (e: Exception) {
                Log.w(TAG, "Audio download failed from $urlStr: ${e.message}")
            }
        }
        return false
    }

    private fun playFile(file: File) {
        mainHandler.post {
            try {
                stop()
                mediaPlayer = MediaPlayer().apply {
                    setAudioAttributes(
                        AudioAttributes.Builder()
                            .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                            .setUsage(AudioAttributes.USAGE_MEDIA)
                            .build()
                    )
                    setDataSource(file.absolutePath)
                    prepare()
                    start()
                    setOnCompletionListener {
                        it.release()
                        mediaPlayer = null
                    }
                    setOnErrorListener { mp, _, _ ->
                        mp.release()
                        mediaPlayer = null
                        true
                    }
                }
            } catch (e: Exception) {
                Log.e(TAG, "MediaPlayer error playing file: ${file.name}", e)
            }
        }
    }

    private fun getCacheFileFor(text: String): File {
        val md = MessageDigest.getInstance("MD5")
        val digest = md.digest(text.toByteArray(Charsets.UTF_8))
        val hex = digest.joinToString("") { "%02x".format(it) }
        return File(cacheDir, "$hex.mp3")
    }

    fun stop() {
        try {
            tts?.stop()
        } catch (e: Exception) {}
        try {
            if (mediaPlayer?.isPlaying == true) {
                mediaPlayer?.stop()
            }
            mediaPlayer?.release()
            mediaPlayer = null
        } catch (e: Exception) {}
    }

    fun shutdown() {
        stop()
        try {
            tts?.shutdown()
            tts = null
        } catch (e: Exception) {}
        executor.shutdown()
    }
}
