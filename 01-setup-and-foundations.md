# فصل اول: راه‌اندازی و مبانی بنیادین

> 📖 **منبع رسمی:** [Vibe Code School — Claude Code Course](https://vibecodeschool.com/courses/claude-code-vibe-coding)
> 🎯 **هدف این فصل:** نصب و راه‌اندازی ابزار خط فرمان، درک عمیق چرخه ایجنتیک (Agentic Loop)، و پیکربندی حافظه مانا پروژه (CLAUDE.md). در پایان این فصل شما کاملاً بر محیط خط فرمان مسلط و آماده تعامل هستید.

---

## ۰۱. کلود کد چیست؟ (What Is Claude Code)

**برچسب:** `مفهوم بنیادین 💡` | **شناسه درس:** `cc-01-what-is-claude-code` | **زمان مطالعه:** ۵ دقیقه

> 💡 **خلاصه اجرایی:** کلود کد (Claude Code) صرفاً یک ابزار تکمیل خودکار کد (Autocomplete) نیست؛ بلکه یک ایجنت هوشمند مستقل است که مستقیماً در ترمینال شما اجرا می‌شود: فایل‌ها را می‌خواند، فرامین سیستم‌عامل را اجرا می‌کند، کدها را ویرایش می‌نماید و برای اقدامات مهم منتظر تایید شما می‌ماند.

### تبیین مفهومی و اصول مهندسی
تغییر بزرگ ذهنی در وایب کدینگ (Vibe Coding) این است: به جای این‌که ساعت‌ها وقت صرف تایپ کاراکتر به کاراکتر کدها و سر و کله زدن با سینتکس کنید، «نتیجه و هدف نهایی» (Outcomes) را برای ایجنت توصیف می‌کنید. شما در ارتفاع بالاتری از تفکر قرار می‌گیرید؛ شما تمرکزتان را روی «چه چیزی» (What) می‌گذارید و ایجنت به نحو احسن بخش «چگونه» (How) را اجرا می‌کند.

کلود کد ابزاری محلی در سیستم‌عامل شماست. این ایجنت با دستورات bash، ابزارهای جستجو مانند grep و glob، و ویرایشگر فایل مستقیماً به مخزن پروژه شما متصل است. اما وجه تمایز حیاتی آن، وجود «دروازه‌های مجوز» (Permission Gates) است؛ یعنی برای هر عملیاتی که ریسک داشته باشد یا تغییری دائمی ایجاد کند، ایجنت توقف کرده و از شما تاییدیه صریح می‌گیرد.

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** کدام مورد توصیف دقیق‌تری از کلود کد (Claude Code) است؟
- **الف)** یک افزونه IDE که همان‌طور که تایپ می‌کنید کد را تکمیل خودکار می‌کند.
- **ب)** یک ایجنت خط فرمان (CLI) که مخزن شما را می‌خواند، دستورات را اجرا می‌کند و با تایید شما کدها را ادیت می‌نماید.
- **ج)** یک پلتفرم ابری SaaS که کدهای شما را میزبانی کرده و تست‌ها را آنجا اجرا می‌کند.
- **د)** یک ربات بررسی کد (Code Review) که روی پول‌ریکوئست‌های گیت‌هاب کامنت می‌گذارد.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>کلود کد به صورت محلی به عنوان یک ابزار خط فرمان روی رایانه شما اجرا می‌شود؛ می‌تواند فایل‌ها را بخواند، دستورات شل را ران کند و کدها را ویرایش نماید، اما هر اقدام پرمخاطره با یک تاییدیه امنیتی متوقف می‌شود.</p>
</details>

