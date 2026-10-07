// DeutschMeister Web Preview App
let curriculumData = null;
let currentLevel = "A1";
let currentLessonId = null;

// Speech synthesis helper
function speakGerman(text) {
  if (!('speechSynthesis' in window)) {
    alert("您的浏览器不支持 Web Speech 语音合成 API");
    return;
  }
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'de-DE';
  utterance.rate = 0.9;
  window.speechSynthesis.speak(utterance);
}

// Fetch curriculum data
async function loadCurriculum() {
  try {
    const res = await fetch('../curriculum.json');
    if (!res.ok) throw new Error("无法加载 ../curriculum.json");
    curriculumData = await res.json();
    initApp();
  } catch (err) {
    console.error("加载数据失败:", err);
    document.getElementById('lesson-title').innerText = "加载课程数据失败，请确保本地服务器正在运行。";
  }
}

function initApp() {
  // Update stats
  let totalLessons = 0;
  let totalWords = 0;
  let totalQuizzes = 0;
  curriculumData.levels.forEach(lvl => {
    totalLessons += lvl.lessons.length;
    lvl.lessons.forEach(les => {
      totalWords += les.words.length;
      totalQuizzes += (les.quiz || []).length;
    });
  });

  document.getElementById('stats-badge').innerText = 
    `共 ${curriculumData.levels.length} 个级别 · ${totalLessons} 节核心课时 · ${totalWords} 核心词汇 · ${totalQuizzes} 练习题`;

  // Render level tabs
  const levelTabs = document.getElementById('level-tabs');
  levelTabs.innerHTML = '';
  curriculumData.levels.forEach(lvl => {
    const btn = document.createElement('button');
    btn.className = `level-btn ${lvl.id === currentLevel ? 'active' : ''}`;
    btn.innerText = lvl.id;
    btn.onclick = () => switchLevel(lvl.id);
    levelTabs.appendChild(btn);
  });

  // Switch to default level
  switchLevel("A1");

  // Mode tab switching
  document.querySelectorAll('.mode-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      tab.classList.add('active');
      const tabId = `tab-${tab.dataset.tab}`;
      document.getElementById(tabId).classList.add('active');
    });
  });

  // Test audio button
  document.getElementById('tts-toggle-btn').addEventListener('click', () => {
    speakGerman("Guten Tag! Willkommen bei DeutschMeister. Herzlichen Glückwunsch!");
  });
}

function switchLevel(levelId) {
  currentLevel = levelId;
  document.querySelectorAll('.level-btn').forEach(btn => {
    btn.classList.toggle('active', btn.innerText === levelId);
  });

  const levelObj = curriculumData.levels.find(l => l.id === levelId);
  if (!levelObj) return;

  const lessonList = document.getElementById('lesson-list');
  lessonList.innerHTML = '';

  levelObj.lessons.forEach((les, idx) => {
    const item = document.createElement('div');
    item.className = 'lesson-item';
    item.innerHTML = `
      <div class="l-title">${les.title}</div>
      <div class="l-desc">${les.summary}</div>
    `;
    item.onclick = () => selectLesson(les, item);
    lessonList.appendChild(item);

    if (idx === 0) {
      selectLesson(les, item);
    }
  });
}

function selectLesson(lesson, itemElem) {
  currentLessonId = lesson.id;
  document.querySelectorAll('.lesson-item').forEach(i => i.classList.remove('active'));
  if (itemElem) itemElem.classList.add('active');

  // Header info
  document.getElementById('lesson-level-tag').innerText = `LEVEL ${currentLevel} · ${lesson.id}`;
  document.getElementById('lesson-title').innerText = lesson.title;
  document.getElementById('lesson-summary').innerText = lesson.summary;

  document.getElementById('words-count').innerText = lesson.words.length;
  document.getElementById('quiz-count').innerText = (lesson.quiz || []).length;

  renderWords(lesson.words);
  renderGrammar(lesson.grammar);
  renderQuiz(lesson.quiz || []);
}

function renderWords(words) {
  const grid = document.getElementById('words-grid');
  grid.innerHTML = '';

  words.forEach(w => {
    const card = document.createElement('div');
    const artClass = w.article ? `card-${w.article}` : 'card-other';
    card.className = `word-card ${artClass}`;

    let articleBadge = '';
    if (w.article) {
      articleBadge = `<span class="chip chip-${w.article}">${w.article}</span>`;
    }

    card.innerHTML = `
      <div class="word-header">
        <div class="word-title">
          ${articleBadge}
          <span>${w.word}</span>
        </div>
        <span class="speak-icon" title="朗读德语单词">🔊</span>
      </div>
      <div class="ipa-text">${w.ipa || ''} <span style="color:#94a3b8; font-size:11px;">${w.type}</span></div>
      ${w.plural ? `<div class="plural-tag">复数/变位: ${w.plural}</div>` : ''}
      <div class="word-meaning">${w.meaning}</div>
      <div class="example-box">
        <div class="example-de">
          <span class="speak-icon-mini" title="朗读例句">🔊</span>
          <span>${w.example}</span>
        </div>
        <div class="example-cn">${w.exampleCn}</div>
      </div>
    `;

    // Audio click
    card.querySelector('.speak-icon').onclick = (e) => {
      e.stopPropagation();
      speakGerman(w.word);
    };
    card.querySelector('.speak-icon-mini').onclick = (e) => {
      e.stopPropagation();
      speakGerman(w.example);
    };

    grid.appendChild(card);
  });
}

function renderGrammar(grammar) {
  const container = document.getElementById('grammar-container');
  container.innerHTML = '';

  if (!grammar || !grammar.sections) {
    container.innerHTML = '<p style="color:#94a3b8;">本课暂无专门语法章节</p>';
    return;
  }

  grammar.sections.forEach(sec => {
    const card = document.createElement('div');
    card.className = 'grammar-card';
    card.innerHTML = `
      <h3>${sec.heading}</h3>
      <pre>${sec.content}</pre>
    `;
    container.appendChild(card);
  });
}

function renderQuiz(quizList) {
  const container = document.getElementById('quiz-container');
  container.innerHTML = '';

  if (!quizList || quizList.length === 0) {
    container.innerHTML = '<p style="color:#94a3b8;">本课暂无测验题目</p>';
    return;
  }

  quizList.forEach((q, qIdx) => {
    const card = document.createElement('div');
    card.className = 'quiz-card';

    const optsHtml = q.options.map((opt, oIdx) => `
      <button class="quiz-option" data-idx="${oIdx}">${String.fromCharCode(65 + oIdx)}. ${opt}</button>
    `).join('');

    card.innerHTML = `
      <div class="quiz-type-tag">题型: ${q.type}</div>
      <div class="quiz-question">${qIdx + 1}. ${q.question}</div>
      <div class="quiz-options">${optsHtml}</div>
      <div class="quiz-explanation" id="expl-${qIdx}">
        <strong>解析：</strong>${q.explanation}
      </div>
    `;

    // Interactive buttons
    const optButtons = card.querySelectorAll('.quiz-option');
    optButtons.forEach(btn => {
      btn.onclick = () => {
        const selectedIdx = parseInt(btn.dataset.idx);
        optButtons.forEach(b => b.disabled = true);
        if (selectedIdx === q.correctIndex) {
          btn.classList.add('correct');
        } else {
          btn.classList.add('wrong');
          optButtons[q.correctIndex].classList.add('correct');
        }
        card.querySelector('.quiz-explanation').classList.add('show');
      };
    });

    container.appendChild(card);
  });
}

window.addEventListener('DOMContentLoaded', loadCurriculum);
