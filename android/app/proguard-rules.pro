# Proguard rules for DeutschMeister
-keepattributes *Annotation*
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}
-keep class com.deutschmeister.app.data.** { *; }
