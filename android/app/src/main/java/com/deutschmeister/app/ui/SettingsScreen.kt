package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(
    onSpeak: (String) -> Unit,
    isLocalTtsAvailable: Boolean = false,
    onOpenTtsSettings: () -> Unit = {}
) {
    var speechRate by remember { mutableStateOf(StorageManager.getSpeechRate()) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("设置与歌德备考指南", fontWeight = FontWeight.Bold) },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = SurfaceDark)
            )
        },
        containerColor = BgDark
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // TTS Setting & Engine Diagnostic Card
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(12.dp),
                colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Icon(Icons.Default.VolumeUp, contentDescription = null, tint = AmberSecondary)
                        Spacer(modifier = Modifier.width(8.dp))
                        Text(
                            text = "德语语音合成与发音引擎",
                            fontWeight = FontWeight.Bold,
                            color = Color.White,
                            fontSize = 16.sp
                        )
                    }

                    Spacer(modifier = Modifier.height(12.dp))

                    // Engine Status Diagnostic Box
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(8.dp))
                            .background(BgDark)
                            .border(1.dp, if (isLocalTtsAvailable) DasGreen else AmberPrimary, RoundedCornerShape(8.dp))
                            .padding(12.dp)
                    ) {
                        Column {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = if (isLocalTtsAvailable) Icons.Default.CheckCircle else Icons.Default.Info,
                                    contentDescription = null,
                                    tint = if (isLocalTtsAvailable) DasGreen else AmberSecondary,
                                    modifier = Modifier.size(18.dp)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = if (isLocalTtsAvailable) "本地德语语音包：已就绪 (可离线发音)" else "本地德语语音包：手机未安装",
                                    color = if (isLocalTtsAvailable) DasGreen else AmberSecondary,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 13.sp
                                )
                            }
                            Text(
                                text = if (isLocalTtsAvailable) {
                                    "已连接手机系统原生德语 TTS 引擎，发音快速且无需消耗移动网络流量。"
                                } else {
                                    "系统已自动启用【在线母语高清发音】双重引擎保障（支持有道/谷歌德语母语发音），联网即可流畅发音；播放过的内容将自动缓存本地离线使用。"
                                },
                                color = TextSecondary,
                                fontSize = 12.sp,
                                lineHeight = 17.sp,
                                modifier = Modifier.padding(top = 4.dp)
                            )
                            if (!isLocalTtsAvailable) {
                                Spacer(modifier = Modifier.height(8.dp))
                                OutlinedButton(
                                    onClick = onOpenTtsSettings,
                                    modifier = Modifier.fillMaxWidth(),
                                    colors = ButtonDefaults.outlinedButtonColors(contentColor = AmberSecondary)
                                ) {
                                    Icon(Icons.Default.Settings, contentDescription = null, modifier = Modifier.size(16.dp))
                                    Spacer(modifier = Modifier.width(6.dp))
                                    Text("前往系统语音设置安装德语离线包", fontSize = 12.sp)
                                }
                            }
                        }
                    }

                    Spacer(modifier = Modifier.height(16.dp))
                    Text(
                        text = "发音语速微调: ${String.format("%.2f", speechRate)}x",
                        color = AmberSecondary,
                        fontSize = 14.sp
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        listOf(0.75f to "慢速 (0.75x)", 0.9f to "标准 (0.9x)", 1.1f to "常速 (1.1x)").forEach { (rate, label) ->
                            FilterChip(
                                selected = Math.abs(speechRate - rate) < 0.05f,
                                onClick = {
                                    speechRate = rate
                                    StorageManager.setSpeechRate(rate)
                                },
                                label = { Text(label) },
                                colors = FilterChipDefaults.filterChipColors(
                                    selectedContainerColor = AmberPrimary,
                                    selectedLabelColor = Color.White
                                )
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(14.dp))
                    Button(
                        onClick = { onSpeak("Guten Tag! Willkommen bei DeutschMeister. Übung macht den Meister.") },
                        modifier = Modifier.fillMaxWidth(),
                        colors = ButtonDefaults.buttonColors(containerColor = AmberPrimary)
                    ) {
                        Icon(Icons.Default.VolumeUp, contentDescription = null, tint = Color.White)
                        Spacer(modifier = Modifier.width(6.dp))
                        Text("🔊 立即试听德语发音效果", color = Color.White, fontWeight = FontWeight.Bold)
                    }
                }
            }

            // Goethe Exam Guide Card
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(12.dp),
                colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Icon(Icons.Default.Info, contentDescription = null, tint = AmberSecondary)
                        Spacer(modifier = Modifier.width(8.dp))
                        Text(
                            text = "歌德学院考试 (Goethe-Zertifikat) 指南",
                            fontWeight = FontWeight.Bold,
                            color = Color.White,
                            fontSize = 15.sp
                        )
                    }
                    Spacer(modifier = Modifier.height(12.dp))
                    val guideItems = listOf(
                        "• A1 (Start Deutsch 1)：60分及格。适合团聚签证、简单涉外生活起步，考察基础自我介绍、购物、问路与信件简写。",
                        "• A2：60分及格。适合简单日常会话、基础工作交流，要求掌握现在完成时、情态动词与静三动四介词。",
                        "• B1：四个独立模块（听、说、读、写各100分，各60分及格）。德国入籍、预科、双元制核心证书。重点考察从句语序、形容词词尾变化、被动语态及论证逻辑。",
                        "• B2：德国大学直接入学、医生/护士等专业执照硬性标准。全面掌握学术演讲、商务信函、双重连词及第二格名物化表达。"
                    )
                    guideItems.forEach { item ->
                        Text(
                            text = item,
                            color = TextSecondary,
                            fontSize = 12.5.sp,
                            lineHeight = 18.sp,
                            modifier = Modifier.padding(vertical = 4.dp)
                        )
                    }
                }
            }

            // About Card
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(12.dp),
                colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
            ) {
                Column(
                    modifier = Modifier.padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "DeutschMeister 德语大师 v1.1.0",
                        color = Color.White,
                        fontWeight = FontWeight.Bold,
                        fontSize = 14.sp
                    )
                    Text(
                        text = "海量词库 (A0-B2 4000+核心词汇) · 双引擎德语音频 · 歌德全真大纲",
                        color = TextMuted,
                        fontSize = 11.sp,
                        modifier = Modifier.padding(top = 4.dp)
                    )
                }
            }
        }
    }
}