**پرسش 2:** تغییر ذهنی و پارادایم بنیادین در «وایب کدینگ» (Vibe Coding) چیست؟
- **الف)** سپردن کامل انتشار کدها به هوش مصنوعی بدون هیچ‌گونه نظارت انسانی.
- **ب)** تایپ پرامپت‌ها به زبان طبیعی به جای کدنویسی.
- **ج)** توصیف نتایج و اهداف نهایی برای ایجنت و قضاوت خروجی‌ها، به جای تمرکز بر تک‌تک کاراکترهای سینتکس.
- **د)** سرعت بخشیدن به فرآیند کدنویسی با کپی‌پیست سریع‌تر کدهای تولیدی.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ج»</strong></p>
<p>وایب کدینگ یعنی کار کردن در ارتفاع فکری بالاتر: شما تمرکزتان را روی «چه چیزی» (What) و مشخصات سیستم می‌گذارید، و ایجنت هوشمند وظیفه سنگین پیاده‌سازی «چگونه» (How) را انجام می‌دهد.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.
- **Vibe coding:** Building software by describing what you want to an agent and judging the result rather than reading every line of code.
- **Permission request:** The harness pausing before a risky tool call to ask you yes or no; the simplest human-in-the-loop gate there is.

---

## ۰۲. نصب و راه‌اندازی ابزار خط فرمان (Install the CLI)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-02-install-the-cli` | **زمان مطالعه:** ۷ دقیقه

> 💡 **خلاصه اجرایی:** کلود کد را روی رایانه خود راه‌اندازی کرده و صحت عملکرد آن را با اجرای تست اولیه اعتبارسنجی کنید.

### تبیین مفهومی و اصول مهندسی
برای اجرای کلود کد، نیاز به یک حساب آنتروپیک با پلن فعال (یا کلید API آنتروپیک) دارید. خود بسته خط فرمان کاملاً رایگان نصب می‌شود و تنها هزینه مربوط به مصرف توکن‌های مدل هوش مصنوعی است.

توصیه رسمی استفاده از نصاب بومی (Native Installer) از طریق دستور curl در مک/لینوکس یا PowerShell در ویندوز است؛ زیرا نیازی به پیکربندی دستی Node.js ندارد و به‌روزرسانی‌های جدید را خودکار دریافت می‌کند. روش npm نیز برای توسعه‌دهندگانی که ترجیح می‌دهند با زنجیره ابزار جاوااسکریپت کار کنند کاملاً در دسترس است.

> 💡 **نکته کلیدی:** You need a Claude account with a **Pro or Max plan** (or an Anthropic API key). The install itself is free — the agent needs the account to think with.

#### دستورات نصب پلتفرم‌های مختلف:
- **macOS / Linux:**
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- **Windows:**
  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```
- **npm:**
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```

> ✅ **نکته کلیدی:** Verify with `claude --version` — a version number means the CLI is on your PATH and ready.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Install the CLI
Pick your platform in the tabs above and run the one-liner. The native installer is the recommended path — no Node.js required.
- **روش راستی‌آزمایی:** `A version number prints. If `command not found`, open a fresh terminal so PATH changes load.`

#### گام 02: Authenticate
Launch Claude Code from any directory. The first run opens a browser window for OAuth login with your Claude account.
- **روش راستی‌آزمایی:** `After login the prompt becomes interactive and shows your working directory in the header.`

#### گام 03: Pick a project
Quit (Ctrl+C twice) and re-run `claude` from inside an existing repo. The directory you launch from becomes the working tree the agent can read and edit.
- **روش راستی‌آزمایی:** `The header shows the project path. Type "hi" to confirm the agent responds.`

