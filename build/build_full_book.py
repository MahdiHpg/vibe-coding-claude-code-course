# -*- coding: utf-8 -*-
import json
import base64
import os
import html
import subprocess
from persian_course_content import MODULES_TRANSLATION, LESSONS_TRANSLATION

# 1. Base64 Fonts
font_dir = "fonts"
b64_reg = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Regular.woff2"), "rb").read()).decode("utf-8")
b64_med = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Medium.woff2"), "rb").read()).decode("utf-8")
b64_semi = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-SemiBold.woff2"), "rb").read()).decode("utf-8")
b64_bold = base64.b64encode(open(os.path.join(font_dir, "Vazirmatn-Bold.woff2"), "rb").read()).decode("utf-8")

# 2. Datasets
course_data = json.load(open("complete_course_raw.json", encoding="utf-8"))
quizzes_map = json.load(open("quizzes_persian_ready.json", encoding="utf-8"))
cheatsheet_fa = json.load(open("cheatsheet_persian_ready.json", encoding="utf-8"))
glossary_fa = json.load(open("glossary_persian_ready.json", encoding="utf-8"))
lessons_structured = {l["slug"]: l for l in json.load(open("all_lessons_structured.json", encoding="utf-8"))}

print("Loaded all inputs. Generating HTML...")

