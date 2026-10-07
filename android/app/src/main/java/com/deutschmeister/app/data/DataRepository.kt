package com.deutschmeister.app.data

import android.content.Context
import com.google.gson.Gson
import java.io.InputStreamReader

object DataRepository {
    private var curriculum: CurriculumRoot? = null
    private val allWordsCache = mutableListOf<Pair<String, WordModel>>() // Level to Word

    fun init(context: Context) {
        if (curriculum != null) return
        try {
            context.assets.open("curriculum_data.json").use { inputStream ->
                InputStreamReader(inputStream, "UTF-8").use { reader ->
                    curriculum = Gson().fromJson(reader, CurriculumRoot::class.java)
                }
            }
            // Populate all words cache
            curriculum?.levels?.forEach { level ->
                level.lessons.forEach { lesson ->
                    lesson.words.forEach { word ->
                        allWordsCache.add(level.id to word)
                    }
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    fun getCurriculum(): CurriculumRoot? = curriculum

    fun getLevels(): List<LevelModel> = curriculum?.levels ?: emptyList()

    fun getLevel(levelId: String): LevelModel? =
        curriculum?.levels?.find { it.id == levelId }

    fun getLesson(lessonId: String): Pair<LevelModel, LessonModel>? {
        curriculum?.levels?.forEach { level ->
            val lesson = level.lessons.find { it.id == lessonId }
            if (lesson != null) return level to lesson
        }
        return null
    }

    fun search(query: String): List<SearchResult> {
        if (query.isBlank()) return emptyList()
        val q = query.trim().lowercase()
        val results = mutableListOf<SearchResult>()

        curriculum?.levels?.forEach { level ->
            level.lessons.forEach { lesson ->
                // Search in words
                lesson.words.forEach { w ->
                    if (w.word.lowercase().contains(q) ||
                        w.meaning.lowercase().contains(q) ||
                        w.example.lowercase().contains(q) ||
                        w.exampleCn.lowercase().contains(q)
                    ) {
                        results.add(SearchResult.WordResult(level.id, lesson.id, lesson.title, w))
                    }
                }
                // Search in grammar
                lesson.grammar?.sections?.forEach { sec ->
                    if (sec.heading.lowercase().contains(q) || sec.content.lowercase().contains(q)) {
                        results.add(SearchResult.GrammarResult(level.id, lesson.id, lesson.title, sec.heading, sec.content))
                    }
                }
            }
        }
        return results
    }

    fun getAllQuizQuestions(): List<Triple<String, String, QuizModel>> {
        // Returns (levelId, lessonTitle, quiz)
        val list = mutableListOf<Triple<String, String, QuizModel>>()
        curriculum?.levels?.forEach { lvl ->
            lvl.lessons.forEach { les ->
                les.quiz?.forEach { q ->
                    list.add(Triple(lvl.id, les.title, q))
                }
            }
        }
        return list
    }
}

sealed class SearchResult {
    data class WordResult(
        val levelId: String,
        val lessonId: String,
        val lessonTitle: String,
        val word: WordModel
    ) : SearchResult()

    data class GrammarResult(
        val levelId: String,
        val lessonId: String,
        val lessonTitle: String,
        val heading: String,
        val content: String
    ) : SearchResult()
}