#### گام 04: Try a smoke test
Ask the agent to describe your repo. If it can list files and summarize the structure, your install is healthy.
- **روش راستی‌آزمایی:** `You should see a Read tool call against your files, then a 3-line summary.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** کدام پوشه به عنوان دایرکتوری کاری (Working Tree) کلود کد تعیین می‌شود؟
- **الف)** پوشه خانگی سیستم کاربر (Home Directory).
- **ب)** پوشه‌ای که دستور claude را درون آن از ترمینال اجرا کرده‌اید.
- **ج)** ریشه درایو اصلی سیستم‌عامل.
- **د)** پوشه مخفی .git در پروژه.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>دایرکتوری‌ای که دستور claude را در آن فراخوانی می‌کنید، ریشه کاری ایجنت می‌شود و تمامی ابزارهای خواندن، جستجو و ویرایش فایل در همان محدوده فعال خواهند بود.</p>
</details>

---

## ۰۳. اولین مکالمه با ایجنت (Your First Conversation)

**برچسب:** `شبیه‌ساز مکالمه 💬` | **شناسه درس:** `cc-03-first-conversation` | **زمان مطالعه:** ۶ دقیقه

> 💡 **خلاصه اجرایی:** مشاهده چرخه ایجنتیک در عمل: یک پرامپت، یک فراخوانی ابزار، یک نتیجه، و پاسخ نهایی. این ریتم، نبض تپنده وایب کدینگ است.

### تبیین مفهومی و اصول مهندسی
هر تعاملی در کلود کد یک چرخه تکرارشونده است. شما با زبان طبیعی سخن می‌گویید. ایجنت ابتدا تحلیل می‌کند که آیا برای پاسخ دقیق نیاز به اطلاعات واقعی از سیستم و کدهای شما دارد یا خیر. اگر پاسخ مثبت باشد، ابزار مناسبی مانند Read یا Grep یا Bash را فراخوانی می‌کند و منتظر دریافت خروجی واقعی می‌ماند. سپس داده‌ها را تحلیل کرده و مجدداً صحبت می‌کند. این حلقه تا پایان کامل کار یا مداخله شما ادامه دارد.

نکته بنیادین: ایجنت هرگز حدس نمی‌زند و توهم نمی‌بافد؛ بلکه قبل از خلاصه‌سازی فایل، آن را می‌خواند تا پاسخی مستند و مبتنی بر حقیقت (Grounded Answer) ارائه دهد.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: Open the README and tell me what this project does in one sentence.
[کلود کد]: I'll read the README first, then summarize.
[کلود کد]: It's an interactive curriculum that teaches three agentic coding tools — Claude Code, Codex for mobile, and Antigravity — end to end.
[کاربر]: Are there any failing tests?
[کلود کد]: Let me check by running the test suite.
[کلود کد]: Two tests, both passing. The suite is green.
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چرا ایجنت قبل از خلاصه‌سازی فایل README، ابتدا ابزار Read را فراخوانی کرد؟
- **الف)** چون این کار در پرامپت سیستمی اجباری شده بود.
- **ب)** چون برای ارائه پاسخی مستند و دقیق به جای حدس و توهم، به محتوای واقعی فایل نیاز داشت.
- **ج)** چون ابزار Read سریع‌تر از حافظه درونی مدل است.
- **د)** چون ایجنت همیشه قبل از هر کاری باید فایل README.md را بخواند.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>ایجنت بر خلاف مدل‌های سنتی حدس نمی‌زند؛ بلکه با فراخوانی ابزار Read، داده‌های مستند و زنده را از دیسک واکشی کرده و پاسخی کاملاً بر پایه واقعیت (Grounded) تولید می‌کند.</p>
</details>

**پرسش 2:** حلقه تکرارشونده در این مکالمه چگونه بود؟
- **الف)** کاربر → خواندن فایل → پایان کار.
- **ب)** کاربر → تصمیم ایجنت → فراخوانی ابزار → نتیجه ابزار → پاسخ نهایی ایجنت.
- **ج)** ایجنت → کاربر → ابزار → اتمام.
- **د)** ابزار → کاربر → ایجنت → ابزار.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>چرخه استاندارد ایجنتیک شامل: دریافت پرامپت کاربر، تحلیل نیاز به ابزار، اجرای ابزار و دریافت نتیجه، و سرانجام فرموله‌سازی پاسخ نهایی است.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.
- **Tool:** A named capability the harness lets the model invoke, such as reading a file, running a shell command or fetching a page.
- **Tool call:** The model's request to run a tool: a structured message naming the tool and its arguments, which the harness then executes.

---

## ۰۴. چرخه ایجنتیک (The Agentic Loop)

**برچسب:** `مفهوم بنیادین 💡` | **شناسه درس:** `cc-04-the-agentic-loop` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** ریتم چهارگانه: برنامه‌ریزی (Plan) → اقدام (Act) → مشاهده (Observe) → تنظیم (Adjust). شناخت این چرخه مرز میان جنگیدن با ایجنت و همراهی روان با آن است.

### تبیین مفهومی و اصول مهندسی
هر اقدامی که ایجنت انجام می‌دهد از ریتم چهارضرب پی‌رویی می‌کند:
۱. برنامه‌ریزی (Plan): تعیین گام بعدی بر اساس هدف نهایی و زمینه فعلی.
۲. اقدام (Act): فراخوانی یک ابزار — خواندن فایل، اجرای دستور شل، یا ویرایش کد.
۳. مشاهده (Observe): خواندن دقیق خروجی ابزار و ارزیابی نتیجه.
۴. تنظیم (Adjust): به‌روزرسانی طرح اجرایی بر اساس بازخورد و تکرار چرخه.

وقتی این ریتم را درک کنید، دو اتفاق مهم می‌افتد: نخست این‌که وسواس مداخله‌های ناگهانی در میانه کار را کنار می‌گذارید و اجازه می‌دهید ایجنت خروجی را مشاهده کند؛ دوم این‌که یاد می‌گیرید تمامی قیود و شرایط حیاتی را از همان ابتدا و قبل از آغاز چرخه تعیین کنید (Front-loading Constraints)، زیرا بازتعریف قیود در میانه کار، هزینه بازبرنامه‌ریزی سنگینی به همراه دارد.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: Add a /health endpoint to the API. It should return {status: 'ok'} and have a test.
[کلود کد]: Plan: find the API entry point, add the route, add a test. Acting now.
[کلود کد]: I see Express. Adding the /health route and a Jest test next to existing tests.
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** کدام توالی یک ضرب از چرخه ایجنتیک (Agentic Loop) را توصیف می‌کند؟
- **الف)** برنامه‌ریزی (Plan) → اقدام (Act) → مشاهده (Observe) → تنظیم (Adjust).
- **ب)** اقدام → تست → کامیت → پوش.
- **ج)** پرامپت → پاسخ → اصلاح → خروج.
- **د)** فکر کردن → کدنویسی → بازبینی → تکرار.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «الف»</strong></p>
<p>ریتم ۴ گانه چرخه ایجنتیک شامل: تعیین گام بعدی (Plan)، فراخوانی ابزار (Act)، خواندن خروجی ابزار (Observe)، و به‌روزرسانی طرح اجرایی (Adjust) است.</p>
</details>

**پرسش 2:** چرا تعریف زودهنگام قیود (Front-loading Constraints) در ابتدای پرامپت ارزان‌تر از اضافه کردن آن‌ها در میانه کار است؟
- **الف)** چون مدل‌های زبانی فقط پرامپت اول را به خاطر می‌سپارند.
- **ب)** چون تغییر قید در میانه کار، ایجنت را مجبور به بازبرنامه‌ریزی، حذف کدهای نوشته‌شده و اتلاف توکن‌های فراوان می‌کند.
- **ج)** چون پرامپت‌های اولیه تخفیف مصرف توکن دارند.
- **د)** چون اضافه کردن قید در میانه کار نشست را ریست می‌کند.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>قیودی که از ابتدا مشخص باشند از گام اول در مسیر صحیح برنامه‌ریزی می‌شوند؛ اما قیود ناگهانی باعث شکست چرخه فعلی و هدررفت شدید زمان و توکن می‌شوند.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.

---

## ۰۵. حافظه مانا پروژه با CLAUDE.md (Project Memory)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-05-claude-md-and-memory` | **زمان مطالعه:** ۱۰ دقیقه

