package com.deutschmeister.app.util

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

val AmberPrimary = Color(0xFFD97706)
val AmberSecondary = Color(0xFFF59E0B)
val BgDark = Color(0xFF0F172A)
val SurfaceDark = Color(0xFF1E293B)
val SurfaceCard = Color(0xFF243048)
val SurfaceCardBorder = Color(0xFF334155)

val DerBlue = Color(0xFF38BDF8)
val DieRed = Color(0xFFF43F5E)
val DasGreen = Color(0xFF10B981)
val PluralGold = Color(0xFFF59E0B)

val TextPrimary = Color(0xFFF8FAFC)
val TextSecondary = Color(0xFF94A3B8)
val TextMuted = Color(0xFF64748B)

private val DarkColorScheme = darkColorScheme(
    primary = AmberPrimary,
    secondary = DerBlue,
    tertiary = DasGreen,
    background = BgDark,
    surface = SurfaceDark,
    surfaceVariant = SurfaceCard,
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onTertiary = Color.White,
    onBackground = TextPrimary,
    onSurface = TextPrimary
)

fun getArticleColor(article: String): Color {
    return when (article.trim().lowercase()) {
        "der" -> DerBlue
        "die" -> DieRed
        "das" -> DasGreen
        else -> TextSecondary
    }
}

@Composable
fun DeutschMeisterTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColorScheme,
        content = content
    )
}