css = f"""
@font-face {{
  font-family: 'Vazirmatn';
  src: url('data:font/woff2;base64,{b64_reg}') format('woff2');
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: 'Vazirmatn';
  src: url('data:font/woff2;base64,{b64_med}') format('woff2');
  font-weight: 500;
  font-style: normal;
}}
@font-face {{
  font-family: 'Vazirmatn';
  src: url('data:font/woff2;base64,{b64_semi}') format('woff2');
  font-weight: 600;
  font-style: normal;
}}
@font-face {{
  font-family: 'Vazirmatn';
  src: url('data:font/woff2;base64,{b64_bold}') format('woff2');
  font-weight: 700;
  font-style: normal;
}}

@page {{
  size: A4;
  margin: 20mm 15mm 20mm 15mm;
  @bottom-center {{
    content: counter(page);
    font-family: 'Vazirmatn', sans-serif;
    font-size: 9pt;
    color: #64748b;
  }}
  @bottom-right {{
    content: "کتابچه جامع وایب کدینگ با کلود کد (Claude Code)";
    font-family: 'Vazirmatn', sans-serif;
    font-size: 8pt;
    color: #94a3b8;
    direction: rtl;
  }}
  @top-left {{
    content: "Vibe Code School · راهنمای جامع فارسی";
    font-family: 'Vazirmatn', sans-serif;
    font-size: 8pt;
    color: #94a3b8;
    direction: rtl;
  }}
}}

* {{
  box-sizing: border-box;
}}

body {{
  font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  direction: rtl;
  text-align: justify;
  color: #0f172a;
  background: #ffffff;
  font-size: 10pt;
  line-height: 1.8;
  margin: 0;
  padding: 0;
}}

/* Typography */
h1, h2, h3, h4 {{
  font-family: 'Vazirmatn', sans-serif;
  color: #0f172a;
  margin-top: 0;
  font-weight: 700;
}}

h1 {{ font-size: 22pt; line-height: 1.3; color: #1e1b4b; }}
h2 {{ font-size: 15pt; line-height: 1.4; color: #312e81; border-bottom: 2px solid #e0e7ff; padding-bottom: 6px; margin-top: 24px; margin-bottom: 14px; }}
h3 {{ font-size: 12pt; line-height: 1.4; color: #4338ca; margin-top: 18px; margin-bottom: 10px; }}
h4 {{ font-size: 10.5pt; color: #475569; margin-top: 14px; margin-bottom: 8px; }}

p {{
  margin: 0 0 10px 0;
  color: #334155;
}}

code, pre {{
  font-family: Consolas, "Courier New", monospace;
  direction: ltr;
  unicode-bidi: isolate;
  text-align: left;
}}

code {{
  background: #f1f5f9;
  color: #db2777;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 9pt;
  border: 1px solid #e2e8f0;
}}

pre {{
  background: #0f172a;
  color: #f8fafc;
  padding: 12px 14px;
  border-radius: 8px;
  font-size: 8.5pt;
  line-height: 1.5;
  overflow-x: auto;
  margin: 10px 0;
  border: 1px solid #1e293b;
}}

/* Break helpers */
.page-break {{
  page-break-before: always;
}}

.avoid-break {{
  break-inside: avoid;
  page-break-inside: avoid;
}}

/* Cover Page */
.cover-page {{
  page-break-before: always;
  height: 250mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 30px 20px;
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%);
  color: #ffffff;
  border-radius: 12px;
}}

.cover-badge {{
  display: inline-block;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 9.5pt;
  color: #e0e7ff;
  letter-spacing: 0.5px;
}}

.cover-title-group h1 {{
  color: #ffffff;
  font-size: 28pt;
  margin: 18px 0 10px 0;
  line-height: 1.25;
  text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}}

.cover-subtitle {{
  font-size: 13pt;
  color: #c7d2fe;
  line-height: 1.6;
  margin-bottom: 25px;
}}

.cover-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 15px;
}}

.cover-tag {{
  background: rgba(255,255,255,0.12);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 8.5pt;
  color: #f1f5f9;
}}

.cover-meta-table {{
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  padding: 16px 20px;
  margin-top: auto;
}}

.cover-meta-row {{
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 9.5pt;
}}

.cover-meta-row:last-child {{
  border-bottom: none;
}}

.cover-meta-label {{
  color: #94a3b8;
}}

.cover-meta-val {{
  color: #ffffff;
  font-weight: 600;
}}

/* Table of Contents */
.toc-box {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 16px 20px;
  margin: 20px 0;
}}

.toc-module-title {{
  font-size: 11pt;
  font-weight: 700;
  color: #312e81;
  margin: 14px 0 6px 0;
  padding-bottom: 4px;
  border-bottom: 1px solid #cbd5e1;
}}

.toc-list {{
  list-style: none;
  padding: 0;
  margin: 0;
}}

.toc-item {{
  display: flex;
  justify-content: space-between;
  padding: 4px 8px;
  font-size: 9pt;
  border-radius: 4px;
}}

.toc-item:nth-child(even) {{
  background: #f1f5f9;
}}

/* Module Splash Banner */
.module-banner {{
  page-break-before: always;
  background: linear-gradient(135deg, #312e81 0%, #4338ca 100%);
  color: #ffffff;
  border-radius: 10px;
  padding: 30px;
  margin-bottom: 24px;
}}

.module-banner-num {{
  font-size: 12pt;
  color: #a5b4fc;
  font-weight: 700;
  letter-spacing: 1px;
}}

.module-banner-title {{
  color: #ffffff;
  font-size: 22pt;
  margin: 8px 0 12px 0;
}}

.module-banner-summary {{
  font-size: 11pt;
  line-height: 1.7;
  color: #e0e7ff;
}}

/* Lesson Container */
.lesson-card {{
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px dashed #cbd5e1;
}}

.lesson-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f1f5f9;
  padding: 8px 14px;
  border-radius: 6px;
  margin-bottom: 12px;
}}

.lesson-badge {{
  background: #4338ca;
  color: #ffffff;
  font-size: 8.5pt;
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: 600;
}}

.lesson-kind {{
  font-size: 8.5pt;
  color: #475569;
  font-weight: 500;
}}

.lesson-duration {{
  font-size: 8pt;
  color: #64748b;
}}

.lesson-title {{
  font-size: 14pt;
  color: #1e1b4b;
  margin: 6px 0 8px 0;
}}

.lesson-summary-box {{
  background: #f8fafc;
  border-right: 4px solid #4338ca;
  padding: 10px 14px;
  border-radius: 4px;
  font-size: 9.5pt;
  color: #334155;
  margin-bottom: 14px;
  line-height: 1.65;
}}

.concept-body {{
  margin-bottom: 14px;
  font-size: 9.5pt;
  line-height: 1.8;
}}

/* Callouts */
.callout {{
  border-radius: 8px;
  padding: 12px 14px;
  margin: 12px 0;
  font-size: 9.5pt;
  line-height: 1.7;
}}

.callout-info {{
  background: #eff6ff;
  border-right: 4px solid #3b82f6;
  color: #1e40af;
}}

.callout-success {{
  background: #f0fdf4;
  border-right: 4px solid #22c55e;
  color: #166534;
}}

.callout-warning {{
  background: #fffbeb;
  border-right: 4px solid #f59e0b;
  color: #92400e;
}}

/* Step by Step */
.steps-container {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
}}

.step-card {{
  padding: 10px 12px;
  margin-bottom: 10px;
  background: #f8fafc;
  border-radius: 6px;
  border: 1px solid #f1f5f9;
}}

.step-card:last-child {{
  margin-bottom: 0;
}}

.step-num-title {{
  font-weight: 700;
  color: #1e293b;
  font-size: 9.5pt;
  margin-bottom: 4px;
}}

.step-body-text {{
  font-size: 9pt;
  color: #475569;
  margin-bottom: 6px;
}}

.step-verify {{
  font-size: 8.5pt;
  color: #059669;
  background: #ecfdf5;
  padding: 4px 8px;
  border-radius: 4px;
  display: inline-block;
}}

/* Dialogue / Sandbox Transcripts */
.transcript-box {{
  background: #0f172a;
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
  color: #f8fafc;
}}

.transcript-header {{
  font-size: 8.5pt;
  color: #94a3b8;
  border-bottom: 1px solid #1e293b;
  padding-bottom: 6px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
}}

.dialogue-turn {{
  margin-bottom: 8px;
  padding: 8px 10px;
  border-radius: 6px;
  font-size: 9pt;
  line-height: 1.6;
}}

.dialogue-user {{
  background: rgba(99, 102, 241, 0.2);
  border-right: 3px solid #6366f1;
  color: #e0e7ff;
}}

.dialogue-assistant {{
  background: rgba(30, 41, 59, 0.8);
  border-right: 3px solid #10b981;
  color: #f1f5f9;
}}

.dialogue-tool {{
  background: rgba(15, 23, 42, 0.95);
  border-right: 3px solid #f59e0b;
  font-family: Consolas, monospace;
  font-size: 8pt;
  color: #fde68a;
  direction: ltr;
  text-align: left;
}}

.dialogue-result {{
  background: rgba(15, 23, 42, 0.7);
  border-right: 3px solid #64748b;
  font-family: Consolas, monospace;
  font-size: 8pt;
  color: #cbd5e1;
  direction: ltr;
  text-align: left;
}}

/* Quiz Card */
.quiz-section {{
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 14px 16px;
  margin: 16px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}}

.quiz-title-badge {{
  display: inline-block;
  background: #312e81;
  color: #ffffff;
  font-size: 8pt;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 700;
  margin-bottom: 6px;
}}

.quiz-question {{
  font-weight: 700;
  font-size: 9.5pt;
  color: #0f172a;
  margin-bottom: 10px;
}}

.quiz-options-list {{
  list-style: none;
  padding: 0;
  margin: 0 0 12px 0;
}}

.quiz-option-item {{
  padding: 6px 10px;
  margin-bottom: 6px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 8.5pt;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 8px;
}}

.quiz-letter {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  background: #e2e8f0;
  color: #1e293b;
  border-radius: 50%;
  font-size: 8pt;
  font-weight: 700;
  flex-shrink: 0;
}}

.quiz-explanation {{
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 8.5pt;
  color: #166534;
  line-height: 1.6;
}}

.quiz-correct-badge {{
  font-weight: 700;
  color: #15803d;
  margin-bottom: 2px;
}}

/* Vocabulary Grid */
.terms-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 12px 0;
}}

.term-card {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px 10px;
}}

.term-name {{
  font-weight: 700;
  color: #4338ca;
  font-size: 9pt;
  margin-bottom: 2px;
}}

.term-desc {{
  font-size: 8pt;
  color: #475569;
  line-height: 1.5;
}}

/* Table Styles */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  font-size: 8.5pt;
}}

th, td {{
  padding: 8px 10px;
  border: 1px solid #e2e8f0;
  text-align: right;
}}

th {{
  background: #f1f5f9;
  color: #1e293b;
  font-weight: 700;
}}

tr:nth-child(even) {{
  background: #f8fafc;
}}

/* Cheatsheet Grid */
.cs-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
  margin: 10px 0;
}}

.cs-card {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px 12px;
}}

.cs-cmd {{
  font-family: Consolas, monospace;
  font-size: 8.5pt;
  color: #1e1b4b;
  font-weight: 700;
  direction: ltr;
  text-align: left;
  display: block;
  margin-bottom: 3px;
}}

.cs-desc {{
  font-size: 8.5pt;
  color: #475569;
}}
"""

