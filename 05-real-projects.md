# فصل پنجم: پروژه‌های دنیای واقعی و استقرار

> 📖 **منبع رسمی:** [Vibe Code School — Claude Code Course](https://vibecodeschool.com/courses/claude-code-vibe-coding)
> 🎯 **هدف این فصل:** مطالعات موردی از صفر تا صد در مقیاس واقعی، نه مثال‌های اسباب‌بازی و تکراری: ساخت فیچرهای مدرن با Next.js، کدنویسی تست‌محور (TDD)، مهاجرت کدهای قدیمی و میرا، انتشار ایمن در پروداکشن، و تحویل پروژه نهایی.

---

## ۲۴. ساخت یک فیچر کامل در Next.js (Building a Next.js Feature)

**برچسب:** `پروژه عملی 🚀` | **شناسه درس:** `cc-23-nextjs-feature` | **زمان مطالعه:** ۱۰ دقیقه

> 💡 **خلاصه اجرایی:** پیاده‌سازی صفر تا صد یک ویژگی مدرن: خواندن ساختار پوشه‌ها، تعریف روت و صفحه، ساخت کامپوننت، اتصال استیت و تست کامل.

### تبیین مفهومی و اصول مهندسی
یک مطالعه موردی واقعی در Next.js App Router: ایجنت ابتدا درخت فایل‌های پروژه را اسکن می‌کند تا با معماری پروژه (مثلاً وجود مسیرهای داینامیک، نحوه تفکیک Server/Client Components و ابزارهای استایل‌دهی) همگام شود. سپس صفحه و روت مربوطه را پیاده‌سازی کرده و تست اجرای صحیح صفحه را انجام می‌دهد.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: Add /pricing as a new route with a server-component page. Pull copy from a `pricing.json` next to the page. Add a test that asserts the page renders the headlines.
[کلود کد]: Plan: create the route folder, the JSON, the page, the test.
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چرا در ساخت فیچر Next.js، پرامپت همزمان مسیر (Route)، ساختار داده و تست را در یک دستور تعیین می‌کند؟
- **الف)** برای این‌که پرامپت طولانی‌تر به نظر برسد.
- **ب)** چون دادن تمام اضلاع یک ویژگی در کنار هم، قیود کاملی به ایجنت می‌دهد تا معماری را منسجم و بدون فرضیات اشتباه بسازد.
- **ج)** چون فریم‌ورک Next.js دستورات چندبخشی را قبول نمی‌کند.
- **د)** چون در غیر این صورت ایجنت متوقف می‌شود.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>تعریف همزمان ورودی، خروجی و معیار پذیرش (تست) باعث همگرایی فوری مدل در اولین تلاش می‌شود.</p>
</details>

---

## ۲۵. رویکرد تست‌محور (Writing Tests-First in Action)

**برچسب:** `پروژه عملی 🚀` | **شناسه درس:** `cc-24-tests-first` | **زمان مطالعه:** ۹ دقیقه

> 💡 **خلاصه اجرایی:** سریع‌ترین و مطمئن‌ترین حلقه TDD که تا به حال تجربه کرده‌اید: شما مشخصات را می‌گویید؛ ایجنت تست ناموفق می‌سازد و سپس تا پاس شدن آن کد می‌زند.

### تبیین مفهومی و اصول مهندسی
مشاهده عملی چرخه ساخت ماژول محاسباتی: ابتدا تست برای مقادیر مرزی، اعداد منفی و حالت‌های نامعتبر نوشته شده و شکست می‌خورد؛ سپس پیاده‌سازی منطق بیزینس انجام شده و با فرمان تست مجدد، سبز شدن تمام سناریوها به ثبت می‌رسد.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: Build a `RateLimiter` class. New limiter accepts (maxRequests, windowMs). Each call to .check(key) returns true if under limit, false if over. Window slides. Memory only.
[کلود کد]: Tests first. Writing failing tests for: under limit, exactly at limit, over limit, window slides, distinct keys are independent.
[کلود کد]: All red. Now writing the implementation.
[کلود کد]: Green. Want me to refactor for clarity, or ship as-is?
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** دیدن شکست هر ۵ تست قبل از پیاده‌سازی کدها چه چیزی را اثبات می‌کند؟
- **الف)** اثبات می‌کند که کامپیوتر خراب است.
- **ب)** اثبات می‌کند که تست‌ها توخالی نیستند و شرایط مد نظر ما واقعاً هنوز پیاده‌سازی نشده است؛ پس وقتی بعداً سبز شوند، نشانه موفقیت قطعی است.
- **ج)** نشان می‌دهد که باید فریم‌ورک تست را عوض کنیم.
- **د)** هیچ ارزشی ندارد و وقت را تلف می‌کند.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>اثبات حساسیت تست‌ها به فقدان ویژگی، پایه و اساس اطمینان در مهندسی تست‌محور است.</p>
</details>

