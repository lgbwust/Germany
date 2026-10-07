# 🇩🇪 DeutschMeister (德语大师 · 歌德 A1-B2 学习通)

[![Android](https://img.shields.io/badge/Platform-Android-3DDC84.svg?style=flat&logo=android)](file:///Users/pioneer/Desktop/AI/Germany/android)
[![Kotlin](https://img.shields.io/badge/Language-Kotlin-7F52FF.svg?style=flat&logo=kotlin)](file:///Users/pioneer/Desktop/AI/Germany/android/app/src/main/java)
[![Jetpack Compose](https://img.shields.io/badge/UI-Jetpack%20Compose%20%2F%20Material3-4285F4.svg?style=flat)](file:///Users/pioneer/Desktop/AI/Germany/android/app/build.gradle.kts)
[![Goethe Standard](https://img.shields.io/badge/CEFR-A0%20%7C%20A1%20%7C%20A2%20%7C%20B1%20%7C%20B2-D97706.svg)](file:///Users/pioneer/Desktop/AI/Germany/tools/curriculum.json)

基于欧洲语言共同参考标准（CEFR）与**歌德学院（Goethe-Institut）考试大纲**严格设计的全功能 Android 德语学习系统与配套开发工具集。

---

## 🎯 需求对照与功能落实

根据 [`app实现需求.txt`](file:///Users/pioneer/Desktop/AI/Germany/app%E5%AE%9E%E7%8E%B0%E9%9C%80%E6%B1%82.txt) 的 5 大核心要求，本项目实现了全方位的深度落地：

| 需求条目 | 需求要求 | 实现情况与功能亮点 |
| :--- | :--- | :--- |
| **需求 1** | 从 0 到 B2 的所有学习内容，包括单词、语法及课后测试 | 覆盖 **A0（字母与语音）、A1、A2、B1、B2** 全部 5 个层级，包含核心大纲词汇、详实语法讲义、全套互动题库。 |
| **需求 2** | 内容循序渐进，划分相应课时，合理学习及测验 | 严格划分为 **21 个模块化课时（Lektionen）**，每课包含“考纲词汇”、“语法精讲”、“课后实战测验”，环环相扣。 |
| **需求 3** | 提供例句及单词音标发音 | 1. 每个词条均配备**标准国际音标（IPA）**、词性与复数/变位。<br>2. 集成 Android 原生 `TextToSpeech` 引擎（`Locale.GERMANY`），支持**单词发音**与**例句整句发音**，支持 0.75x~1.1x 语速调节。<br>3. 提供地道实用的德汉双语例句。 |
| **需求 4** | 实用性强，安排合理 | 1. **独创冠词颜色视觉记忆法**：`der 阳性(天蓝)`、`die 阴性(玫红)`、`das 中性(草绿)`。<br>2. **智能学习闭环**：生词一键收藏（生词本），测验错题自动收录（错题本），支持错题专项重练与攻克。 |
| **需求 5** | 基于歌德考试（Goethe-Zertifikat）要求 | 考题深度还原歌德考试真题场景（读信、告示理解、语法填空、变格变位、冠词快判、第二虚拟式礼貌句型、B2双重连词等），并附带权威考纲指南。 |

---

## 🛠️ 德语学习 App 开发工具集 (DevTools Suite)

为方便课程教研、词汇扩充、语法维护以及跨平台实时预览，本项目专为开发者打造了一整套强大的命令行与可视化工具集：

### 1. 课程数据生成工具 (`tools/curriculum_generator.py`)
- **功能**：自动生成完整的 A0-B2 歌德大纲课程体系，包含 IPA 音标、德语冠词、复数规则、例句及歌德考题。
- **输出**：直接输出到开发端 [`tools/curriculum.json`](file:///Users/pioneer/Desktop/AI/Germany/tools/curriculum.json) 以及 Android App 的资源目录 [`android/app/src/main/assets/curriculum_data.json`](file:///Users/pioneer/Desktop/AI/Germany/android/app/src/main/assets/curriculum_data.json)。
- **运行命令**：
  ```bash
  python3 tools/curriculum_generator.py
  ```

### 2. 数据质量与考纲校验工具 (`tools/validate_data.py`)
- **功能**：自动化 Linter 校验工具，确保课程数据零错误：
  - 检查 JSON 语法及各级大纲 ID（A0-B2）
  - 检查每个单词是否具备合法冠词（`der`/`die`/`das`）、国际音标 IPA、中文释义和德汉对照例句
  - 检查测验题目选项完整度、答案索引有效性及解析说明
  - 生成词汇量、词性比例与题型分布统计报表
- **运行命令**：
  ```bash
  python3 tools/validate_data.py
  ```

### 3. 本地发音与 TTS 诊断工具 (`tools/tts_tool.py`)
- **功能**：探测系统内置德语发音音色（如 `Anna`, `Eddy`），支持命令行快速试听德语拼读与发音效果。
- **运行命令**：
  ```bash
  python3 tools/tts_tool.py --speak
  ```

### 4. 网页版交互式开发预览器 (`tools/web_preview/`)
- **功能**：无需启动 Android 模拟器，在 Mac 浏览器中即可即时预览与试用全部 A0-B2 课程：
  - 支持直接调用浏览器 Web Speech API 朗读德语单词与例句
  - 直观浏览所有语法表格与重点避坑规则
  - 互动体验 48 道课后测验题（即时显示正确/错误及答案解析）
- **启动命令**：
  ```bash
  python3 tools/web_preview/preview_server.py --open
  ```
  *(浏览器打开 `http://localhost:8080/web_preview/index.html`)*

### 5. 一键开发与构建脚本 (`build_app.sh`)
- **功能**：自动探测并配置 Android Studio 的 JBR (Java 21) 与 Android SDK 环境变量，支持一步完成数据生成、代码校验、Web预览或编译打包。
- **常用命令**：
  ```bash
  ./build_app.sh generate    # 重新生成课程数据并校验
  ./build_app.sh validate    # 校验数据完整度
  ./build_app.sh preview     # 启动网页预览器
  ./build_app.sh tts         # 测试发音
  ./build_app.sh build       # 一键编译生成 Android Debug APK
  ```

---

## 📱 Android App 架构与核心源码

App 采用 Google 官方推荐的**单 Activity + Jetpack Compose + Material 3 现代响应式架构**：

```
android/app/src/main/
├── AndroidManifest.xml                  # 清单文件，配置 TTS Service 与方向自适应
├── assets/
│   └── curriculum_data.json             # A0-B2 歌德大纲全套结构化课程数据
├── java/com/deutschmeister/app/
│   ├── MainActivity.kt                  # 主入口，处理底部导航、状态分发与生命周期
│   ├── data/
│   │   ├── Model.kt                     # 数据实体定义（Level, Lesson, Word, Quiz）
│   │   ├── DataRepository.kt            # 课程仓库，支持全局快速搜索
│   │   └── StorageManager.kt            # 进度持久化（生词本、错题本、测验高分榜）
│   ├── util/
│   │   ├── TtsHelper.kt                 # Android 原生 TextToSpeech 语音合成封装
│   │   └── Theme.kt                     # Material 3 深色学习主题与冠词色彩规范
│   └── ui/
│       ├── HomeScreen.kt                # 首页大纲：歌德进阶雷达、总进度、打卡统计
│       ├── LessonListScreen.kt          # 阶段课时列表与测验得分展示
│       ├── LessonDetailScreen.kt        # 课时详情：词汇、语法精讲、测验入口（3Tab联动）
│       ├── VocabularyComponent.kt       # 词汇卡片：IPA、冠词高亮、点击发音、例句朗读
│       ├── GrammarComponent.kt          # 语法讲义：结构树、变格变位表、避坑指南
│       ├── QuizScreen.kt                # 互动测验：即时判分、错题自动录入、解析弹窗
│       ├── NotebookScreen.kt            # 生词本与错题本：错题专项重练与攻克
│       ├── SearchScreen.kt              # 全局检索：德汉双向查词与语法知识点速查
│       └── SettingsScreen.kt            # 设置页：TTS 语速调节、歌德考试四模块备考指南
└── res/
    ├── values/strings.xml
    ├── values/colors.xml
    └── values/themes.xml
```

---

## 🚀 在 Android Studio 中运行与调试

1. 打开 **Android Studio**（路径：`/Users/pioneer/Applications/Android Studio.app`）。
2. 点击 **Open**，选择本项目中的 [`android/`](file:///Users/pioneer/Desktop/AI/Germany/android) 目录。
3. 等待 Gradle 自动完成项目同步（Sync）。
4. 连接 Android 手机或启动 Android 模拟器，点击顶部绿色的 **Run 'app'** 按钮即可运行。