html_out = []
html_out.append("<!DOCTYPE html>")
html_out.append("<html lang='fa' dir='rtl'>")
html_out.append("<head>")
html_out.append("<meta charset='UTF-8'>")
html_out.append("<title>آموزش جامع وایب کدینگ با کلود کد (Claude Code)</title>")
html_out.append(f"<style>{css}</style>")
html_out.append("</head>")
html_out.append("<body>")

# --- 1. COVER PAGE ---
html_out.append("""
<div class="cover-page">
  <div class="cover-header">
    <div class="cover-badge">⚡ دوره جامع مهندسی نرم‌افزار ایجنتیک (Agentic AI) ۲۰۲۶</div>
    <div class="cover-title-group">
      <h1>راهنمای جامع وایب کدینگ<br>با کلود کد (Claude Code)</h1>
      <div class="cover-subtitle">
        آموزش صفر تا صد، مفهومی و عملی از مبانی ترمینال تا استقرار پروژه‌های مدرن بر مبنای سرفصل‌های رسمی Vibe Code School
      </div>
    </div>
    <div class="cover-tags">
      <span class="cover-tag">🚀 ۵ فصل تخصصی</span>
      <span class="cover-tag">📚 ۲۸ درس پروژه محور</span>
      <span class="cover-tag">🛠️ چیت‌شیت جامع ۱۳ گانه</span>
      <span class="cover-tag">📖 واژه‌نامه ۸۳ اصطلاح هوش مصنوعی</span>
      <span class="cover-tag">💡 آزمون‌های تستی با تشریح پاسخ</span>
    </div>
  </div>

  <div class="cover-meta-table">
    <div class="cover-meta-row">
      <span class="cover-meta-label">مرجع و منبع اصلی:</span>
      <span class="cover-meta-val">Vibe Code School (Dinesh Puppala) & Anthropic</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">ترجمه، تبیین و تنظیم تخصصی:</span>
      <span class="cover-meta-val">مهدی حیدرپور (MahdiDev)</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">تایپوگرافی و قلم:</span>
      <span class="cover-meta-val">فونت وزیرمتن (Vazirmatn) — کاملاً راست‌به‌چپ (RTL)</span>
    </div>
    <div class="cover-meta-row">
      <span class="cover-meta-label">تاریخ انتشار:</span>
      <span class="cover-meta-val">آبان ۱۴۰۳ (مطابق با نسخه ۲۰۲۶)</span>
    </div>
  </div>
</div>
""")