> 💡 **خلاصه اجرایی:** دستورالعمل‌های سطح پروژه که ایجنت به صورت خودکار بارگذاری می‌کند؛ پرقدرت‌ترین و اثربخش‌ترین اهرم مخزن در متدولوژی وایب کدینگ.

### تبیین مفهومی و اصول مهندسی
هر بار که کلود کد را در پوشه‌ای که حاوی فایل CLAUDE.md است باز می‌کنید، این فایل به صورت خودکار در کانتکست ایجنت تزریق می‌شود. این فایل نقش «حافظه مانا و قرارداد کاری» پروژه را بازی می‌کند.

یک فایل CLAUDE.md عالی باید کوتاه، تلگرافی و بسیار دقیق باشد. چیزهایی که ایجنت خودش با خواندن package.json متوجه می‌شود (مانند فریم‌ورک‌ها) را حذف کنید؛ در عوض چیزهایی را بنویسید که ایجنت هرگز خودش نمی‌تواند حدس بزند: قراردادهای معماری خاص تیم، نحوه اجرای تست‌ها و ساخت، پیچیدگی‌های استقرار، و اشتباهاتی که قبلاً ایجنت مرتکب شده و شما تذکر داده‌اید.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Run /init in a real project
From inside a project with code, type /init. The agent reads your repo and proposes a CLAUDE.md.
- **روش راستی‌آزمایی:** `A CLAUDE.md appears at your project root with sections like 'Stack' and 'Conventions'.`