#### 📚 واژگان تخصصی این درس:
- **Agent:** A model wired to tools and a loop: it reads, acts, checks the result, and goes again until the task is done or you stop it.

---

## ۲۶. مهاجرت کدهای قدیمی (Migrating Legacy Code)

**برچسب:** `پروژه عملی 🚀` | **شناسه درس:** `cc-25-legacy-migration` | **زمان مطالعه:** ۹ دقیقه

> 💡 **خلاصه اجرایی:** مهاجرت‌های بزرگ معمولاً شکست می‌خورند اگر تیم بخواهد همه‌چیز را در یک تغییر ناگهانی دگرگون کند. کلود کد این کار را با ایمنی و لایه‌به‌لایه جلو می‌برد.

### تبیین مفهومی و اصول مهندسی
نمونه ارتقای ماژول‌های کدهای قدیمی (مثلاً تبدیل کدهای جاوااسکریپت قدیمی به تایپ‌اسکریپت تایپ‌شده سخت‌گیرانه): تبدیل مرحله‌به‌مرحله توابع، اضافه کردن فایل‌های d.ts، اطمینان از سازگاری کدهای بالادستی با تست‌های رگرسیون، و تثبیت کامیت‌ها پس از هر گام موفق.

### 💬 شبیه‌ساز مکالمه زنده و اجرای چرخه ایجنت (Sandbox Transcript)
```text
[کاربر]: Migrate src/utils/format.js to TypeScript. Don't touch any other file. Existing tests must still pass.
[کلود کد]: Reading the file and its tests.
```

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** قید کلیدی که مهاجرت کدهای قدیمی به روش برگ‌به‌برگ (Leaf-by-leaf) را ایمن می‌سازد چیست؟
- **الف)** حذف تمام متغیرهای سراسری.
- **ب)** تغییر ندادن اینترفیس عمومی توابع و ثابت نگه‌داشتن قرارداد ورودی-خروجی تا کدهای بالادستی دچار شکست نشوند.
- **ج)** تبدیل همزمان تمام فایل‌های ریپازیتوری در یک کامیت.
- **د)** خاموش کردن تایپ‌چکر.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>با حفظ ثبات API عمومی، قطعات داخلی ماژول‌ها بدون ایجاد اثر پروانه‌ای یا شکستن سایر بخش‌های پروژه به‌روزرسانی می‌شوند.</p>
</details>

---

## ۲۷. استقرار و ارسال به پروداکشن (Shipping to Production)

**برچسب:** `کارگاه عملی 🛠️` | **شناسه درس:** `cc-26-shipping-to-production` | **زمان مطالعه:** ۸ دقیقه

> 💡 **خلاصه اجرایی:** استقرار در محیط زنده و عملیاتی، حساس‌ترین بخش چرخه است. ایجنت در این مرحله نقش ناظر سفت‌وسخت و مجری چک‌لیست را ایفا می‌کند.

### تبیین مفهومی و اصول مهندسی
قبل از این‌که کدی وارد پروداکشن شود، از ایجنت بخواهید چک‌لیست چهارگانه را اجرا کند:
۱. اجرای تست‌ها و تایید ۱۰۰٪
۲. بررسی کامل نوع‌ها با TypeCheck
۳. بررسی خطاهای نحوی با Linter
۴. ساخت پکیج بیلد نهایی بدون اخطار.
همچنین تدوین برنامه بازگشت (Rollback Plan) پیش از دپلوی توسط ایجنت آماده می‌شود.

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Run the pre-deploy gauntlet
Tests, types, lint, build — all four green before anything touches prod.
- **روش راستی‌آزمایی:** `Either all four pass, or you get a precise failure to triage.`

#### گام 02: Inspect the migration
Have the agent read the migration that's about to run, summarize what it changes, and flag any non-reversible operations.
- **روش راستی‌آزمایی:** `You get a 1-paragraph summary plus an explicit list of irreversible ops (DROPs, NOT NULL on backfilled columns, etc.).`