# --- 2. PREFACE & MANIFESTO ---
html_out.append("""
<div class="page-break"></div>
<h2>سخن آغازین: مانیفست وایب کدینگ و عصر ایجنت‌های هوشمند</h2>

<p>
در سال‌های اخیر، مفهوم برنامه‌نویسی و مهندسی نرم‌افزار با بزرگ‌ترین زلزله پارادایمی تاریخ خود مواجه شده است. اصطلاح <strong>وایب کدینگ (Vibe Coding)</strong> که نخستین بار توسط <em>آندری کارپاتی (Andrej Karpathy)</em>، از بنیان‌گذاران پیشین OpenAI و مدیر اسبق هوش مصنوعی تسلا مطرح گردید، به یک تغییر رویکرد شگرف اشاره دارد: <strong>پایان عصر تایپ کاراکتر به کاراکتر سینتکس و آغاز عصر هدایت نتایج نهایی به وسیله ایجنت‌ها.</strong>
</p>

<div class="callout callout-info avoid-break">
  <strong>تعریف رسمی وایب کدینگ:</strong>
  «ساخت نرم‌افزارهای کامل از طریق توصیف آنچه می‌خواهید به یک ایجنت خودمختار، ارزیابی هوشمندانه نتایج و هدایت مسیر، به جای درگیر شدن با جزئیات خسته‌کننده خطوط کد.»
</div>

<h3>تفاوت بنیادین ابزارهای تکمیل خودکار با Claude Code</h3>
<p>
ابزارهای نسل پیشین (مانند افزونه‌های Autocomplete قدیمی در ادیتورها) مانند یک دستیار منفعل عمل می‌کردند که صرفاً چند کلمه جلوتر را حدس می‌زدند. اما <strong>کلود کد (Claude Code)</strong> یک <strong>ایجنت ترمینال (Terminal-Native Agent)</strong> است. این ایجنت:
</p>
<ul>
  <li>به فایل‌های واقعی مخزن شما دسترسی محلی دارد و با ابزارهای Read, Edit, Write آن‌ها را ویرایش می‌کند.</li>
  <li>می‌تواند فرامین خط فرمان (Bash, PowerShell) را اجرا کند، لاگ‌های خطا را ببیند و خودش را تصحیح نماید.</li>
  <li>تست‌های پروژه را اجرا می‌کند و تا سبز شدن تست‌ها به چرخه ادامه می‌دهد.</li>
  <li>دارای <strong>دروازه‌های امنیتی مجوز (Permission Gates)</strong> است تا هرگز اقدام مخربی بدون اجازه صریح شما رخ ندهد.</li>
</ul>

<h3>سه قانون طلایی موفقیت در وایب کدینگ</h3>
<ol>
  <li><strong>مشخصات و قیود پیش از شروع (Spec & Constraints First):</strong> تمام محدودیت‌ها، تایپ‌ها و انتظارات را در ابتدای چرخه مشخص کنید؛ اصلاح مسیر در میانه کار توکن‌های زیادی را هدر می‌دهد.</li>
  <li><strong>چرخه تست قرمز به سبز (Red-to-Green Loop):</strong> ابتدا رفتار سیستم را با تست‌های شکست‌خورده اثبات کنید؛ تست‌ها قطب‌نمای هدایت ایجنت هستند.</li>
  <li><strong>شجاعت در آزمایش به لطف چک‌پوینت‌ها (Fearless Iteration):</strong> کلود کد قبل از هر تغییر فایل، چک‌پوینت ایجاد می‌کند. با دستور <code>/rewind</code> هر لحظه می‌توانید بدون درگیر شدن با گیت به عقب بازگردید.</li>
</ol>
""")

