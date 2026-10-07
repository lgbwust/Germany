package com.deutschmeister.app.data

import com.google.gson.annotations.SerializedName

data class CurriculumRoot(
    @SerializedName("appName") val appName: String,
    @SerializedName("version") val version: String,
    @SerializedName("description") val description: String,
    @SerializedName("levels") val levels: List<LevelModel>
)

data class LevelModel(
    @SerializedName("id") val id: String, // "A0", "A1", "A2", "B1", "B2"
    @SerializedName("name") val name: String,
    @SerializedName("goetheLevel") val goetheLevel: String,
    @SerializedName("description") val description: String,
    @SerializedName("lessons") val lessons: List<LessonModel>
)

data class LessonModel(
    @SerializedName("id") val id: String,
    @SerializedName("title") val title: String,
    @SerializedName("summary") val summary: String,
    @SerializedName("grammar") val grammar: GrammarModel?,
    @SerializedName("words") val words: List<WordModel>,
    @SerializedName("quiz") val quiz: List<QuizModel>?
)

data class GrammarModel(
    @SerializedName("title") val title: String,
    @SerializedName("sections") val sections: List<GrammarSectionModel>
)

data class GrammarSectionModel(
    @SerializedName("heading") val heading: String,
    @SerializedName("content") val content: String
)

data class WordModel(
    @SerializedName("word") val word: String,
    @SerializedName("article") val article: String, // "der", "die", "das" or ""
    @SerializedName("type") val type: String, // "n.", "v.", "adj.", etc.
    @SerializedName("ipa") val ipa: String,
    @SerializedName("plural") val plural: String,
    @SerializedName("meaning") val meaning: String,
    @SerializedName("example") val example: String,
    @SerializedName("exampleCn") val exampleCn: String
)

data class QuizModel(
    @SerializedName("id") val id: String,
    @SerializedName("type") val type: String,
    @SerializedName("question") val question: String,
    @SerializedName("options") val options: List<String>,
    @SerializedName("correctIndex") val correctIndex: Int,
    @SerializedName("explanation") val explanation: String
)

enum class ScreenState {
    HOME,
    LESSON_LIST,
    LESSON_DETAIL,
    QUIZ,
    NOTEBOOK,
    SEARCH,
    SETTINGS
}
