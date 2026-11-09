# فصل سوم: قابلیت‌های پیشرفته و قدرت‌بخش

> 📖 **منبع رسمی:** [Vibe Code School — Claude Code Course](https://vibecodeschool.com/courses/claude-code-vibe-coding)
> 🎯 **هدف این فصل:** دستورات اسلش توکار، اسلش کامندهای اختصاصی، مهارت‌های ایجنت (Agent Skills)، ساب‌ایجنت‌ها، مود برنامه‌ریزی (Plan Mode)، هوک‌های قبل و بعد از ابزار (Hooks) و سرورهای MCP — جعبه‌ابزاری که کلود کد را مطابق میل شما منعطف می‌سازد.

---

## ۱۲. دستورات اسلش توکار (Built-in Slash Commands)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-12-slash-commands` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** دستورات میانبر حیاتی: /init, /clear, /resume, /compact, /rewind, /model, /doctor, /cost. شناخت این‌ها مرز بین گیج شدن و هدایت مقتدرانه است.

### تبیین مفهومی و اصول مهندسی
دستورات اسلش میانبرهای درجه یک در محیط کلود کد هستند:
- دستور /init: پروژه را اسکن کرده و CLAUDE.md پایه را تولید می‌کند.
- دستور /clear: نشست جاری را کاملاً پاک می‌کند اما حافظه CLAUDE.md را حفظ می‌نماید؛ برای شروع تسک جدید ضروری است.
- دستور /compact: نشست طولانی را خلاصه می‌کند تا حافظه کانتکست آزاد شود بدون این‌که پیوستگی کار از بین برود.
- دستور /rewind (یا دوبار زدن کلید Escape): ماشین زمان شماست! کدهای تغییریافته یا مکالمه را به چک‌پوینت‌های قبلی برمی‌گرداند بدون درگیر شدن با گیت.
- دستور /model: سوئیچ سریع بین مدل‌ها (مثلاً استفاده از Opus برای طراحی معماری و سپس استفاده از Haiku برای ادیت‌های سریع).

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Try /init
Generates or updates CLAUDE.md by reading your repo. Use it once per project, then prune the output.
- **روش راستی‌آزمایی:** `A CLAUDE.md is written or updated at the project root.`

#### گام 02: Use /clear when context drifts
/clear wipes the conversation but keeps your project memory. Run it when you switch tasks — fresh context produces sharper plans.
- **روش راستی‌آزمایی:** `The chat starts a new session; CLAUDE.md is still loaded.`

#### گام 03: Resume a long session with /resume
If you closed Claude Code and want to pick up where you left off, /resume loads the previous session.
- **روش راستی‌آزمایی:** `The agent restates the goal of the prior session before you continue.`

#### گام 04: Compact when you must keep going
/compact summarizes the conversation so far so context doesn't blow up. Less destructive than /clear when you need continuity.
- **روش راستی‌آزمایی:** `The session continues with a much smaller context window than before.`

#### گام 05: Rewind when a change goes sideways
Claude Code checkpoints your files before each change. /rewind (or double-tap Escape) opens the checkpoint picker — restore the code, the conversation, or both. It's the undo button that makes bold experiments cheap.
- **روش راستی‌آزمایی:** `A picker lists recent checkpoints; selecting one restores that state without touching your git history.`

#### گام 06: Match the model to the task
/model switches models mid-session. Reach for the frontier tier (Opus 4.8, or the Claude 5 family where available) on hard refactors and planning; drop to Haiku 4.5 for fast, cheap iteration on simple edits.
- **روش راستی‌آزمایی:** `The picker shows the active model; the status line reflects your choice on the next turn.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** تفاوت میان دستورات `/clear` و `/compact` در چیست؟
- **الف)** هیچ تفاوتی ندارند و نام مستعار یکدیگرند.
- **ب)** دستور /clear کل گفتگو را پاک می‌کند؛ در حالی که /compact آن را خلاصه کرده تا فضا آزاد شود اما پیوستگی کار حفظ گردد.
- **ج)** دستور /clear ابزارها را فعال نگه می‌دارد اما /compact آن‌ها را غیرفعال می‌سازد.
- **د)** دستور /compact سریع‌تر از /clear اجرا می‌شود.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>دستور /clear برای شروع یک تسک کاملاً جدید است؛ اما /compact برای ادامه‌دادن کارهای طولانی با کانتکست بهینه‌شده استفاده می‌شود.</p>
</details>

**پرسش 2:** دستور `/rewind` چه چیزی را بازمی‌گرداند؟
- **الف)** فقط تاریخچه پیام‌های چت را.
- **ب)** یک چک‌پوینت از کدها، مکالمه یا هر دو را که قبل از هر تغییر به صورت خودکار ثبت شده است.
- **ج)** آخرین کامیت گیت را.
- **د)** تنها فایل‌های حذف‌شده را.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>دستور /rewind ماشین زمان کلود کد است و به شما اجازه می‌دهد کدهای تغییریافته یا کانتکست چت را بدون دستکاری گیت به حالت قبل برگردانید.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Clearing:** Wiping the session so the next request starts from an empty context window, keeping only the standing instructions.
- **Context:** Everything the agent currently has in front of it that bears on the task: loaded files, your messages, tool results so far.
- **Model:** The trained network itself: billions of parameters that turn a context into the next token, and nothing more.
- **Session:** One continuous run with an agent, from an empty context to the moment you clear it, close it, or hand its work off.
- **Compaction:** Replacing the session so far with a shorter summary of it, freeing the context window at the cost of detail.
- **Slash command:** A typed /name shortcut that runs a built-in action or expands a saved prompt, so the prompts you reuse live in the repo.

---

## ۱۳. نوشتن دستورات اسلش سفارشی (Custom Slash Commands)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-13-custom-slash-commands` | **زمان مطالعه:** ۷ دقیقه

> 💡 **خلاصه اجرایی:** پرامپت‌های پرتکرار تیم را به دستوراتی تک‌کلمه‌ای با یک کلید تبدیل کنید و آن‌ها را در پوشه `.claude/commands/` نگه‌داری نمایید.

### تبیین مفهومی و اصول مهندسی
با ایجاد فایل‌های مارک‌داون در مسیر `.claude/commands/`، می‌توانید فرامینی مانند `/review.md` یا `/fix-issue.md` بسازید. این فایل‌ها می‌توانند متغیرهای آرگومان `$ARGUMENTS` را دریافت کرده و یک پروسه استاندارد و مهندسی‌شده را برای کل تیم تضمین کنند.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Create the commands folder
Inside your repo, create the directory if it doesn't exist.
- **روش راستی‌آزمایی:** `.claude/commands/ exists at your project root.`

#### گام 02: Author the command
Write a markdown file with the prompt you want fired. Use $ARGUMENTS for inline arguments.
- **روش راستی‌آزمایی:** `.claude/commands/review-pr.md exists with that content.`

#### گام 03: Use it
From any session in that repo, type the command.
- **روش راستی‌آزمایی:** `The agent runs the prompt with 'auth module' substituted into $ARGUMENTS.`

#### گام 04: Iterate
Run the command. If the output is too long, too short, or wrong — edit the markdown and re-run. Slash commands evolve like any other prompt.
- **روش راستی‌آزمایی:** `After edits, the new behavior is live on the next invocation. No reload needed.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** دستورات اسلش سفارشی (Custom Slash Commands) در چه مسیری ذخیره می‌شوند؟
- **الف)** در فایل `.claude/config.json`.
- **ب)** در مسیر `.claude/commands/` به صورت فایل‌های مارک‌داون (`.md`).
- **ج)** در ریشه پروژه در فایل CLAUDE.md.
- **د)** در تنظیمات گلوبال کاربری سیستم‌عامل.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>هر فایل مارک‌داون درون مسیر `.claude/commands/<name>.md` مستقیماً به یک دستور اسلش جدید به نام `/<name>` تبدیل می‌شود.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Slash command:** A typed /name shortcut that runs a built-in action or expands a saved prompt, so the prompts you reuse live in the repo.

---

## ۱۴. مهارت‌های ایجنت (Agent Skills)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-28-agent-skills` | **زمان مطالعه:** ۹ دقیقه

> 💡 **خلاصه اجرایی:** مهارت یا Skill پوشه‌ای است شامل یک فایل SKILL.md، به همراه اسکریپت‌ها، قالب‌ها و راهنماها؛ روش استاندارد آموزش رفتارهای جدید به ایجنت.

### تبیین مفهومی و اصول مهندسی
اسکیل‌ها زمانی به کار می‌آیند که می‌خواهید ایجنت در یک دامنه خاص (مثل نوشتن کوئری بهینه برای دیتابیس، تبدیل کدهای فیگما به تیل‌ویند، یا بررسی چک‌لیست سئو) با تخصص کامل و متودولوژی خاص عمل کند. اسکیل‌ها به صورت خودکار با برچسب‌های متنی و نیازمندی‌های پرامپت فعال می‌شوند.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Scaffold a skill
Project skills live in .claude/skills/<name>/SKILL.md. Personal ones live in ~/.claude/skills/ and follow you across projects.
- **روش راستی‌آزمایی:** `The folder exists at your project root.`

#### گام 02: Write SKILL.md
Frontmatter carries the name and — most importantly — the description Claude matches against. The body is the playbook.
- **روش راستی‌آزمایی:** `SKILL.md exists with frontmatter and numbered instructions.`

#### گام 03: Trigger it naturally
Don't type a slash command — just ask in plain language and watch Claude pick the skill up.
- **روش راستی‌آزمایی:** `The transcript shows the skill loading, then the playbook being followed step by step.`

#### گام 04: Tune the description
If the skill didn't fire, the description didn't match how you actually ask. Rewrite it with the phrases you'd really use — that line is the routing layer.
- **روش راستی‌آزمایی:** `The same natural-language ask now reliably triggers the skill.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** تفاوت کلیدی میان یک دستور اسلش (Slash Command) و یک مهارت ایجنت (Agent Skill) در چیست؟
- **الف)** دستورات اسلش سریع‌تر هستند اما اسکیل‌ها کندترند.
- **ب)** دستور اسلش صریحاً توسط کاربر با تایپ کاراکتر / فراخوانی می‌شود؛ در حالی که مهارت به صورت خودکار توسط ایجنت بر اساس محتوای پرامپت فعال می‌گردد.
- **ج)** اسکیل‌ها فقط در زبان پایتون کار می‌کنند.
- **د)** هیچ تفاوتی ندارند.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>اسکیل‌ها مانند ابزارهای شناختی در جعبه‌ابزار ایجنت هستند که وقتی تسک نیازمند تخصص خاصی باشد، خود ایجنت آن‌ها را لود و اجرا می‌کند.</p>
</details>

**پرسش 2:** چرا داشتن ۳۰ مهارت مختلف در پروژه باعث اشغال و آلودگی پنجره کانتکست نمی‌شود؟
- **الف)** چون اسکیل‌ها با الگوریتم Zip فشرده می‌شوند.
- **ب)** چون ایجنت در ابتدا تنها متادیتا و توضیحات کوتاه اسکیل‌ها را در حافظه دارد و فقط زمانی که به مهارت نیاز باشد متن کامل آن را لود می‌کند.
- **ج)** چون اسکیل‌ها خارج از حافظه مدل زبانی اجرا می‌گردند.
- **د)** چون سقف مصرف توکن برای اسکیل‌ها رایگان است.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>بارگذاری تنبل (Lazy Loading): فقط توصیف یک‌خطی مهارت‌ها در کانتکست است؛ محتوای کامل SKILL.md تنها در صورت تطابق با تسک بارگذاری می‌گردد.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Skill:** A named, reusable procedure the agent loads on demand: a folder of instructions and optional scripts, used when a task matches.
- **Slash command:** A typed /name shortcut that runs a built-in action or expands a saved prompt, so the prompts you reuse live in the repo.
- **Progressive disclosure:** Giving the agent a short index up front and letting it load the detail only when a task calls for it.

---

## ۱۵. ساب‌ایجنت‌ها و ابزار ایجنت (Subagents & Agent Tool)

**برچسب:** `مفهوم بنیادین 💡` | **شناسه درس:** `cc-14-subagents` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** یک ساب‌ایجنت، یک نشست تازه و موازی از کلود است که توسط ایجنت اصلی برای انجام کاری مشخص و متمرکز متولد می‌شود.

### تبیین مفهومی و اصول مهندسی
مشکل کارهای بزرگ در هوش مصنوعی این است که لاگ‌های پرحجم و جستجوهای پراکنده، کانتکست ایجنت اصلی را آلوده و کند می‌کنند. ساب‌ایجنت در یک کانتکست ایزوله متولد می‌شود، تمام جستجوها و آزمایش‌ها را انجام می‌دهد، و صرفاً یک «چکیده خالص و نتیجه نهایی» به ایجنت اصلی برمی‌گرداند.

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چه زمانی استفاده از یک ساب‌ایجنت (Subagent) تصمیم درستی است؟
- **الف)** برای ویرایش فایل‌های تک‌خطی ساده.
- **ب)** برای انجام جستجوهای عمیق، خواندن دهها فایل و آزمون‌های پرتکرار که ممکن است کانتکست ایجنت اصلی را آلوده و شلوغ کنند.
- **ج)** تنها زمانی که اینترنت قطع است.
- **د)** برای کامیت زدن به گیت.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>ساب‌ایجنت کار کثیف و پرحجم جستجو را در یک اتاق تمیز و مجزا انجام می‌دهد و فقط عصاره و نتیجه نهایی را به جلسه اصلی بازمی‌گرداند.</p>
</details>

**پرسش 2:** ساب‌ایجنت چه چیزی را به ایجنت اصلی بازمی‌گرداند؟
- **الف)** کل تاریخچه تمامی توکن‌ها و لاگ‌های اجراشده‌اش را.
- **ب)** یک پاسخ خلاصه‌شده و متمرکز که هدف تسک تفویض‌شده را مستقیماً پاسخ می‌دهد.
- **ج)** فایل‌های سیستم‌عامل را در قالب آرشیو tar.
- **د)** هیچ خروجی برنمی‌گرداند و کار را در پس‌زمینه خاتمه می‌دهد.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>ساب‌ایجنت یک خلاصه استخراج‌شده و نهایی از پاسخ تسک برمی‌گرداند؛ بنابراین کانتکست ایجنت اصلی سبک و شفاف باقی می‌ماند.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Subagent:** A separate agent the main agent spins up for a bounded task, with its own context window; only its final report comes back.
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.
- **Context:** Everything the agent currently has in front of it that bears on the task: loaded files, your messages, tool results so far.
- **Context window:** The fixed-size buffer of tokens a model can read in one request; if something isn't in it, the model can't see it.
- **System prompt:** The standing instructions the harness puts in front of every request: who the agent is, what tools it has, how it should behave.

---

## ۱۶. مود برنامه‌ریزی (Plan Mode)

**برچسب:** `شبیه‌ساز مکالمه 💬` | **شناسه درس:** `cc-15-plan-mode` | **زمان مطالعه:** ۷ دقیقه

> 💡 **خلاصه اجرایی:** در مود برنامه‌ریزی، ایجنت اجازه خواندن، جستجو و استدلال دارد، اما حق دستکاری کدها یا اجرای کامندهای مخرب را ندارد.

### تبیین مفهومی و اصول مهندسی
کلید میانبر Shift+Tab شما را بین مود معمولی و مود Plan جابه‌جا می‌کند (یا از طریق فلگ `--permission-mode plan`). در این مود، ایجنت مخزن را شخم می‌زند و یک نقشه راه گام‌به‌گام و تاییدپذیر ارائه می‌دهد. بعد از توافق بر سر پلن، مود را تغییر می‌دهید تا اجرای سریع آغاز شود.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: [Plan mode] Migrate our auth from session cookies to JWTs. Don't change anything yet — propose the plan.
[کلود کد]: Reading current auth implementation first.
[کلود کد]: Plan:
1. Add JWT issue/verify utilities (src/auth/jwt.ts).
2. Replace session middleware with JWT middleware; keep req.user shape stable.
3. Update 6 call sites that read req.session — they should switch to req.user.
4. Add tests for: valid token, expired token, missing token, malformed.
5. Migration: keep old session middleware behind a flag for one release.

No edits yet. Approve to proceed.
[کاربر]: Approved. Go.
[کلود کد]: Exiting plan mode. Acting now.
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چرا در مود برنامه‌ریزی (Plan Mode) ویرایش فایل‌ها ممنوع است؟
- **الف)** چون مدل‌های هوش مصنوعی توانایی نوشتن در این مود را ندارند.
- **ب)** تا ایجنت قبل از دستکاری کدهای سیستم، فرصت کاوش عمیق، درک معماری و جلب رضایت شما روی نقشه راه را پیدا کند.
- **ج)** برای صرفه‌جویی در فضای هارد دیسک.
- **د)** چون گیت در مود پلن قفل می‌شود.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>مود پلن فضایی امن برای تفکر خالص و تحلیل ریسک است بدون این‌که نگران شکستن کدها قبل از توافق نهایی باشید.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Plan mode:** A read-only agent mode: the agent may search and read, but must propose a plan for your approval before it edits anything.
- **Session:** One continuous run with an agent, from an empty context to the moment you clear it, close it, or hand its work off.

---

## ۱۷. هوک‌ها: قبل و بعد از ابزارها (Pre & Post Tool Hooks)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-16-hooks` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** هوک‌ها به شما اجازه می‌دهند منطق سفارشی خود را درون حلقه ایجنت تزریق کنید: اجرای اجباری لینتر یا جلوگیری از دستورات پرخطر.

### تبیین مفهومی و اصول مهندسی
دو نوع هوک اصلی داریم:
- PreToolUse: پیش از اجرای یک ابزار شل یا ادیت فعال می‌شود؛ اگر اسکریپت خروجی غیر صفر (مثل exit 2) برگرداند، عملیات ایجنت متوقف شده و به کاربر گزارش می‌شود.
- PostToolUse: بلافاصله پس از ادیت فایل اجرا می‌شود؛ مثلاً اجرای خودکار prettier یا eslint تا کدهای تولیدی همیشه استاندارد و تمیز بمانند.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Open the settings file
Create or open the project settings.
- **روش راستی‌آزمایی:** `An empty or existing settings.json opens.`

#### گام 02: Add a post-edit format hook
Run prettier on every Edit/Write to keep code consistent without asking the agent.
- **روش راستی‌آزمایی:** `After the agent edits a file, you see prettier run in the tool stream.`

#### گام 03: Add a pre-bash safety hook
Block the agent from running risky commands without asking. The hook intercepts and you decide.
- **روش راستی‌آزمایی:** `Bash calls now route through your script. Add a deny list for things like `rm -rf /` and `git push --force`.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** تنظیمات هوک‌ها (Hooks) در کجا تعریف و نگه‌داری می‌شوند؟
- **الف)** در کرنل سیستم‌عامل.
- **ب)** در فایل تنظیمات کلود کد در مسیر `.claude/config.json` یا تنظیمات پروژه تحت کلید hooks.
- **ج)** در داخل کدهای سورس برنامه.
- **د)** در متغیرهای فایل .env.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>هوک‌ها درون تنظیمات پیکربندی کلود کد قرار می‌گیرند و به ابزارها و الگوهای دستورات متصل می‌شوند.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.
- **Hooks:** Commands you configure the harness to run at fixed moments, such as before or after a tool call, regardless of what the model wants.
- **Tool call:** The model's request to run a tool: a structured message naming the tool and its arguments, which the harness then executes.

---

## ۱۸. سرورهای پروتکل متنی مدل (MCP Servers)

**برچسب:** `مفهوم بنیادین 💡` | **شناسه درس:** `cc-17-mcp-servers` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** پروتکل MCP (Model Context Protocol) استاندارد باز برای اتصال کلود به دیتابیس‌ها، مرورگرها، مستندات، ایشیوهای گیت‌هاب و سرویس‌های خارجی است.

### تبیین مفهومی و اصول مهندسی
ابزارهای توکار کلود کد، به ایجنت یک ترمینال روی رایانه شما می‌دهند؛ اما سرورهای MCP به ایجنت دسترسی به کل اینترنت، دیتابیس‌های Postgres و Mongo، ایشیوهای گیت‌هاب و جیرا، و حتی کنسول‌های ابری را اهدا می‌کنند. اتصال این سرورها با دستور تک‌خطی `claude mcp add` انجام می‌شود.

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** پروتکل MCP (Model Context Protocol) چه وظیفه‌ای دارد؟
- **الف)** مدل‌های جدید هوش مصنوعی را آموزش می‌دهد.
- **ب)** یک استاندارد باز و یکپارچه فراهم می‌سازد تا ایجنت بتواند با دیتابیس‌ها، سرویس‌های ابری، مرورگرها و ابزارهای خارجی ارتباط برقرار کند.
- **ج)** کدهای جاوااسکریپت را به تایپ‌اسکریپت کامپایل می‌کند.
- **د)** رمز عبور سیستم را نگه‌داری می‌نماید.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>پروتکل MCP پلی جهان‌شمول است که به ایجنت‌ها اجازه می‌دهد به جای محدود شدن به ترمینال محلی، با تمام سرویس‌های دنیای وب سخن بگویند.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **MCP:** Model Context Protocol: an open standard for plugging external tool servers into any agent harness.
- **Tool:** A named capability the harness lets the model invoke, such as reading a file, running a shell command or fetching a page.
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.

---

## ✅ جمع‌بندی فصل سوم: قابلیت‌های پیشرفته و قدرت‌بخش
- تسلط بر مفاهیم و فرامین مطرح‌شده در این فصل پایه و اساس موفقیت شما در ادامه مسیر است.
- همواره پیش از ورود به فصل بعد، تمرینات و فرامین را در یک پروژه واقعی تست کنید.

➡️ **گام بعدی:** [رفتن به ۰۴ — الگوها و تکنیک‌های وایب کدینگ](./04-vibe-coding-patterns.md)