# --- 3. TABLE OF CONTENTS ---
html_out.append("""
<div class="page-break"></div>
<h2>فهرست تفصیلی مطالب کتابچه</h2>
<div class="toc-box">
""")

for m in course_data:
    mid = m["id"]
    m_info = MODULES_TRANSLATION.get(mid, {})
    html_out.append(f"<div class='toc-module-title'>{m_info.get('title_fa', m['title'])}</div>")
    html_out.append("<ul class='toc-list'>")
    for l in m["lessons"]:
        lid = l["id"]
        l_info = LESSONS_TRANSLATION.get(lid, {})
        title_fa = l_info.get("title_fa", l.get("title", ""))
        kind_fa = l_info.get("kind_fa", l.get("kind", ""))
        duration = l_info.get("duration_fa", "۵ دقیقه")
        html_out.append(f"<li class='toc-item'><span>{title_fa}</span><span style='color:#64748b;'>{kind_fa} · {duration}</span></li>")
    html_out.append("</ul>")

html_out.append("""
  <div class="toc-module-title">ضمایم و مراجع تخصصی</div>
  <ul class="toc-list">
    <li class="toc-item"><span>ضمیمه شماره ۱: چیت‌شیت جامع و مرجع سریع کلود کد (۱۳ بخش)</span><span style="color:#64748b;">چیت‌شیت 🛠️</span></li>
    <li class="toc-item"><span>ضمیمه شماره ۲: واژه‌نامه و اصطلاح‌نامه تخصصی هوش مصنوعی و وایب کدینگ (۸۳ اصطلاح)</span><span style="color:#64748b;">دیکشنری 📖</span></li>
  </ul>
</div>
""")

