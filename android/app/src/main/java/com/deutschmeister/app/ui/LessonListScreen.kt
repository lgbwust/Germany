package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.LessonModel
import com.deutschmeister.app.data.LevelModel
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LessonListScreen(
    level: LevelModel,
    onSelectLesson: (LessonModel) -> Unit,
    onBack: () -> Unit
) {
    val completedLessons = StorageManager.getCompletedLessons()

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(text = level.name, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                        Text(
                            text = level.goetheLevel,
                            fontSize = 12.sp,
                            color = AmberSecondary
                        )
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "返回")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = SurfaceDark)
            )
        },
        containerColor = BgDark
    ) { padding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(horizontal = 16.dp),
            contentPadding = PaddingValues(vertical = 16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item {
                // Level Goal Description Card
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(12.dp),
                    colors = CardDefaults.cardColors(containerColor = SurfaceDark),
                    border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(AmberPrimary.copy(alpha = 0.5f)))
                ) {
                    Column(modifier = Modifier.padding(14.dp)) {
                        Text(
                            text = "🎯 歌德考纲要求与学习目标",
                            fontWeight = FontWeight.Bold,
                            color = AmberSecondary,
                            fontSize = 14.sp
                        )
                        Text(
                            text = level.description,
                            color = TextPrimary,
                            fontSize = 13.sp,
                            lineHeight = 19.sp,
                            modifier = Modifier.padding(top = 4.dp)
                        )
                    }
                }
            }

            itemsIndexed(level.lessons) { index, lesson ->
                val isCompleted = completedLessons.contains(lesson.id)
                val score = StorageManager.getQuizScore(lesson.id)

                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(12.dp))
                        .clickable { onSelectLesson(lesson) },
                    shape = RoundedCornerShape(12.dp),
                    colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                    border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        // Lesson Number Badge
                        Box(
                            modifier = Modifier
                                .size(44.dp)
                                .clip(RoundedCornerShape(10.dp))
                                .background(if (isCompleted) DasGreen.copy(alpha = 0.2f) else AmberPrimary.copy(alpha = 0.2f))
                                .border(1.dp, if (isCompleted) DasGreen else AmberPrimary, RoundedCornerShape(10.dp)),
                            contentAlignment = Alignment.Center
                        ) {
                            if (isCompleted) {
                                Icon(
                                    imageVector = Icons.Default.CheckCircle,
                                    contentDescription = null,
                                    tint = DasGreen,
                                    modifier = Modifier.size(24.dp)
                                )
                            } else {
                                Text(
                                    text = "${index + 1}",
                                    fontWeight = FontWeight.Bold,
                                    color = AmberSecondary,
                                    fontSize = 16.sp
                                )
                            }
                        }

                        Spacer(modifier = Modifier.width(14.dp))

                        // Lesson Info
                        Column(modifier = Modifier.weight(1f)) {
                            Text(
                                text = lesson.title,
                                color = TextPrimary,
                                fontWeight = FontWeight.Bold,
                                fontSize = 16.sp
                            )
                            Text(
                                text = lesson.summary,
                                color = TextSecondary,
                                fontSize = 12.sp,
                                maxLines = 1,
                                modifier = Modifier.padding(top = 2.dp)
                            )
                            Row(
                                modifier = Modifier.padding(top = 6.dp),
                                horizontalArrangement = Arrangement.spacedBy(8.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    text = "${lesson.words.size} 词汇",
                                    fontSize = 11.sp,
                                    color = TextMuted
                                )
                                Text("•", fontSize = 11.sp, color = TextMuted)
                                if (score > 0) {
                                    Text(
                                        text = "测验 $score 分",
                                        fontSize = 11.sp,
                                        color = if (score >= 80) AmberSecondary else if (score >= 60) DasGreen else DieRed,
                                        fontWeight = FontWeight.Bold
                                    )
                                } else {
                                    Text(
                                        text = "未测验",
                                        fontSize = 11.sp,
                                        color = TextMuted
                                    )
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
