package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material3.*
import androidx.compose.material3.TabRowDefaults.tabIndicatorOffset
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.DataRepository
import com.deutschmeister.app.data.QuizModel
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.data.WordModel
import com.deutschmeister.app.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun NotebookScreen(
    initialTab: Int = 0,
    onSpeak: (String) -> Unit
) {
    var selectedTab by remember { mutableStateOf(initialTab) }
    var refreshTrigger by remember { mutableStateOf(0) }

    val bookmarks = remember(refreshTrigger) { StorageManager.getBookmarks() }
    val mistakeIds = remember(refreshTrigger) { StorageManager.getMistakes() }

    // Find all bookmarked word models
    val bookmarkedWordModels = remember(bookmarks) {
        val list = mutableListOf<WordModel>()
        DataRepository.getLevels().forEach { lvl ->
            lvl.lessons.forEach { les ->
                les.words.forEach { w ->
                    if (bookmarks.contains(w.word)) {
                        list.add(w)
                    }
                }
            }
        }
        list
    }

    // Find all mistake quiz models
    val allQuizzes = remember { DataRepository.getAllQuizQuestions() }
    val mistakeQuizzes = remember(mistakeIds) {
        allQuizzes.filter { mistakeIds.contains(it.third.id) }
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("学习本与薄弱项", fontWeight = FontWeight.Bold) },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = SurfaceDark)
            )
        },
        containerColor = BgDark
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
        ) {
            TabRow(
                selectedTabIndex = selectedTab,
                containerColor = SurfaceDark,
                contentColor = AmberPrimary,
                indicator = { tabPositions ->
                    TabRowDefaults.SecondaryIndicator(
                        modifier = Modifier.tabIndicatorOffset(tabPositions[selectedTab]),
                        color = AmberPrimary
                    )
                }
            ) {
                Tab(
                    selected = selectedTab == 0,
                    onClick = { selectedTab = 0 },
                    text = {
                        Text(
                            text = "生词本 (${bookmarkedWordModels.size})",
                            fontSize = 14.sp,
                            fontWeight = if (selectedTab == 0) FontWeight.Bold else FontWeight.Normal,
                            color = if (selectedTab == 0) AmberSecondary else TextSecondary
                        )
                    }
                )
                Tab(
                    selected = selectedTab == 1,
                    onClick = { selectedTab = 1 },
                    text = {
                        Text(
                            text = "错题本 (${mistakeQuizzes.size})",
                            fontSize = 14.sp,
                            fontWeight = if (selectedTab == 1) FontWeight.Bold else FontWeight.Normal,
                            color = if (selectedTab == 1) DieRed else TextSecondary
                        )
                    }
                )
            }

            if (selectedTab == 0) {
                // Bookmarked Words
                if (bookmarkedWordModels.isEmpty()) {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        Text(
                            text = "暂无收藏的生词，在学习单词时点击书签即可添加！",
                            color = TextSecondary,
                            fontSize = 14.sp
                        )
                    }
                } else {
                    LazyColumn(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(horizontal = 16.dp),
                        contentPadding = PaddingValues(vertical = 12.dp)
                    ) {
                        items(bookmarkedWordModels) { word ->
                            WordCard(word = word, onSpeak = onSpeak)
                        }
                    }
                }
            } else {
                // Mistakes Practice
                if (mistakeQuizzes.isEmpty()) {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        Text(
                            text = "太棒了！当前没有任何错题记录。",
                            color = DasGreen,
                            fontSize = 15.sp,
                            fontWeight = FontWeight.SemiBold
                        )
                    }
                } else {
                    LazyColumn(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(horizontal = 16.dp),
                        contentPadding = PaddingValues(vertical = 12.dp),
                        verticalArrangement = Arrangement.spacedBy(16.dp)
                    ) {
                        items(mistakeQuizzes) { (levelId, lessonTitle, quiz) ->
                            MistakeQuizCard(
                                levelId = levelId,
                                lessonTitle = lessonTitle,
                                quiz = quiz,
                                onResolved = {
                                    StorageManager.removeMistake(quiz.id)
                                    refreshTrigger++
                                }
                            )
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun MistakeQuizCard(
    levelId: String,
    lessonTitle: String,
    quiz: QuizModel,
    onResolved: () -> Unit
) {
    var selectedIdx by remember { mutableStateOf<Int?>(null) }
    var isSubmitted by remember { mutableStateOf(false) }

    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.cardColors(containerColor = SurfaceCard),
        border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "$levelId · $lessonTitle",
                    color = AmberSecondary,
                    fontSize = 12.sp,
                    fontWeight = FontWeight.Bold
                )
                IconButton(onClick = onResolved, modifier = Modifier.size(28.dp)) {
                    Icon(
                        imageVector = Icons.Default.Delete,
                        contentDescription = "移除错题",
                        tint = TextMuted,
                        modifier = Modifier.size(18.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(6.dp))
            Text(
                text = quiz.question,
                color = Color.White,
                fontWeight = FontWeight.SemiBold,
                fontSize = 15.sp,
                lineHeight = 22.sp
            )

            Spacer(modifier = Modifier.height(12.dp))

            quiz.options.forEachIndexed { oIdx, optText ->
                val isCorrect = oIdx == quiz.correctIndex
                val isChosen = selectedIdx == oIdx

                val btnBg = when {
                    !isSubmitted -> SurfaceDark
                    isCorrect -> DasGreen.copy(alpha = 0.2f)
                    isChosen -> DieRed.copy(alpha = 0.2f)
                    else -> SurfaceDark
                }
                val btnBorder = when {
                    !isSubmitted -> SurfaceCardBorder
                    isCorrect -> DasGreen
                    isChosen -> DieRed
                    else -> SurfaceCardBorder
                }

                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                        .clip(RoundedCornerShape(8.dp))
                        .background(btnBg)
                        .border(1.dp, btnBorder, RoundedCornerShape(8.dp))
                        .padding(10.dp)
                ) {
                    Text(
                        text = "${('A' + oIdx)}. $optText",
                        color = if (isSubmitted && isCorrect) DasGreen else TextPrimary,
                        fontSize = 14.sp
                    )
                }
            }

            if (!isSubmitted) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 10.dp),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    quiz.options.indices.forEach { idx ->
                        OutlinedButton(
                            onClick = {
                                selectedIdx = idx
                                isSubmitted = true
                            },
                            modifier = Modifier.weight(1f),
                            contentPadding = PaddingValues(vertical = 4.dp),
                            colors = ButtonDefaults.outlinedButtonColors(contentColor = AmberSecondary)
                        ) {
                            Text("${('A' + idx)}")
                        }
                    }
                }
            } else {
                Spacer(modifier = Modifier.height(10.dp))
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(8.dp))
                        .background(BgDark)
                        .padding(10.dp)
                ) {
                    Column {
                        Text(
                            text = if (selectedIdx == quiz.correctIndex) "✅ 回答正确！已攻克此题。" else "❌ 仍需巩固：",
                            color = if (selectedIdx == quiz.correctIndex) DasGreen else DieRed,
                            fontWeight = FontWeight.Bold,
                            fontSize = 13.sp
                        )
                        Text(
                            text = quiz.explanation,
                            color = TextSecondary,
                            fontSize = 12.sp,
                            modifier = Modifier.padding(top = 4.dp)
                        )
                    }
                }
                if (selectedIdx == quiz.correctIndex) {
                    Spacer(modifier = Modifier.height(10.dp))
                    Button(
                        onClick = onResolved,
                        modifier = Modifier.fillMaxWidth(),
                        colors = ButtonDefaults.buttonColors(containerColor = DasGreen)
                    ) {
                        Text("从错题本移出", color = Color.White)
                    }
                }
            }
        }
    }
}