# --- 4. MODULES & LESSONS RENDERING ---
lesson_counter = 1
for m in course_data:
    mid = m["id"]
    m_info = MODULES_TRANSLATION.get(mid, {})
    m_title_fa = m_info.get("title_fa", m["title"])
    m_summary_fa = m_info.get("summary_fa", m.get("summary", ""))
    m_icon = m_info.get("icon", "📌")

    # Module Splash Banner
    html_out.append(f"""
    <div class="module-banner">
      <div class="module-banner-num">{m_icon} ماژول {mid.replace('cc-m', '').upper()}</div>
      <h2 class="module-banner-title">{m_title_fa}</h2>
      <div class="module-banner-summary">{m_summary_fa}</div>
    </div>
    """)

    for l in m["lessons"]:
        lid = l["id"]
        l_info = LESSONS_TRANSLATION.get(lid, {})
        title_fa = l_info.get("title_fa", l.get("title", ""))
        kind_fa = l_info.get("kind_fa", l.get("kind", "درس"))
        duration = l_info.get("duration_fa", "۵ دقیقه")
        intro_fa = l_info.get("intro_fa", l.get("summary", ""))
        concept_fa = l_info.get("concept_deep_fa", "")

        html_out.append(f"""
        <div class="lesson-card">
          <div class="lesson-header avoid-break">
            <span class="lesson-badge">درس {lesson_counter:02d}</span>
            <span class="lesson-kind">{kind_fa}</span>
            <span class="lesson-duration">⏱️ زمان مطالعه: {duration}</span>
          </div>

          <h3 class="lesson-title">{title_fa}</h3>
          <div style="font-size: 8.5pt; color: #64748b; margin-top: -6px; margin-bottom: 10px; direction: ltr; text-align: left;">ID: {lid}</div>

          <div class="lesson-summary-box avoid-break">
            <strong>خلاصه اجرایی:</strong> {intro_fa}
          </div>

          <div class="concept-body">
            {concept_fa.strip()}
          </div>
        """)

        # Extra callouts or content items if available
        if "content" in l and isinstance(l["content"], list):
            for c_item in l["content"]:
                kind = c_item.get("kind")
                if kind == "callout":
                    tone = c_item.get("tone", "info")
                    text = c_item.get("text", "")
                    html_out.append(f"""
                    <div class="callout callout-{tone} avoid-break">
                      💡 <strong>نکته کاربردی:</strong> {text}
                    </div>
                    """)
                elif kind == "tabs":
                    tabs = c_item.get("tabs", [])
                    html_out.append("<div class='steps-container avoid-break'><strong>فرامین نصب برای سیستم‌عامل‌های مختلف:</strong>")
                    for tb in tabs:
                        html_out.append(f"<div style='margin-top:6px; font-size:9pt;'><strong>{tb.get('label')}:</strong><pre>{tb.get('code')}</pre></div>")
                    html_out.append("</div>")

        # Steps
        if "steps" in l and isinstance(l["steps"], list) and len(l["steps"]) > 0:
            html_out.append("<div class='steps-container avoid-break'>")
            html_out.append("<h4>🛠️ مراحل عملی و گام‌به‌گام (Hands-on Walkthrough):</h4>")
            for s_idx, st in enumerate(l["steps"], 1):
                s_title = st.get("title", "")
                s_body = st.get("body", "") or st.get("prompt", "")
                s_verify = st.get("verify", "")
                html_out.append(f"""
                <div class="step-card">
                  <div class="step-num-title">گام {s_idx:02d}: {s_title}</div>
                  <div class="step-body-text">{s_body}</div>
                  {f"<div class='step-verify'><strong>راستی‌آزمایی:</strong> {s_verify}</div>" if s_verify else ""}
                </div>
                """)
            html_out.append("</div>")

        # Transcript Sandbox Dialogue
        if "transcript" in l and isinstance(l["transcript"], list) and len(l["transcript"]) > 0:
            html_out.append("""
            <div class="transcript-box avoid-break">
              <div class="transcript-header">
                <span>💬 بازپخش نشست شبیه‌سازی‌شده (Sandbox Transcript Replay)</span>
                <span>Claude Code Agentic Loop</span>
              </div>
            """)
            for t_turn in l["transcript"][:8]:
                role = t_turn.get("role")
                t_text = t_turn.get("text", "")
                if role == "user":
                    html_out.append(f"<div class='dialogue-turn dialogue-user'><strong>👤 کاربر:</strong> {t_text}</div>")
                elif role == "assistant":
                    html_out.append(f"<div class='dialogue-turn dialogue-assistant'><strong>🤖 کلود:</strong> {t_text}</div>")
                elif role == "tool_call":
                    tool = t_turn.get("tool", "Tool")
                    inp = t_turn.get("input", "")
                    html_out.append(f"<div class='dialogue-turn dialogue-tool'>⚙️ [Tool Call] {tool}: {inp}</div>")
                elif role == "tool_result":
                    res = t_turn.get("result", "")[:160]
                    html_out.append(f"<div class='dialogue-turn dialogue-result'>⬅️ [Result]: {res}...</div>")
            html_out.append("</div>")

        # Quiz Section
        quizzes = l.get("quiz", [])
        if quizzes:
            html_out.append("<div class='quiz-section avoid-break'>")
            html_out.append("<div class='quiz-title-badge'>📝 سنجش درک مطلب و ارزیابی (Quiz)</div>")
            for q_idx, q in enumerate(quizzes, 1):
                raw_q = q.get("q", "")
                c_idx = q.get("correctIndex", 0)
                # Lookup Persian translation
                q_data = quizzes_map.get(raw_q, {})
                q_text_fa = q_data.get("q_fa", raw_q)
                options_fa = q_data.get("options_fa", q.get("options", []))
                exp_fa = q_data.get("explanation_fa", q.get("explanation", ""))

                html_out.append(f"""
                <div style="margin-bottom: 14px;">
                  <div class="quiz-question">پرسش {q_idx}: {q_text_fa}</div>
                  <ul class="quiz-options-list">
                """)

                letters = ["الف", "ب", "ج", "د"]
                for o_idx, opt in enumerate(options_fa):
                    is_correct = (o_idx == c_idx)
                    border_style = "border-right: 3px solid #10b981; font-weight: 600;" if is_correct else ""
                    html_out.append(f"""
                    <li class="quiz-option-item" style="{border_style}">
                      <span class="quiz-letter">{letters[o_idx] if o_idx < len(letters) else chr(65+o_idx)}</span>
                      <span>{opt}</span>
                    </li>
                    """)

                letter_correct = letters[c_idx] if c_idx < len(letters) else chr(65+c_idx)
                html_out.append(f"""
                  </ul>
                  <div class="quiz-explanation">
                    <div class="quiz-correct-badge">✅ پاسخ صحیح: گزینه «{letter_correct}»</div>
                    <div>{exp_fa}</div>
                  </div>
                </div>
                """)
            html_out.append("</div>")

        # Terms / Vocabulary
        struct_info = lessons_structured.get(lid, {})
        terms = struct_info.get("terms", [])
        if terms:
            html_out.append("<div class='avoid-break'>")
            html_out.append("<h4 style='color:#312e81; font-size:9.5pt;'>📚 اصطلاحات تخصصی این درس:</h4>")
            html_out.append("<div class='terms-grid'>")
            for tm in terms:
                t_name = tm.get("term", "")
                t_def = tm.get("definition", "")
                html_out.append(f"""
                <div class="term-card">
                  <div class="term-name">{t_name}</div>
                  <div class="term-desc">{t_def}</div>
                </div>
                """)
            html_out.append("</div>")
            html_out.append("</div>")

        html_out.append("</div>") # End lesson-card
        lesson_counter += 1

