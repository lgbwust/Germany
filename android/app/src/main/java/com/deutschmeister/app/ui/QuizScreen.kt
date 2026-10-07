package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.QuizModel
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuizScreen(
    lessonTitle: String,
    lessonId: String,
    quizList: List<QuizModel>,
    onBack: () -> Unit
) {
    if (quizList.isEmpty()) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = { Text("课后测验") },
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
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding),
                contentAlignment = Alignment.Center
            ) {
                Text(text = "当前课时暂无测验题目", color = TextSecondary)
            }
        }
        return
    }

    var currentIndex by remember { mutableStateOf(0) }
    var selectedOptionIndex by remember { mutableStateOf<Int?>(null) }
    var isSubmitted by remember { mutableStateOf(false) }
    var correctCount by remember { mutableStateOf(0) }
    var isFinished by remember { mutableStateOf(false) }

    val currentQuiz = quizList[currentIndex]

    fun handleOptionSelect(index: Int) {
        if (isSubmitted) return
        selectedOptionIndex = index
        isSubmitted = true
        if (index == currentQuiz.correctIndex) {
            correctCount++
        } else {
            StorageManager.addMistake(currentQuiz.id)
        }
    }

    fun handleNext() {
        if (currentIndex < quizList.size - 1) {
            currentIndex++
            selectedOptionIndex = null
            isSubmitted = false
        } else {
            // Finished quiz
            val finalScore = (correctCount * 100) / quizList.size
            StorageManager.saveQuizScore(lessonId, finalScore)
            if (finalScore >= 60) {
                StorageManager.markLessonCompleted(lessonId)
            }
            isFinished = true
        }
    }

    fun restartQuiz() {
        currentIndex = 0
        selectedOptionIndex = null
        isSubmitted = false
        correctCount = 0
        isFinished = false
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(lessonTitle, maxLines = 1) },
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
        if (isFinished) {
            val score = (correctCount * 100) / quizList.size
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                Icon(
                    imageVector = Icons.Default.CheckCircle,
                    contentDescription = "完成",
                    tint = if (score >= 60) DasGreen else DieRed,
                    modifier = Modifier.size(72.dp)
                )
                Spacer(modifier = Modifier.height(16.dp))
                Text(
                    text = "测验完成！",
                    fontSize = 24.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = "得分：$score 分",
                    fontSize = 32.sp,
                    fontWeight = FontWeight.ExtraBold,
                    color = if (score >= 80) AmberSecondary else if (score >= 60) DasGreen else DieRed
                )
                Spacer(modifier = Modifier.height(12.dp))
                Text(
                    text = if (score >= 80) "太棒了！完全达到歌德考试优秀标准！"
                    else if (score >= 60) "恭喜及格！已达到歌德大纲基本要求。"
                    else "建议多加复习语法与词汇后重试！错题已记录在错题本中。",
                    color = TextSecondary,
                    textAlign = TextAlign.Center,
                    fontSize = 14.sp
                )
                Spacer(modifier = Modifier.height(32.dp))
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    OutlinedButton(
                        onClick = { restartQuiz() },
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.outlinedButtonColors(contentColor = TextPrimary)
                    ) {
                        Icon(Icons.Default.Refresh, contentDescription = null)
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("重新测验")
                    }
                    Button(
                        onClick = onBack,
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.buttonColors(containerColor = AmberPrimary)
                    ) {
                        Text("返回课程")
                    }
                }
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .verticalScroll(rememberScrollState())
                    .padding(16.dp)
            ) {
                // Progress
                LinearProgressIndicator(
                    progress = (currentIndex + 1).toFloat() / quizList.size,
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(6.dp)
                        .clip(RoundedCornerShape(3.dp)),
                    color = AmberPrimary,
                    trackColor = SurfaceCard
                )
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 8.dp, bottom = 16.dp),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text(
                        text = "题型: ${currentQuiz.type}",
                        color = AmberSecondary,
                        fontSize = 12.sp,
                        fontWeight = FontWeight.Bold
                    )
                    Text(
                        text = "第 ${currentIndex + 1} / ${quizList.size} 题",
                        color = TextSecondary,
                        fontSize = 12.sp
                    )
                }

                // Question Card
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(12.dp),
                    colors = CardDefaults.cardColors(containerColor = SurfaceCard),
                    border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
                ) {
                    Text(
                        text = currentQuiz.question,
                        color = Color.White,
                        fontWeight = FontWeight.Bold,
                        fontSize = 17.sp,
                        lineHeight = 24.sp,
                        modifier = Modifier.padding(16.dp)
                    )
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Options
                currentQuiz.options.forEachIndexed { optIndex, optText ->
                    val isSelected = selectedOptionIndex == optIndex
                    val isCorrect = optIndex == currentQuiz.correctIndex

                    val borderColor = when {
                        !isSubmitted -> SurfaceCardBorder
                        isCorrect -> DasGreen
                        isSelected -> DieRed
                        else -> SurfaceCardBorder
                    }

                    val bgColor = when {
                        !isSubmitted -> SurfaceCard
                        isCorrect -> DasGreen.copy(alpha = 0.2f)
                        isSelected -> DieRed.copy(alpha = 0.2f)
                        else -> SurfaceCard
                    }

                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 6.dp)
                            .clip(RoundedCornerShape(10.dp))
                            .background(bgColor)
                            .border(1.5.dp, borderColor, RoundedCornerShape(10.dp))
                            .clickable(enabled = !isSubmitted) { handleOptionSelect(optIndex) }
                            .padding(16.dp)
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(
                                text = "${('A' + optIndex)}. ",
                                fontWeight = FontWeight.Bold,
                                color = if (isSubmitted && isCorrect) DasGreen else AmberSecondary,
                                fontSize = 15.sp
                            )
                            Text(
                                text = optText,
                                color = TextPrimary,
                                fontSize = 15.sp
                            )
                        }
                    }
                }

                // Explanation & Next Button
                if (isSubmitted) {
                    Spacer(modifier = Modifier.height(16.dp))
                    Card(
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(10.dp),
                        colors = CardDefaults.cardColors(containerColor = BgDark),
                        border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(AmberSecondary))
                    ) {
                        Column(modifier = Modifier.padding(14.dp)) {
                            Text(
                                text = "💡 试题解析：",
                                fontWeight = FontWeight.Bold,
                                color = AmberSecondary,
                                fontSize = 14.sp
                            )
                            Text(
                                text = currentQuiz.explanation,
                                color = TextSecondary,
                                fontSize = 13.sp,
                                lineHeight = 20.sp,
                                modifier = Modifier.padding(top = 4.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(20.dp))
                    Button(
                        onClick = { handleNext() },
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(48.dp),
                        colors = ButtonDefaults.buttonColors(containerColor = AmberPrimary)
                    ) {
                        Text(
                            text = if (currentIndex < quizList.size - 1) "下一题" else "查看测验成绩",
                            fontSize = 16.sp,
                            fontWeight = FontWeight.Bold
                        )
                    }
                }
            }
        }
    }
}
