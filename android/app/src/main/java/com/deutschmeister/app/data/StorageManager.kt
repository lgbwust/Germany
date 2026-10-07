package com.deutschmeister.app.data

import android.content.Context
import android.content.SharedPreferences
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken

object StorageManager {
    private const val PREFS_NAME = "deutsch_meister_prefs"
    private const val KEY_BOOKMARKS = "key_bookmarks"
    private const val KEY_MISTAKES = "key_mistakes"
    private const val KEY_COMPLETED_LESSONS = "key_completed_lessons"
    private const val KEY_QUIZ_SCORES = "key_quiz_scores"
    private const val KEY_SPEECH_RATE = "key_speech_rate"

    private lateinit var prefs: SharedPreferences
    private val gson = Gson()

    fun init(context: Context) {
        prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }

    // Bookmarks (Saved Vocabulary)
    fun isBookmarked(word: String): Boolean {
        return getBookmarks().contains(word)
    }

    fun toggleBookmark(word: String): Boolean {
        val list = getBookmarks().toMutableSet()
        val newState = if (list.contains(word)) {
            list.remove(word)
            false
        } else {
            list.add(word)
            true
        }
        prefs.edit().putStringSet(KEY_BOOKMARKS, list).apply()
        return newState
    }

    fun getBookmarks(): Set<String> {
        return prefs.getStringSet(KEY_BOOKMARKS, emptySet()) ?: emptySet()
    }

    // Mistakes Book (错题本)
    fun addMistake(quizId: String) {
        val list = getMistakes().toMutableSet()
        list.add(quizId)
        prefs.edit().putStringSet(KEY_MISTAKES, list).apply()
    }

    fun removeMistake(quizId: String) {
        val list = getMistakes().toMutableSet()
        list.remove(quizId)
        prefs.edit().putStringSet(KEY_MISTAKES, list).apply()
    }

    fun getMistakes(): Set<String> {
        return prefs.getStringSet(KEY_MISTAKES, emptySet()) ?: emptySet()
    }

    // Completed Lessons
    fun markLessonCompleted(lessonId: String) {
        val set = getCompletedLessons().toMutableSet()
        set.add(lessonId)
        prefs.edit().putStringSet(KEY_COMPLETED_LESSONS, set).apply()
    }

    fun getCompletedLessons(): Set<String> {
        return prefs.getStringSet(KEY_COMPLETED_LESSONS, emptySet()) ?: emptySet()
    }

    // Quiz High Scores: LessonId -> Score (0-100)
    fun saveQuizScore(lessonId: String, score: Int) {
        val currentScores = getQuizScores().toMutableMap()
        val old = currentScores[lessonId] ?: 0
        if (score > old) {
            currentScores[lessonId] = score
            val json = gson.toJson(currentScores)
            prefs.edit().putString(KEY_QUIZ_SCORES, json).apply()
        }
    }

    fun getQuizScore(lessonId: String): Int {
        return getQuizScores()[lessonId] ?: 0
    }

    fun getQuizScores(): Map<String, Int> {
        val json = prefs.getString(KEY_QUIZ_SCORES, null) ?: return emptyMap()
        val type = object : TypeToken<Map<String, Int>>() {}.type
        return try {
            gson.fromJson(json, type) ?: emptyMap()
        } catch (e: Exception) {
            emptyMap()
        }
    }

    // Speech Rate Preference (0.7f - 1.2f)
    fun getSpeechRate(): Float {
        return prefs.getFloat(KEY_SPEECH_RATE, 0.9f)
    }

    fun setSpeechRate(rate: Float) {
        prefs.edit().putFloat(KEY_SPEECH_RATE, rate).apply()
    }
}