# --- 5. APPENDIX 1: THE COMPLETE CHEAT SHEET ---
html_out.append("""
<div class="page-break"></div>
<div class="module-banner">
  <div class="module-banner-num">🛠️ بخش ضمیمه شماره ۱</div>
  <h2 class="module-banner-title">چیت‌شیت جامع و مرجع سریع کلود کد (Claude Code Cheat Sheet)</h2>
  <div class="module-banner-summary">
    تمام فرامین ترمینال، دستورات اسلش، کلیدهای میانبر، سطوح دسترسی، تنظیمات، هوک‌ها، سرورهای MCP و شیوه‌نامه‌های طلایی وایب کدینگ در یک نگاه.
  </div>
</div>
""")

for cs in cheatsheet_fa:
    html_out.append(f"""
    <div class="avoid-break" style="margin-bottom: 20px;">
      <h2>{cs['title_fa']}</h2>
      <p style="font-size: 9.5pt; color: #475569; margin-bottom: 8px;">{cs['desc_fa']}</p>
      <div class="cs-grid">
    """)
    for it in cs["items"]:
        html_out.append(f"""
        <div class="cs-card">
          <span class="cs-cmd">{it['cmd']}</span>
          <span class="cs-desc">{it['desc_fa']}</span>
        </div>
        """)
    html_out.append("</div></div>")