#### گام 03: Draft the rollback plan
Before deploying, have the agent write the rollback steps you'll run if something breaks.
- **روش راستی‌آزمایی:** `A markdown file exists with the rollback steps before you deploy. Future you will thank present you.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** چرا برنامه بازگشت (Rollback Plan) باید «قبل» از استقرار نوشته شود نه بعد از بروز فاجعه؟
- **الف)** چون بعد از خرابی در پروداکشن، استرس بالاست و تصمیم‌گیری درست دشوار می‌شود؛ مراحل رول‌بک باید با ذهن آرام تست و آماده باشد.
- **ب)** چون گیت بعد از دپلوی اجازه پول‌بک نمی‌دهد.
- **ج)** چون سرورهای کلود به فایل بازگشت نیاز دارند تا روشن شوند.
- **د)** چون این یک قانون اداری بی‌اهمیت است.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>در هنگام حادثه در پروداکشن زمان برای فکر کردن نیست؛ چک‌لیست دقیق بازگشت باید از قبل تست و تایید شده باشد.</p>
</details>

---

## ۲۸. پروژه پایانی: ساخت و انتشار یک سایدپروژه (Capstone: Ship a Side Project)

**برچسب:** `پروژه نهایی 🏆` | **شناسه درس:** `cc-27-capstone` | **زمان مطالعه:** ۱۵ دقیقه

> 💡 **خلاصه اجرایی:** اثبات نهایی تسلط شما بر وایب کدینگ: انتخاب یک ایده واقعی و کوچک، معماری با ایجنت، ساخت در چند چرخه کوتاه و استقرار نهایی در اینترنت.

### تبیین مفهومی و اصول مهندسی
پروژه نهایی نباید یک کپی عظیم از توییتر باشد؛ یک ابزار کوچک اما واقعی انتخاب کنید که واقعاً کار کند: مثلاً یک خلاصه‌ساز متون، یک سازمان‌دهنده بوک‌مارک‌ها یا یک ماشین حساب مالی اختصاصی. با آموخته‌های ۲۷ درس گذشته، ساختار را پایه‌ریزی کنید، با گام‌های مشخصات→تست→کد پیش بروید و محصول را در یک پلتفرم مستقر کنید!

### 🛠️ کارگاه عملی و مراحل گام‌به‌گام (Hands-on Walkthrough)
#### گام 01: Pick the idea — small and real
Not a clone of Twitter. Not 'a CRM for X.' Pick one tiny tool with one user — maybe yourself. A bookmark organizer. A meeting-notes summarizer. A tip calculator with split logic. The smaller, the better.
- **روش راستی‌آزمایی:** `Your idea fits in three sentences. If it doesn't, scope down.`

#### گام 02: Set up the repo with the agent
Use Claude Code to scaffold. Pick a stack you mostly know — capstone is not the time to learn three new frameworks.
- **روش راستی‌آزمایی:** `You have a runnable app on localhost:3000.`

#### گام 03: Build the spine in 3-4 small turns
Use what you learned: spec → tests → code, small slices, mark-complete on each. Each turn ends in a runnable, testable state.
- **روش راستی‌آزمایی:** `Each turn produces a slice you could ship. If a turn produces something not-shippable, scope it smaller next time.`

#### گام 04: Deploy
Vercel, Netlify, Cloudflare Pages, Railway — pick whichever has a one-command deploy.
- **روش راستی‌آزمایی:** `There is a public URL. You can text it to a friend.`

#### گام 05: Write a 1-paragraph postmortem
The capstone isn't done until you've reflected. What did the agent do better than you expected? Where did it lose? What prompts would you reuse next time?
- **روش راستی‌آزمایی:** `POSTMORTEM.md exists, is 1-2 paragraphs, and lists at least one thing you'd do differently. You're done with the course.`

### 📝 آزمون سنجش درک مطلب و تمرین فصل
**پرسش 1:** کدام یک انتخاب «نامناسبی» برای سایدپروژه نهایی (Capstone) است؟
- **الف)** یک ابزار کوچک و واقعی که نیاز روزمره خودتان را برطرف کند.
- **ب)** تلاش برای شبیه‌سازی یک پلتفرم عظیم تجاری مانند یک CRM کامل برای بیمارستان‌ها یا کلون توییتر در اولین تجربه.
- **ج)** یک خلاصه‌ساز لینک‌های خبری.
- **د)** یک افزونه ساده برای مرتب‌سازی فایل‌ها.

<details><summary>💡 مشاهده پاسخ صحیح و تحلیل تشریحی</summary>
<p><strong>پاسخ صحیح: گزینه «ب»</strong></p>
<p>سایدپروژه باید کوچک، متمرکز و به اتمام‌رسیدنی باشد؛ ایده‌های عظیم و نامشخص در دام پیچیدگی‌ها می‌افتند و هدف یادگیری چرخه کامل را مخدوش می‌کنند.</p>
</details>

---

## ✅ جمع‌بندی فصل پنجم: پروژه‌های دنیای واقعی و استقرار
- تسلط بر مفاهیم و فرامین مطرح‌شده در این فصل پایه و اساس موفقیت شما در ادامه مسیر است.
- همواره پیش از ورود به فصل بعد، تمرینات و فرامین را در یک پروژه واقعی تست کنید.

➡️ **گام بعدی:** [رفتن به ۰۶ — چیت‌شیت جامع کلود کد](./06-cheatsheet.md)