#### گام 02: Trim aggressively
Open the generated file. Delete anything obvious from package.json (frameworks, scripts). Keep only: hidden conventions, deploy quirks, and rules you've corrected the agent on before.
- **روش راستی‌آزمایی:** `Your CLAUDE.md is under ~30 lines and every line says something the agent could not infer.`

#### گام 03: Test that it took
Quit and relaunch claude in the same directory. Ask a question whose answer requires the file.
- **روش راستی‌آزمایی:** `The agent answers "pnpm — npm install would corrupt the workspaces" without reading any other file.`

#### گام 04: Add a personal layer
Create ~/.claude/CLAUDE.md for cross-project preferences (your tone, your default test framework). It loads on every project, layered under the project file.
- **روش راستی‌آزمایی:** `These rules now apply in every Claude Code session you open.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چه مطالبی باید درون فایل CLAUDE.md قرار گیرند؟
- **الف)** کپی کامل تمام فایل‌های package.json و توضیحات معماری کلی وب.
- **ب)** دستورات بیلد، تست، قراردادهای مخفی پروژه، و قواعدی که قبلاً ایجنت را به خاطر نقض آن‌ها اصلاح کرده‌اید.
- **ج)** تاریخچه لاگ‌های کامل گیت و اسامی تمام مشارکت‌کنندگان.
- **د)** لیست تمام فایل‌های موجود در ریپازیتوری.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>فایل CLAUDE.md باید خلاصه و تلگرافی باشد و فقط اطلاعاتی را شامل شود که ایجنت خودش نمی‌تواند از روی کدهای منبع بفهمد.</p>
</details>

**پرسش 2:** لایه تنظیمات و دستورالعمل‌های شخصی کاربر در چه مسیری ذخیره می‌شود؟
- **الف)** در فایل `~/.claude/CLAUDE.md` در پوشه خانگی کاربر.
- **ب)** در پوشه `.git/config` پروژه.
- **ج)** در متغیرهای سیستمی ویندوز یا بش.
- **د)** در رجیستری سیستم‌عامل.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>فایل `~/.claude/CLAUDE.md` در دایرکتوری خانگی کاربر قرار دارد و تنظیمات شخصی او را در تمام پروژه‌ها زیر لایه تنظیمات پروژه تزریق می‌کند.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **AGENTS.md:** The instructions file at the repo root that every session reads first: commands, conventions, gotchas. CLAUDE.md in Claude Code.
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.
- **Slash command:** A typed /name shortcut that runs a built-in action or expands a saved prompt, so the prompts you reuse live in the repo.

---

## ✅ جمع‌بندی فصل اول: راه‌اندازی و مبانی بنیادین
- تسلط بر مفاهیم و فرامین مطرح‌شده در این فصل پایه و اساس موفقیت شما در ادامه مسیر است.
- همواره پیش از ورود به فصل بعد، تمرینات و فرامین را در یک پروژه واقعی تست کنید.

➡️ **گام بعدی:** [رفتن به ۰۲ — جریان‌های کاری هسته](./02-core-workflows.md)