# --- 6. APPENDIX 2: AI & VIBE CODING GLOSSARY ---
html_out.append("""
<div class="page-break"></div>
<div class="module-banner">
  <div class="module-banner-num">📖 بخش ضمیمه شماره ۲</div>
  <h2 class="module-banner-title">واژه‌نامه و اصطلاح‌نامه تخصصی هوش مصنوعی و وایب کدینگ</h2>
  <div class="module-banner-summary">
    فرهنگ تشریحی ۸۳ اصطلاح کلیدی مهندسی مدل‌های زبانی بزرگ، یادگیری عمیق، و توسعه نرم‌افزار ایجنتیک با برگردان روان فارسی.
  </div>
</div>

<div class="terms-grid" style="grid-template-columns: 1fr;">
""")

for g in glossary_fa:
    html_out.append(f"""
    <div class="term-card avoid-break" style="padding: 10px 14px; margin-bottom: 6px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
        <span class="term-name" style="font-size:10pt;">{g['name_fa']}</span>
        <span style="font-family:Consolas, monospace; font-size:8.5pt; color:#6366f1; direction:ltr;">{g['name_en']}</span>
      </div>
      <div class="term-desc" style="font-size:9pt; line-height:1.65; color:#334155;">
        {g['desc_fa']}
      </div>
    </div>
    """)

html_out.append("</div>")

# --- 7. EPILOGUE & FOOTER ---
html_out.append("""
<div class="page-break"></div>
<div class="avoid-break" style="text-align: center; padding: 40px 20px;">
  <div style="font-size: 32pt; margin-bottom: 10px;">🚀</div>
  <h2 style="border:none; color:#312e81; font-size:18pt;">پایان کتابچه و آغاز سفر وایب کدینگ شما</h2>
  <p style="max-width: 650px; margin: 0 auto 16px auto; font-size: 10pt; line-height: 1.8; color: #475569;">
    شما اکنون تمامی مبانی، ابزارها، الگوهای فکری، و جریان‌های کاری وایب کدینگ با Claude Code را آموخته‌اید. به یاد داشته باشید که در این پارادایم نوین، قدرت شما در توانایی شما برای تعیین شفاف اهداف، معماری تمیز، و هدایت ایجنت خلاصه می‌شود.
  </p>
  <div class="callout callout-success" style="max-width: 600px; margin: 20px auto; text-align: right;">
    🌟 <strong>پیشنهاد بعدی:</strong> همین حالا ترمینال خود را باز کنید، دستور <code>claude</code> را در یکی از پروژه‌هایتان تایپ کنید و اولین سایدپروژه واقعی خود را با ریتم Spec → Tests → Code خلق کنید!
  </div>
  <div style="margin-top: 30px; font-size: 8.5pt; color: #94a3b8;">
    تهیه‌شده با عشق برای جامعه توسعه‌دهندگان مدرن وب · پاییز ۱۴۰۳ (مطابق با ۲۰۲۶)
  </div>
</div>
""")

html_out.append("</body>")
html_out.append("</html>")

full_html_str = "\n".join(html_out)
output_html_path = "vibe_coding_claude_code_complete.html"
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(full_html_str)

print(f"Generated {output_html_path} ({len(full_html_str)} chars).")

# Now let's call Brave Browser to print to PDF!
brave_exe = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
pdf_out_path = os.path.abspath("vibe_coding_claude_code_complete.pdf")
abs_html_path = os.path.abspath(output_html_path)

print("Starting Brave headless rendering to PDF...")
cmd = [
    brave_exe,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out_path}",
    abs_html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Brave returncode:", res.returncode)
if os.path.exists(pdf_out_path):
    size_mb = os.path.getsize(pdf_out_path) / (1024 * 1024)
    print(f"SUCCESS! Created PDF: {pdf_out_path} ({size_mb:.2f} MB)")
else:
    print("PDF creation failed. Stderr:", res.stderr)
