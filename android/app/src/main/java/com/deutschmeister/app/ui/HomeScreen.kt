package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.DataRepository
import com.deutschmeister.app.data.LevelModel
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.util.*

@Composable
fun HomeScreen(
    onSelectLevel: (LevelModel) -> Unit,
    onOpenNotebook: (initialTab: Int) -> Unit
) {
    val levels = DataRepository.getLevels()
    val completedLessons = StorageManager.getCompletedLessons()
    val bookmarkedWords = StorageManager.getBookmarks()
    val mistakes = StorageManager.getMistakes()

    val totalLessons = levels.sumOf { it.lessons.size }
    val completedCount = completedLessons.size

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .background(BgDark)
            .padding(horizontal = 16.dp),
        contentPadding = PaddingValues(top = 20.dp, bottom = 24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // App Header & Greeting
        item {
            Column {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    Text(text = "🇩🇪", fontSize = 28.sp)
                    Column {
                        Text(
                            text = "DeutschMeister",
                            color = Color.White,
                            fontSize = 22.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Text(
                            text = "德语从零到B2全系统 · 歌德考试通",
                            color = AmberSecondary,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Medium
                        )
                    }
                }
            }
        }

        // Today's Progress & Quick Stats Card
        item {
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(16.dp),
                colors = CardDefaults.cardColors(containerColor = SurfaceDark),
                border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "全阶段学习进度",
                            color = TextPrimary,
                            fontWeight = FontWeight.Bold,
                            fontSize = 15.sp
                        )
                        Text(
                            text = "$completedCount / $totalLessons 课时",
                            color = AmberSecondary,
                            fontWeight = FontWeight.SemiBold,
                            fontSize = 13.sp
                        )
                    }

                    Spacer(modifier = Modifier.height(10.dp))
                    val progressRatio = if (totalLessons > 0) completedCount.toFloat() / totalLessons else 0f
                    LinearProgressIndicator(
                        progress = progressRatio,
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(8.dp)
                            .clip(RoundedCornerShape(4.dp)),
                        color = AmberPrimary,
                        trackColor = SurfaceCard
                    )

                    Spacer(modifier = Modifier.height(16.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceAround
                    ) {
                        StatItem(
                            count = "${bookmarkedWords.size}",
                            label = "生词本",
                            icon = Icons.Default.Bookmark,
                            tint = AmberSecondary,
                            onClick = { onOpenNotebook(0) }
                        )
                        StatItem(
                            count = "${mistakes.size}",
                            label = "错题本",
                            icon = Icons.Default.Warning,
                            tint = DieRed,
                            onClick = { onOpenNotebook(1) }
                        )
                        StatItem(
                            count = "${(progressRatio * 100).toInt()}%",
                            label = "总掌握率",
                            icon = Icons.Default.CheckCircle,
                            tint = DasGreen,
                            onClick = {}
                        )
                    }
                }
            }
        }

        // Section Title: Goethe CEFR Levels
        item {
            Text(
                text = "歌德考试等级进阶大纲",
                color = Color.White,
                fontWeight = FontWeight.Bold,
                fontSize = 18.sp,
                modifier = Modifier.padding(top = 4.dp)
            )
        }

        // Level Cards
        items(levels) { level ->
            val levelCompleted = level.lessons.count { completedLessons.contains(it.id) }
            val levelTotal = level.lessons.size
            val ratio = if (levelTotal > 0) levelCompleted.toFloat() / levelTotal else 0f

            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(14.dp))
                    .clickable { onSelectLevel(level) },
                shape = RoundedCornerShape(14.dp),
                colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(10.dp)
                        ) {
                            Box(
                                modifier = Modifier
                                    .size(38.dp)
                                    .clip(RoundedCornerShape(8.dp))
                                    .background(AmberPrimary.copy(alpha = 0.2f))
                                    .border(1.dp, AmberPrimary, RoundedCornerShape(8.dp)),
                                contentAlignment = Alignment.Center
                            ) {
                                Text(
                                    text = level.id,
                                    color = AmberSecondary,
                                    fontWeight = FontWeight.ExtraBold,
                                    fontSize = 16.sp
                                )
                            }
                            Column {
                                Text(
                                    text = level.name,
                                    color = TextPrimary,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 16.sp
                                )
                                Text(
                                    text = level.goetheLevel,
                                    color = AmberSecondary,
                                    fontSize = 12.sp
                                )
                            }
                        }

                        Text(
                            text = "$levelCompleted / $levelTotal",
                            color = TextSecondary,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Medium
                        )
                    }

                    Spacer(modifier = Modifier.height(10.dp))
                    Text(
                        text = level.description,
                        color = TextMuted,
                        fontSize = 12.sp,
                        lineHeight = 17.sp,
                        maxLines = 2
                    )

                    Spacer(modifier = Modifier.height(12.dp))
                    LinearProgressIndicator(
                        progress = ratio,
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(5.dp)
                            .clip(RoundedCornerShape(2.5.dp)),
                        color = if (ratio >= 1.0f) DasGreen else AmberPrimary,
                        trackColor = BgDark
                    )
                }
            }
        }
    }
}

@Composable
private fun StatItem(
    count: String,
    label: String,
    icon: ImageVector,
    tint: Color,
    onClick: () -> Unit
) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier
            .clip(RoundedCornerShape(8.dp))
            .clickable { onClick() }
            .padding(horizontal = 12.dp, vertical = 6.dp)
    ) {
        Icon(imageVector = icon, contentDescription = null, tint = tint, modifier = Modifier.size(22.dp))
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = count, color = Color.White, fontWeight = FontWeight.Bold, fontSize = 16.sp)
        Text(text = label, color = TextMuted, fontSize = 11.sp)
    }
}
