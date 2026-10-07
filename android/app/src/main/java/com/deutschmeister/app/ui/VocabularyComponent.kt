package com.deutschmeister.app.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Bookmark
import androidx.compose.material.icons.filled.BookmarkBorder
import androidx.compose.material.icons.filled.VolumeUp
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.deutschmeister.app.data.StorageManager
import com.deutschmeister.app.data.WordModel
import com.deutschmeister.app.util.*

@Composable
fun WordCard(
    word: WordModel,
    onSpeak: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    var isBookmarked by remember(word.word) {
        mutableStateOf(StorageManager.isBookmarked(word.word))
    }
    val articleColor = getArticleColor(word.article)

    Card(
        modifier = modifier
            .fillMaxWidth()
            .padding(vertical = 6.dp),
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.cardColors(containerColor = SurfaceCard),
        border = CardDefaults.outlinedCardBorder().copy(brush = androidx.compose.ui.graphics.SolidColor(SurfaceCardBorder))
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            // Header: Article Tag + Word + Actions (Speak, Bookmark)
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                    modifier = Modifier.weight(1f)
                ) {
                    if (word.article.isNotBlank()) {
                        Box(
                            modifier = Modifier
                                .clip(RoundedCornerShape(6.dp))
                                .background(articleColor.copy(alpha = 0.2f))
                                .border(1.dp, articleColor, RoundedCornerShape(6.dp))
                                .padding(horizontal = 8.dp, vertical = 2.dp)
                        ) {
                            Text(
                                text = word.article,
                                color = articleColor,
                                fontWeight = FontWeight.Bold,
                                fontSize = 13.sp
                            )
                        }
                    }
                    Text(
                        text = word.word,
                        color = TextPrimary,
                        fontWeight = FontWeight.Bold,
                        fontSize = 18.sp
                    )
                }

                Row(verticalAlignment = Alignment.CenterVertically) {
                    IconButton(onClick = { onSpeak(word.word) }) {
                        Icon(
                            imageVector = Icons.Default.VolumeUp,
                            contentDescription = "发音",
                            tint = AmberPrimary
                        )
                    }
                    IconButton(onClick = {
                        isBookmarked = StorageManager.toggleBookmark(word.word)
                    }) {
                        Icon(
                            imageVector = if (isBookmarked) Icons.Default.Bookmark else Icons.Default.BookmarkBorder,
                            contentDescription = "收藏生词",
                            tint = if (isBookmarked) AmberSecondary else TextSecondary
                        )
                    }
                }
            }

            // IPA & Word Type
            Row(
                modifier = Modifier.padding(top = 4.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                if (word.ipa.isNotBlank()) {
                    Text(
                        text = word.ipa,
                        color = DerBlue,
                        fontFamily = FontFamily.Monospace,
                        fontSize = 13.sp
                    )
                }
                Text(
                    text = word.type,
                    color = TextSecondary,
                    fontSize = 12.sp
                )
            }

            // Plural / Verb forms
            if (word.plural.isNotBlank()) {
                Text(
                    text = "复数/变位: ${word.plural}",
                    color = PluralGold,
                    fontSize = 12.sp,
                    modifier = Modifier.padding(top = 4.dp)
                )
            }

            // Meaning
            Text(
                text = word.meaning,
                color = Color.White,
                fontWeight = FontWeight.SemiBold,
                fontSize = 15.sp,
                modifier = Modifier.padding(vertical = 8.dp)
            )

            // Example Sentence Box
            if (word.example.isNotBlank()) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(8.dp))
                        .background(BgDark.copy(alpha = 0.6f))
                        .border(1.dp, SurfaceCardBorder, RoundedCornerShape(8.dp))
                        .padding(10.dp)
                ) {
                    Column {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Text(
                                text = word.example,
                                color = TextPrimary,
                                fontSize = 13.sp,
                                modifier = Modifier.weight(1f)
                            )
                            IconButton(
                                onClick = { onSpeak(word.example) },
                                modifier = Modifier.size(28.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.VolumeUp,
                                    contentDescription = "例句发音",
                                    tint = TextSecondary,
                                    modifier = Modifier.size(18.dp)
                                )
                            }
                        }
                        if (word.exampleCn.isNotBlank()) {
                            Text(
                                text = word.exampleCn,
                                color = TextMuted,
                                fontSize = 12.sp,
                                modifier = Modifier.padding(top = 4.dp)
                            )
                        }
                    }
                }
            }
        }
    }
}
