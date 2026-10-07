package com.deutschmeister.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import com.deutschmeister.app.data.*
import com.deutschmeister.app.ui.*
import com.deutschmeister.app.util.DeutschMeisterTheme
import com.deutschmeister.app.util.SurfaceDark
import com.deutschmeister.app.util.TtsHelper

class MainActivity : ComponentActivity() {
    private lateinit var ttsHelper: TtsHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Initialize core data repositories and preferences
        DataRepository.init(this)
        StorageManager.init(this)
        ttsHelper = TtsHelper(this)

        setContent {
            DeutschMeisterTheme {
                MainAppContainer(
                    onSpeak = { text -> ttsHelper.speak(text) },
                    isLocalTtsAvailable = ttsHelper.isLocalGermanTtsAvailable(),
                    onOpenTtsSettings = { ttsHelper.openSystemTtsSettings() }
                )
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        ttsHelper.shutdown()
    }
}

sealed class BottomTab(val route: String, val title: String, val icon: ImageVector) {
    object Home : BottomTab("home", "学习大纲", Icons.Default.MenuBook)
    object Notebook : BottomTab("notebook", "生词错题", Icons.Default.Bookmark)
    object Search : BottomTab("search", "检索查询", Icons.Default.Search)
    object Settings : BottomTab("settings", "设置考纲", Icons.Default.Settings)
}

@Composable
fun MainAppContainer(
    onSpeak: (String) -> Unit,
    isLocalTtsAvailable: Boolean = false,
    onOpenTtsSettings: () -> Unit = {}
) {
    var currentTab by remember { mutableStateOf<BottomTab>(BottomTab.Home) }

    // Navigation sub-states for Home tab
    var selectedLevel by remember { mutableStateOf<LevelModel?>(null) }
    var selectedLesson by remember { mutableStateOf<LessonModel?>(null) }
    var isInQuiz by remember { mutableStateOf(false) }

    // Notebook initial tab state (0 = bookmarks, 1 = mistakes)
    var notebookInitialTab by remember { mutableStateOf(0) }

    // Back handling
    BackHandler(enabled = isInQuiz || selectedLesson != null || selectedLevel != null) {
        if (isInQuiz) {
            isInQuiz = false
        } else if (selectedLesson != null) {
            selectedLesson = null
        } else if (selectedLevel != null) {
            selectedLevel = null
        }
    }

    Scaffold(
        modifier = Modifier.fillMaxSize(),
        bottomBar = {
            // Only show bottom navigation when not inside a quiz or lesson detail
            if (!isInQuiz && selectedLesson == null) {
                NavigationBar(
                    containerColor = SurfaceDark
                ) {
                    val tabs = listOf(
                        BottomTab.Home,
                        BottomTab.Notebook,
                        BottomTab.Search,
                        BottomTab.Settings
                    )
                    tabs.forEach { tab ->
                        NavigationBarItem(
                            icon = { Icon(tab.icon, contentDescription = tab.title) },
                            label = { Text(tab.title) },
                            selected = currentTab == tab,
                            onClick = {
                                currentTab = tab
                                selectedLevel = null
                                selectedLesson = null
                                isInQuiz = false
                            },
                            colors = NavigationBarItemDefaults.colors(
                                indicatorColor = com.deutschmeister.app.util.AmberPrimary.copy(alpha = 0.3f),
                                selectedIconColor = com.deutschmeister.app.util.AmberSecondary,
                                selectedTextColor = com.deutschmeister.app.util.AmberSecondary,
                                unselectedIconColor = com.deutschmeister.app.util.TextSecondary,
                                unselectedTextColor = com.deutschmeister.app.util.TextSecondary
                            )
                        )
                    }
                }
            }
        }
    ) { padding ->
        Surface(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
        ) {
            when (currentTab) {
                BottomTab.Home -> {
                    when {
                        isInQuiz && selectedLesson != null -> {
                            QuizScreen(
                                lessonTitle = selectedLesson!!.title,
                                lessonId = selectedLesson!!.id,
                                quizList = selectedLesson!!.quiz ?: emptyList(),
                                onBack = { isInQuiz = false }
                            )
                        }
                        selectedLesson != null && selectedLevel != null -> {
                            LessonDetailScreen(
                                level = selectedLevel!!,
                                lesson = selectedLesson!!,
                                onSpeak = onSpeak,
                                onStartQuiz = { isInQuiz = true },
                                onBack = { selectedLesson = null }
                            )
                        }
                        selectedLevel != null -> {
                            LessonListScreen(
                                level = selectedLevel!!,
                                onSelectLesson = { les -> selectedLesson = les },
                                onBack = { selectedLevel = null }
                            )
                        }
                        else -> {
                            HomeScreen(
                                onSelectLevel = { lvl -> selectedLevel = lvl },
                                onOpenNotebook = { tabIdx ->
                                    notebookInitialTab = tabIdx
                                    currentTab = BottomTab.Notebook
                                }
                            )
                        }
                    }
                }
                BottomTab.Notebook -> {
                    NotebookScreen(
                        initialTab = notebookInitialTab,
                        onSpeak = onSpeak
                    )
                }
                BottomTab.Search -> {
                    SearchScreen(onSpeak = onSpeak)
                }
                BottomTab.Settings -> {
                    SettingsScreen(
                        onSpeak = onSpeak,
                        isLocalTtsAvailable = isLocalTtsAvailable,
                        onOpenTtsSettings = onOpenTtsSettings
                    )
                }
            }
        }
    }
}
