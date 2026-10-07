#!/usr/bin/env bash
# DeutschMeister Build & Development Tool Script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================================="
echo "🇩🇪 DeutschMeister (德语大师 · 歌德 A1-B2) 开发与构建工具"
echo "=========================================================="

# 1. Detect Java JDK
if [ -d "/Users/pioneer/Applications/Android Studio.app/Contents/jbr/Contents/Home" ]; then
    export JAVA_HOME="/Users/pioneer/Applications/Android Studio.app/Contents/jbr/Contents/Home"
    echo "[*] Using Android Studio JDK: $JAVA_HOME"
elif [ -n "$JAVA_HOME" ]; then
    echo "[*] Using environment JAVA_HOME: $JAVA_HOME"
fi

# 2. Detect Android SDK
if [ -d "$HOME/Library/Android/sdk" ]; then
    export ANDROID_HOME="$HOME/Library/Android/sdk"
    export ANDROID_SDK_ROOT="$HOME/Library/Android/sdk"
    echo "[*] Using Android SDK: $ANDROID_HOME"
fi

COMMAND="${1:-build}"

case "$COMMAND" in
    validate)
        echo "[*] Validating curriculum and Goethe exam data..."
        python3 tools/validate_data.py
        ;;
    generate)
        echo "[*] Regenerating curriculum dataset..."
        python3 tools/curriculum_generator.py
        python3 tools/validate_data.py
        ;;
    preview)
        echo "[*] Launching local Web Preview Server at http://localhost:8080/web_preview/index.html..."
        python3 tools/web_preview/preview_server.py --open
        ;;
    tts)
        echo "[*] Testing German TTS Audio..."
        python3 tools/tts_tool.py --speak
        ;;
    build)
        echo "[*] Step 1: Validating curriculum assets..."
        python3 tools/curriculum_generator.py
        python3 tools/validate_data.py
        
        echo "[*] Step 2: Compiling Android App (assembleDebug)..."
        cd android
        chmod +x gradlew
        ./gradlew assembleDebug --stacktrace
        echo ""
        echo "=========================================================="
        echo "🎉 Android APK 编译成功！"
        echo "APK 输出路径: android/app/build/outputs/apk/debug/app-debug.apk"
        echo "=========================================================="
        ;;
    clean)
        echo "[*] Cleaning build cache..."
        cd android
        ./gradlew clean
        ;;
    *)
        echo "Usage: ./build_app.sh [build|generate|validate|preview|tts|clean]"
        exit 1
        ;;
esac
