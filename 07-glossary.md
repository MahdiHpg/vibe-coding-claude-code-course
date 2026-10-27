# فصل ۷ — واژه‌نامه و اصطلاح‌نامه تخصصی هوش مصنوعی و وایب کدینگ (AI Glossary)

> 📖 **مرجع:** [Vibe Code School AI Glossary](https://vibecodeschool.com/glossary)
> 🎯 **هدف:** فرهنگ تشریحی و دقیق ۸۳ اصطلاح کلیدی مهندسی هوش مصنوعی، مدل‌های زبانی بزرگ، یادگیری عمیق و ایجنت‌ها.

---

### ایجنت هوشمند (`Agent`)
سیستمی که در یک چرخه تکرار (While Loop) با اتکا به مدل زبانی، تصمیم می‌گیرد چه ابزاری را فراخوانی کند، آن را اجرا کرده، خروجی را بررسی می‌کند و تا اتمام تسک به کار خود ادامه می‌دهد.

> *English Reference:* A while loop where an LLM decides what tool to call next, executes it, sees the result, and repeats

---

### مکانیزم توجه (Attention) (`Attention`)
مکانیزمی در شبکه‌های ترنسفورمر که در آن هر توکن، مجموع وزن‌داری از مقادیر سایر توکن‌ها را بر اساس میزان ارتباط و شباهت ضرب داخلی (Dot Product) میان بردار پرس‌وجو (Query) و کلید (Key) محاسبه می‌کند.

> *English Reference:* A mechanism where every token computes a weighted sum of all other tokens' values, with weights determined by how relevant they are (via dot product of query and key vectors)

---

### هم‌راستاسازی (Alignment) (`Alignment`)
چالش فنی و اخلاقی در هوش مصنوعی برای تطبیق رفتار مدل با اهداف، ارزش‌ها، ترجیحات و نیت‌های انسانی، به ویژه در شرایط لبه‌ای پیش‌بینی‌نشده.

> *English Reference:* The technical challenge of making an AI system's behavior match human intentions, values, and preferences, including edge cases the designer didn't anticipate

---

### مدل خودبازگشتی (Autoregressive) (`Autoregressive`)
مدلی که توکن بعدی را بر اساس تمامی توکن‌های پیشین پیش‌بینی کرده و سپس آن خروجی را به عنوان ورودی گام بعد به خود تزریق می‌کند. مدل‌های GPT، LLaMA و Claude همگی خودبازگشتی هستند.

> *English Reference:* A model that predicts the next token conditioned on all previous tokens, then feeds that prediction back as input for the next step. GPT, LLaMA, and Claude are all autoregressive.

---

### تابع فعال‌ساز (`Activation Function`)
تابعی که پس از هر لایه خطی اعمال می‌شود تا خاصیت غیرخطی را به شبکه تزریق کند. بدون آن، انباشتن لایه‌های خطی به یک تبدیل خطی واحد تبدیل می‌شود. متداول‌ترین‌ها: ReLU, GELU, SiLU.

> *English Reference:* A function applied after each linear layer that introduces nonlinearity. Without it, stacking any number of linear layers collapses to a single linear transformation. ReLU, GELU, and SiLU are the most common. The choice directly affects whether gradients flow during training.

---

### بهینه‌ساز ادم (Adam) (`Adam (Optimizer)`)
الگوریتم تخمین ممان تطبیقی (Adaptive Moment Estimation) که ممان اول (Momentum) را با نرخ یادگیری تطبیقی برای هر پارامتر (ممان دوم) ترکیب می‌کند و بدون نیاز به تنظیمات پیچیده روی اکثر تسک‌ها عالی کار می‌کند.

> *English Reference:* Adaptive Moment Estimation. Combines momentum (first moment) with adaptive learning rates per parameter (second moment). Has bias correction for early steps. Works well across most tasks without much tuning.

---

### بهینه‌ساز AdamW (`AdamW`)
نگارش اصلاح‌شده Adam با تجزیه وزنی غیروابسته (Decoupled Weight Decay). در ادم سنتی منظم‌سازی L2 تحت تاثیر نرخ یادگیری تغییر می‌کرد اما AdamW تجزیه وزن را مستقیماً روی وزن‌ها اعمال می‌کند.

> *English Reference:* Adam with decoupled weight decay. In standard Adam, L2 regularization gets scaled by the adaptive learning rate per parameter, which is not what you want. AdamW applies weight decay directly to the weights, independent of the gradient statistics. The default optimizer for training transformers.

---

### سیستم گرادیان خودکار (`Autograd`)
موتور محاسباتی در پایتورچ و فریم‌ورک‌های یادگیری عمیق که عملیات روی تنسورها را در یک گراف محاسباتی ثبت کرده و در پس‌انتشار (Backward Pass) مشتقات را به صورت خودکار محاسبه می‌کند.

> *English Reference:* A system that records operations on tensors and automatically computes gradients via reverse-mode differentiation. PyTorch's autograd builds a computation graph on-the-fly (dynamic graph), while JAX uses function transformations (grad). This is what makes backpropagation practical -- you write the forward pass, and the framework computes all the derivatives.

---

### اندازه دسته (Batch Size) (`Batch Size`)
تعداد نمونه‌های آموزشی که در یک گذر رفت‌وبرگشت (Forward/Backward Pass) پردازش می‌شوند. دسته بزرگ‌تر پایداری گرادیان را افزایش داده اما حافظه VRAM بیشتری می‌طلبد.

> *English Reference:* The number of training examples processed in one forward/backward pass before updating weights. Larger batches give more stable gradient estimates but use more memory. Typical values: 32-512 for training, larger for inference. Batch size interacts with learning rate -- double the batch, double the LR (linear scaling rule).

---

### پس‌انتشار خطا (Backpropagation) (`Backpropagation`)
الگوریتم بنیادین آموزش شبکه‌های عصبی بر پایه قاعده زنجیره‌ای دیفرانسیل که نشان می‌دهد هر وزن به چه میزانی در خطای نهایی سهم داشته است.

> *English Reference:* An algorithm that computes how much each weight contributed to the error by applying the chain rule backward through the network, then adjusts weights proportionally

---

### پنجره زمینه / طول کانتکست (Context Window) (`Context Window`)
حداکثر تعداد توکن‌هایی که یک مدل زبانی می‌تواند در یک لحظه به صورت همزمان دریافت، درک و پردازش کند (شامل پرامپت، تاریخچه چت، فایل‌ها و پاسخ تولیدی).

> *English Reference:* The maximum number of tokens (input + output) that fit in a single API call. Not memory — it's a fixed-size buffer that resets every call

---

### زنجیره تفکر (CoT) (`Chain of Thought (CoT)`)
تکنیکی در پرامپت‌نویسی که مدل را وادار می‌کند مسائل پیچیده را گام‌به‌گام و مرحله‌ای استدلال کند تا احتمال خطای منطقی کاهش یابد.

> *English Reference:* A prompting technique where you ask the model to show its reasoning steps, which improves accuracy on multi-step problems because each step conditions the next token generation

---

### شبکه عصبی پیچشی (CNN) (`CNN (Convolutional Neural Network)`)
معماری پیشگام یادگیری عمیق در پردازش تصویر که با اعمال فیلترهای لغزان (Kernels) ویژگی‌های محلی مانند لبه‌ها و بافت‌ها را استخراج می‌کند.

> *English Reference:* A neural network that uses convolution operations (sliding filters over the input) to detect local patterns. Stacking convolutions detects increasingly complex features: edges, textures, objects.

---

### کودا (CUDA) (`CUDA`)
پلتفرم محاسبات موازی و رابط برنامه‌نویسی انویدیا که به نرم‌افزارها اجازه می‌دهد از قدرت پردازشی فوق‌العاده تراشه‌های گرافیکی (GPU) برای محاسبات هوش مصنوعی بهره ببرند.

> *English Reference:* NVIDIA's parallel computing platform. Lets you run matrix operations on thousands of GPU cores simultaneously. PyTorch and TensorFlow use CUDA under the hood.

---

### قطعه‌بندی اسناد (Chunking) (`Chunking`)
فرآیند خرد کردن اسناد و متون طولانی به تکه‌های کوچک‌تر و معنادار پیش از تولید بردار و ذخیره‌سازی در پایگاه‌داده‌های برداری در سیستم‌های RAG.

> *English Reference:* Breaking text into segments before embedding for retrieval. Chunk size determines the granularity of search results. Too small: loses context. Too large: dilutes relevance. Common strategies: fixed-size with overlap, sentence-based, or semantic splitting. Typical chunk size: 256-512 tokens with 10-20% overlap.

---

### یادگیری تقابلی (Contrastive Learning) (`Contrastive Learning`)
روشی از یادگیری که در آن به مدل آموزش داده می‌شود نمونه‌های مشابه را در فضای برداری به یکدیگر نزدیک و نمونه‌های نامرتبط را از هم دور نگه دارد.

> *English Reference:* Training by pulling similar pairs closer and pushing dissimilar pairs apart in embedding space. CLIP uses this: matching image-text pairs vs non-matching ones.

---

### شباهت کسینوسی (Cosine Similarity) (`Cosine Similarity`)
معیاری ریاضی برای سنجش شباهت جهت دو بردار در فضای چندبعدی بدون توجه به اندازه بردار؛ اصلی‌ترین متریک در جستجوی معنایی و پایگاه‌داده‌های برداری.

> *English Reference:* The cosine of the angle between two vectors: dot(a, b) / (||a|| * ||b||). Ranges from -1 (opposite) to 1 (identical direction). Ignores magnitude, only cares about direction. The standard similarity metric for embeddings and semantic search.

---

### انتروپی متقاطع (Cross-Entropy) (`Cross-Entropy`)
تابع خطای استاندارد برای مسائل دسته‌بندی و پیش‌بینی توکن در مدل‌های زبانی که اختلاف میان توزیع احتمال پیش‌بینی‌شده و برچسب واقعی را می‌سنجد.

> *English Reference:* Measures the difference between two probability distributions. For classification: -sum(y_true * log(y_pred)). For language models: the negative log probability of the correct next token. Lower is better. Perplexity is just exp(cross-entropy).

---

### افزودن و غنی‌سازی داده‌ها (Data Augmentation) (`Data Augmentation`)
تکنیک‌هایی برای تولید داده‌های جدید از روی داده‌های موجود (مثل چرخش تصویر یا جایگزینی کلمات هم‌معنی) برای بهبود تعمیم مدل و کاهش بیش‌برازش.

> *English Reference:* Creating modified copies of existing data (rotate images, add noise, paraphrase text) to increase training set diversity without collecting new data. Reduces overfitting.

---

### بخش رمزگشا (Decoder) (`Decoder`)
بخشی از ترنسفورمر که توکن‌ها را به ترتیب و خودبازگشتی بر مبنای بردارهای زمینه و توکن‌های قبلی تولید می‌کند.

> *English Reference:* In transformers, a decoder uses causal (masked) self-attention so each position can only attend to earlier positions. GPT is decoder-only. BERT is encoder-only. T5 is encoder-decoder.

---

### مدل‌های انتشاری (Diffusion) (`Diffusion Model`)
کلاسی از مدل‌های مولد (مثل Stable Diffusion و Midjourney) که ابتدا نویز تدریجی به داده اضافه کرده و سپس با یادگیری فرآیند حذف نویز، تصاویر یا ویدیوهای واقع‌گرایانه خلق می‌کنند.

> *English Reference:* A model trained to reverse a gradual noising process — it learns to predict and remove noise, and at generation time starts from pure noise and iteratively denoises

---

### بهینه‌سازی مستقیم ترجیحات (DPO) (`DPO (Direct Preference Optimization)`)
رویکرد مدرن در هم‌راستاسازی LLMها که بدون نیاز به آموزش یک مدل پاداش جداگانه (برخلاف RLHF سنتی)، مدل را مستقیماً روی جفت‌های مورد ترجیح انسان بهینه‌سازی می‌کند.

> *English Reference:* A training method that skips the reward model entirely — it directly optimizes the language model to prefer the better response in pairs of human preferences

---

### دراپ‌اوت (Dropout) (`Dropout`)
روش منظم‌سازی در شبکه‌های عصبی که در جریان آموزش، تعدادی از نورون‌ها را به صورت تصادفی خاموش می‌کند تا شبکه به ویژگی‌های تصادفی وابسته نشود.

> *English Reference:* During training, randomly set a fraction of activations to zero. Forces the network to not rely on any single neuron. Turned off during inference. Simple but effective regularization.

---

### مقدار ویژه (Eigenvalue) (`Eigenvalue`)
عددی در جبر خطی که نشان می‌دهد یک تبدیل خطی، بردار ویژه مربوطه را چقدر کشیده یا فشرده می‌کند؛ کلیدی در تحلیل مولفه‌های اصلی (PCA).

> *English Reference:* For a matrix A, an eigenvalue lambda satisfies Av = lambda*v for some vector v. It tells you how much the matrix scales vectors in that direction. Large eigenvalues = directions of high variance in your data.

---

### جاسازی / بردارسازی (Embedding) (`Embedding`)
تبدیل کلمات، متون، یا داده‌ها به یک بردار عددی فشرده در فضای چندبعدی پیوسته که روابط معنایی را با فواصل ریاضی حفظ می‌کند.

> *English Reference:* A learned mapping from discrete items (words, images, users) to dense vectors in continuous space, where similar items end up close together

---

### بخش رمزگذار (Encoder) (`Encoder`)
بخشی از ترنسفورمر که کل متن ورودی را به طور همزمان خوانده و آن را به مجموعه‌ای از بردارهای بازنمایی متنی غنی تبدیل می‌کند.

> *English Reference:* In transformers, an encoder uses bidirectional self-attention so each position can attend to all positions. BERT is encoder-only. Good for understanding tasks (classification, NER) but not generation.

---

### دوره آموزشی (Epoch) (`Epoch`)
یک بار عبور کامل تمامی نمونه‌های مجموعه داده آموزشی از درون الگوریتم یادگیری شبکه عصبی.

> *English Reference:* Exactly that. One complete pass through every example in the training set. Multiple epochs = seeing the data multiple times. More epochs can improve learning but risks overfitting.

---

### ویژگی (Feature) (`Feature`)
یک ویژگی قابل اندازه‌گیری یا متغیر مستقل از پدیده مورد مشاهده که به عنوان ورودی به مدل‌های هوش مصنوعی ارائه می‌شود.

> *English Reference:* An individual measurable property of the data. In classical ML, you engineer features by hand. In deep learning, the network learns features automatically from raw data.

---

### یادگیری با چند نمونه (Few-Shot) (`Few-Shot`)
رویکردی در پرامپت‌نویسی که در آن چند نمونه از جفت‌های ورودی-خروجی به مدل داده می‌شود تا فرمت و سبک پاسخ‌دهی را قبل از اجرای تسک اصلی یاد بگیرد.

> *English Reference:* Including a small number of input-output examples in the prompt before asking the model to perform a task. Typically 3-5 examples. The model pattern-matches on these examples to understand the desired format and behavior. Contrast with zero-shot (no examples) and fine-tuning (thousands of examples baked into weights).

---

### تیونینگ و تنظیم دقیق (Fine-tuning) (`Fine-tuning`)
فرآیند بازآموزی یک مدل پیش‌آموزش‌دیده روی یک دیتاست خاص و تخصصی با نرخ یادگیری پایین به منظور انطباق آن با دامنه‌ای ویژه.

> *English Reference:* Starting with a pre-trained model's weights and continuing training on a smaller, task-specific dataset. Only updates existing weights, doesn't add new knowledge from scratch

---

### فراخوانی توابع / ابزارها (Function Calling) (`Function Calling`)
قابلیت یک مدل زبانی برای تشخیص نیاز به ابزار خارجی و تولید یک خروجی ساختاریافته (مثل JSON) شامل نام تابع و آرگومان‌های لازم جهت اجرا در سرور.

> *English Reference:* A structured way for LLMs to request execution of external functions. You define tools with JSON Schema descriptions, the model outputs a structured JSON object specifying which function to call with what arguments, your code executes it, and the result goes back to the model. Not the same as agents -- function calling is the mechanism, agents are the loop.

---

### نرده‌های ایمنی / گاردرِیل (Guardrails) (`Guardrails`)
لایه‌های اعتبارسنجی و قوانین امنیتی پیش و پس از اجرای مدل زبانی برای اطمینان از عدم نقض قوانین، ایمنی داده‌ها و پاسخگویی مسئولانه.

> *English Reference:* Input/output validation layers around an LLM that detect and block harmful content, prompt injection attempts, PII leakage, or off-topic responses. Typically a pipeline: input filter -> LLM -> output filter. Can be rule-based (regex, keyword lists) or model-based (classifier that scores safety).

---

### ترنسفورمر پیش‌آموزش‌دیده مولد (GPT) (`GPT`)
معماری خانواده ترنسفورمر تنها-دیکودر (Decoder-only) توسعه‌یافته توسط OpenAI برای تولید زبان طبیعی با مقیاس وسیع.

> *English Reference:* Generative Pre-trained Transformer — a specific architecture that predicts the next token using a decoder-only transformer trained on large text corpora

---

### شبکه مولد رقابتی (GAN) (`GAN (Generative Adversarial Network)`)
معماری شامل دو شبکه رقیب: مولد (Generator) که داده‌های جعلی می‌سازد و متمایزکننده (Discriminator) که داده واقعی و جعلی را تفکیک می‌کند.

> *English Reference:* A generator network tries to create realistic data while a discriminator network tries to tell real from fake. They train together: the generator gets better at fooling the discriminator, and the discriminator gets better at detecting fakes.

---

### گرادیان (Gradient) (`Gradient`)
برداری از مشتقات جزئی که جهت و نرخ تندترین شیب صعود تابع خطا را نسبت به پارامترهای مدل مشخص می‌کند.

> *English Reference:* A vector of partial derivatives pointing in the direction of steepest increase. In ML, you go opposite to the gradient (gradient descent) to minimize the loss.

---

### گرادیان نزولی (Gradient Descent) (`Gradient Descent`)
الگوریتم پایه‌ای بهینه‌سازی که پارامترها را در خلاف جهت بردار گرادیان حرکت می‌دهد تا مقدار تابع خطا به حداقل برسد.

> *English Reference:* An optimization algorithm that adjusts parameters in the direction that reduces the loss function most steeply, like walking downhill in a high-dimensional landscape

---

### ابَرپارامتر (Hyperparameter) (`Hyperparameter`)
تنظیماتی که قبل از شروع آموزش مدل توسط مهندس مشخص می‌شوند و توسط خود مدل یاد گرفته نمی‌شوند (مثل نرخ یادگیری، اندازه دسته و تعداد لایه‌ها).

> *English Reference:* Values set before training that control the training process itself: learning rate, batch size, number of layers, dropout rate. Unlike model parameters (weights), these aren't learned from data.

---

### توهم هوش مصنوعی (Hallucination) (`Hallucination`)
پدیده‌ای که در آن مدل زبانی اطلاعاتی کاملاً نادرست، جعلی یا ساختگی را با اعتمادبه‌نفس بالا و به عنوان حقیقت بیان می‌کند.

> *English Reference:* The model generates plausible-sounding text that isn't grounded in its training data or the given context — it's pattern-completing, not fact-retrieving

---

### استنتاج / اجرا (Inference) (`Inference`)
مرحله استفاده عملیاتی از مدل آموزش‌دیده برای پاسخگویی به درخواست‌های جدید بدون به‌روزرسانی وزن‌ها.

> *English Reference:* Using a trained model to make predictions on new data. No weight updates happen. This is what you do in production: send input, get output.

---

### سوگیری استقرایی (Inductive Bias) (`Inductive Bias`)
مجموعه مفروضاتی که در معماری یک الگوریتم تعبیه شده تا برای داده‌های نادیده اولویت‌های مشخصی قائل شود (مثلاً ترجمه ناپذیری فضایی در CNN).

> *English Reference:* The assumptions built into a model's architecture. CNNs assume local patterns matter (convolution). RNNs assume order matters (sequential processing). Transformers assume everything might relate to everything (attention). The right bias helps the model learn faster from less data.

---

### کتابخانه JAX (`JAX`)
فریم‌ورک محاسبات عددی گوگل بر پایه کامپایلر XLA که امکان دیفرانسیل‌گیری خودکار، برداری‌سازی خودکار و اجرای شتاب‌یافته روی TPU/GPU را فراهم می‌آورد.

> *English Reference:* A NumPy-compatible library that adds automatic differentiation (grad), JIT compilation (jit), automatic vectorization (vmap), and multi-device parallelism (pmap). Unlike PyTorch's object-oriented style, JAX is purely functional -- no hidden state, no in-place mutation. Used by Google DeepMind for AlphaFold, Gemini, and large-scale research.

---

### حافظه پنهان کلید-مقدار (KV Cache) (`KV Cache`)
تکنیک بهینه‌سازی در استنتاج ترنسفورمرها که با ذخیره بردارهای Key و Value توکن‌های گذشته در رم، از محاسبه مجدد آن‌ها در توکن‌های بعدی جلوگیری کرده و سرعت را چند برابر می‌کند.

> *English Reference:* During autoregressive generation, caching the key and value matrices from previous tokens so you don't recompute them at each step. Trades memory for speed. Essential for fast LLM inference.

---

### فضای نهان (Latent Space) (`Latent Space`)
فضایی فشرده و کم‌بعد که در آن داده‌های پیچیده در قالب ویژگی‌های معنایی انتزاعی نمایش داده می‌شوند.

> *English Reference:* A compressed, learned representation space where similar inputs map to nearby points. Autoencoders, VAEs, and diffusion models all work in latent space. It's lower-dimensional than the input but captures the important structure.

---

### نرخ یادگیری (Learning Rate) (`Learning Rate`)
اندازه گامی که بهینه‌ساز در جهت منفی گرادیان برمی‌دارد؛ بزرگ بودن آن باعث ناپایداری و کوچک بودن آن باعث کندی شدید همگرایی می‌شود.

> *English Reference:* A scalar that controls step size during gradient descent. Too high: overshoots the minimum and diverges. Too low: converges too slowly or gets stuck. The single most important hyperparameter.

---

### مدل زبانی بزرگ (LLM) (`LLM (Large Language Model)`)
مدل‌های هوش مصنوعی با ده‌ها تا صدها میلیارد پارامتر که با تحلیل حجم‌های عظیم از متون اینترنت، توانایی درک، بازنویسی و تولید زبان و کد را به دست آورده‌اند.

> *English Reference:* A transformer-based neural network trained to predict the next token in a sequence, with billions of parameters, trained on internet-scale text data

---

### انطباق کم‌رتبه (LoRA) (`LoRA (Low-Rank Adaptation)`)
تکنیک کارآمد فاین‌تیونینگ (PEFT) که با تثبیت وزن‌های اصلی مدل و تزریق دو ماتریس کوچک کم‌رتبه، حجم حافظه مورد نیاز برای آموزش تخصصی را تا ۹۰٪ کاهش می‌دهد.

> *English Reference:* Instead of updating all weights, insert small low-rank matrices alongside the original weights. Only these small matrices are trained, reducing memory by 10-100x

---

### تابع زیان / تابع هزینه (Loss Function) (`Loss Function`)
فرمول ریاضی که میزان فاصله و خطای خروجی فعلی مدل را با نتیجه ایده‌آل و مورد انتظار اندازه‌گیری می‌کند.

> *English Reference:* A function that measures the gap between predicted and actual output. Training minimizes this function. MSE for regression, cross-entropy for classification, contrastive loss for embeddings. The choice of loss function defines what "good" means to the model.

---

### محاسبات با دقت ترکیبی (Mixed Precision) (`Mixed Precision`)
استفاده همزمان از فرمت‌های محاسباتی ۱۶ بیتی (FP16/BF16) و ۳۲ بیتی (FP32) در جریان آموزش برای صرفه‌جویی در حافظه VRAM و دوبرابر کردن سرعت آموزش.

> *English Reference:* Using float16 for forward pass and most operations (faster, less memory) but keeping float32 for gradient accumulation and weight updates (more precise). Gets 2x speedup with negligible accuracy loss.

---

### معماری ترکیبی متخصصان (MoE) (`MoE (Mixture of Experts)`)
معماری شبکه‌ای که در آن چندین زیرشبکه تخصصی (Experts) وجود دارد و یک شبکه مسیریاب (Router) برای هر توکن تنها ۱ یا ۲ متخصص فعال را انتخاب می‌کند تا بدون افزایش هزینه محاسباتی، ظرفیت مدل بالا برود.

> *English Reference:* A model with many "expert" subnetworks where a routing mechanism sends each input to only a few experts. The full model is huge but each forward pass is cheap because most experts are skipped. Mixtral popularized the open-weights version; most frontier models today are MoE under the hood.

---

### پروتکل متنی مدل (MCP) (`MCP (Model Context Protocol)`)
استاندارد باز معرفی‌شده توسط آنتروپیک برای اتصال امن، استاندارد و یکپارچه مدل‌های هوش مصنوعی و ایجنت‌ها به ابزارها، فایل‌ها، سرورها و پایگاه‌های داده.

> *English Reference:* An open protocol (JSON-RPC over stdio/HTTP) that standardizes how AI applications connect to external data sources and tools, with typed schemas for tools, resources, and prompts

---

### خطای عددی NaN (`NaN (Not a Number)`)
نمادی برای مقادیر نامعتبر ریاضی (مانند تقسیم بر صفر)؛ در آموزش شبکه‌های عصبی معمولاً نشانه انفجار گرادیان است.

> *English Reference:* A floating-point value indicating undefined results (0/0, inf-inf). In training, NaN loss usually means: learning rate too high, exploding gradients, log of zero, or division by zero. Always the first thing to check when training fails.

---

### نرمال‌سازی (Normalization) (`Normalization`)
فرآیند مقیاس‌بندی ورودی‌ها یا فعال‌سازها (مثل LayerNorm یا BatchNorm) تا میانگین و واریانس در طول لایه‌های عمیق پایدار بمانند.

> *English Reference:* Adjusting values to a standard range. Batch normalization normalizes across a batch. Layer normalization normalizes across features. Both stabilize training and allow higher learning rates.

---

### بیش‌برازش (Overfitting) (`Overfitting`)
وضعیتی که مدل جزئیات و نویزهای داده‌های آموزشی را حفظ کرده و کارایی خود را روی داده‌های جدید و نادیده از دست می‌دهد.

> *English Reference:* The model performs well on training data but poorly on unseen data. It learned the noise, not the signal. Fix with: more data, regularization (dropout, weight decay), early stopping, data augmentation, simpler model.

---

### بهینه‌ساز (Optimizer) (`Optimizer`)
الگوریتمی که فرمول به‌روزرسانی وزن‌ها را بر اساس گرادیان‌ها مدیریت می‌کند (مانند SGD, AdamW).

> *English Reference:* An algorithm that uses gradients to update model parameters. SGD is the simplest. Adam is the most common. Each optimizer has different properties: convergence speed, memory usage, sensitivity to hyperparameters.

---

### پارامتر / وزن‌های شبکه (Parameter) (`Parameter`)
متغیرهای درونی شبکه عصبی (وزن‌ها و بایاس‌ها) که در جریان آموزش به‌روز شده و دانش مدل را درون خود حمل می‌کنند.

> *English Reference:* A learnable value in the model, typically a weight or bias. "7B parameters" means 7 billion learnable numbers. Each float32 parameter takes 4 bytes, so 7B parameters = 28GB of memory just for the weights.

---

### شاخص سردرگمی (Perplexity) (`Perplexity`)
معیاری برای سنجش کیفیت مدل زبانی؛ عکس احتمال پیش‌بینی توکن‌های واقعی، به طوری که مقدار کمتر نشان‌دهنده پیش‌بینی دقیق‌تر و اطمینان بالاتر است.

> *English Reference:* The exponential of the average cross-entropy loss. Lower is better. A perplexity of 10 means the model is as uncertain as if it were choosing uniformly among 10 tokens at each step.

---

### دقت و بازخوانی (Precision & Recall) (`Precision & Recall`)
دو معیار اصلی سنجش مدل‌های دسته‌بندی؛ دقت نشان‌دهنده درستی پیش‌بینی‌های مثبت و بازخوانی نشان‌دهنده پوشش تمامی نمونه‌های مثبت واقعی است.

> *English Reference:* Precision = of items you flagged, how many were correct. Recall = of all correct items, how many did you find. They trade off: catching every spam email (high recall) means more false alarms (low precision). F1 score is their harmonic mean. Use precision when false positives are costly, recall when false negatives are costly.

---

### مهندسی پرامپت (Prompt Engineering) (`Prompt Engineering`)
دانش و هنر نگارش دستورالعمل‌ها، زمینه‌ها و مثال‌ها برای هدایت مدل زبانی به سوی خروجی دقیق، ساختاریافته و باکیفیت.

> *English Reference:* Designing the input text to reliably produce desired outputs -- including system prompts, few-shot examples, format instructions, and chain-of-thought triggers

---

### تزریق پرامپت (Prompt Injection) (`Prompt Injection`)
یک آسیب‌پذیری امنیتی که در آن ورودی‌های غیرقابل‌اعتماد کاربر یا وب، دستورات سیستمی مدل را دور زده و رفتار ایجنت را تغییر می‌دهند.

> *English Reference:* An attack where malicious text in the input overrides the system prompt or instructions. Direct injection: user types "Ignore previous instructions." Indirect injection: a retrieved document contains hidden instructions. The LLM equivalent of SQL injection. No complete solution exists -- defense is layers of input validation, output filtering, and privilege separation.

---

### کیولوآرا (QLoRA) (`QLoRA`)
تکنیک فوق‌پیشرفته فاین‌تیونینگ که مدل اصلی را با کوانتیزاسیون ۴ بیتی فشرده کرده و امکان آموزش مدل‌های بسیار بزرگ را روی کارت‌های گرافیک ارزان خانگی فراهم می‌آورد.

> *English Reference:* Quantized LoRA. Keeps the frozen base model weights in 4-bit precision (NF4 format) while training LoRA adapters in 16-bit. Reduces memory by another 3-4x compared to standard LoRA. A 7B model that needs 14GB with LoRA fits in 4-6GB with QLoRA. Quality is within 1% of full fine-tuning on most benchmarks.

---

### تولید مبتنی بر بازیابی (RAG) (`RAG (Retrieval-Augmented Generation)`)
معماری هوشمندی که پیش از پاسخگویی مدل زبانی، مرتبط‌ترین اسناد و اطلاعات را از پایگاه‌های داده بازیابی کرده و به عنوان زمینه به پرامپت مدل تزریق می‌کند.

> *English Reference:* A pattern where you retrieve relevant documents from a knowledge base (using embedding similarity), stuff them into the prompt, and let the LLM answer based on that context

---

### یادگیری تقویتی از بازخورد انسانی (RLHF) (`RLHF (Reinforcement Learning from Human Feedback)`)
فرآیند هم‌راستاسازی که در آن یک مدل پاداش بر اساس رتبه‌بندی‌های انسانی ساخته شده و مدل اصلی با الگوریتم PPO برای کسب پاداش بالاتر بهینه‌سازی می‌شود.

> *English Reference:* A training pipeline: (1) collect human preferences on model outputs, (2) train a reward model on those preferences, (3) use PPO to optimize the LLM to produce higher-reward outputs

---

### کوانتیزاسیون / فشرده‌سازی عددی (Quantization) (`Quantization`)
تبدیل وزن‌ها و فعال‌سازهای مدل از اعداد اعشاری دقیق (مثل FP32 یا FP16) به فرمت‌های کم‌بیت‌تر (مثل INT8 یا INT4) برای کاهش شدید حجم حافظه و افزایش سرعت اجرا.

> *English Reference:* Reducing the precision of model weights from float32 (4 bytes) to int8 (1 byte) or int4 (0.5 bytes). Trades a small amount of accuracy for 4-8x less memory and faster inference. GPTQ, AWQ, and GGUF are common formats.

---

### تابع ReLU (`ReLU`)
تابع فعال‌ساز یکسوساز خطی که مقادیر منفی را صفر کرده و مقادیر مثبت را بدون تغییر عبور می‌دهد؛ سریع‌ترین و متداول‌ترین تابع فعال‌ساز.

> *English Reference:* Rectified Linear Unit: f(x) = max(0, x). The simplest non-linear activation. Fast to compute, doesn't saturate for positive values. Used everywhere because it works and is cheap. Variants: LeakyReLU, GELU, SiLU.

---

### معیار ارزیابی ROUGE (`ROUGE`)
مجموعه معیارهایی برای ارزیابی خودکار سیستم‌های خلاصه‌سازی و ترجمه با مقایسه هم‌پوشانی n-gram ها با متون مرجع انسانی.

> *English Reference:* Recall-Oriented Understudy for Gisting Evaluation. Measures overlap between generated text and reference text. ROUGE-1 counts unigram matches, ROUGE-2 counts bigram matches, ROUGE-L finds the longest common subsequence. Cheap to compute but only measures surface similarity -- two sentences with the same meaning but different words score poorly.

---

### جستجوی معنایی (Semantic Search) (`Semantic Search`)
جستجو بر اساس معنی و مفهوم عبارات به جای تطابق کلمه به کلمه کلیدواژه‌ها، با استفاده از فواصل برداری در امبدینگ‌ها.

> *English Reference:* Finding documents by meaning rather than keyword matching. Embed the query and all documents into the same vector space, then return documents whose embeddings are closest to the query embedding. "payment failed" finds "transaction declined" even though they share no words. Powered by embedding models + vector databases.

---

### پخش جریانی توکن‌ها (Streaming) (`Streaming`)
ارسال تدریجی توکن‌های تولیدی مدل به محض محاسبه شدن به سمت کلاینت بدون نیاز به انتظار برای اتمام کل متن.

> *English Reference:* The LLM sends tokens as they are generated rather than waiting for the complete response. Uses Server-Sent Events (SSE) or WebSocket protocols. Reduces perceived latency from seconds to milliseconds for the first token. Essential for production chat interfaces. Each chunk contains a delta (partial token or word).

---

### توجه به خود (Self-Attention) (`Self-Attention`)
مکانیزم هسته ترنسفورمر که به هر توکن در یک جمله اجازه می‌دهد مستقیماً با تمامی توکن‌های دیگر همان جمله ارتباط برقرار کند و روابط گرامری و معنایی را دریابد.

> *English Reference:* Each token computes query, key, and value vectors. Attention weight between two tokens = dot product of their query and key, scaled and softmaxed. Output = weighted sum of value vectors. Lets every token see every other token.

---

### فاین‌تیونینگ نظارت‌شده (SFT) (`SFT (Supervised Fine-Tuning)`)
آموزش مدل روی دیتاست‌های پرسش و پاسخ یا دستورالعمل با خروجی‌های ایده‌آل دست‌چین‌شده انسانی.

> *English Reference:* Fine-tuning a pre-trained model on (instruction, response) pairs. The model learns to generate the response given the instruction. This is what turns a base model into a chat model.

---

### تابع سافت‌مکس (Softmax) (`Softmax`)
تابعی ریاضی که برداری از اعداد حقیقی را به توزیعی از احتمالات تبدیل می‌کند که مجموع آن‌ها دقیقاً برابر با ۱ است.

> *English Reference:* softmax(x_i) = exp(x_i) / sum(exp(x_j)). Transforms a vector of arbitrary real numbers into a probability distribution (all positive, sums to 1). Used in classification heads, attention weights, and anywhere you need probabilities.

---

### معماری دسته جمعی ایجنت‌ها (Swarm) (`Swarm`)
الگویی که در آن مجموعه‌ای از ایجنت‌های تخصصی و مستقل، با پیام‌رسانی و تقسیم کار بدون کنترل مرکزی بر روی یک هدف مشترک فعالیت می‌کنند.

> *English Reference:* Multiple agents sharing state and coordinating through message passing, with emergent behavior arising from simple individual rules rather than central control

---

### پرامپت سیستمی (System Prompt) (`System Prompt`)
دستورالعمل‌های بنیادین و اولیه‌ای که پیش از پیام‌های کاربر تعریف می‌شوند و شخصیت، نقش، قوانین و نحوه پاسخگویی مدل را تعیین می‌کنند.

> *English Reference:* A special message at the start of a conversation that sets the model's behavior, persona, and constraints. Processed before user messages. Not visible to the user in most UIs. Defines what the model should and shouldn't do, its tone, format preferences, and domain focus. Different from user prompts -- system prompts are set by the developer.

---

### تنسور (Tensor) (`Tensor`)
آرایه‌ای چندبعدی از اعداد که ساختار پایه‌ای داده‌ها و محاسبات در یادگیری عمیق و شبکه‌های عصبی را تشکیل می‌دهد.

> *English Reference:* The fundamental data structure in deep learning frameworks. A 0D tensor is a scalar, 1D is a vector, 2D is a matrix, 3D+ is a tensor. In PyTorch and JAX, tensors track their computation history for automatic differentiation and can live on CPU or GPU. All neural network inputs, outputs, weights, and gradients are tensors.

---

### توکن (Token) (`Token`)
کوچک‌ترین واحد متنی که مدل زبانی پردازش می‌کند؛ می‌تواند یک کاراکتر، بخشی از کلمه، یا یک کلمه کامل باشد (در انگلیسی تقریباً هر کلمه ۱.۳ توکن است).

> *English Reference:* A subword unit (typically 3-4 characters in English) produced by a tokenizer like BPE. "unbelievable" might be 3 tokens: "un" + "believ" + "able"

---

### دما / تصادفی بودن (Temperature) (`Temperature`)
پارامتری برای کنترل درجه تصادفی بودن و خلاقیت پاسخ‌های مدل؛ دمای صفر پاسخ‌های کاملاً قطعی و دمای بالا پاسخ‌های متنوع و غیرقابل‌پیش‌بینی تولید می‌کند.

> *English Reference:* A scalar that divides logits before softmax. Temperature=1 is default. Higher = flatter distribution = more random outputs. Lower = sharper distribution = more deterministic. Temperature=0 is argmax (always pick the most likely token).

---

### یادگیری انتقالی (Transfer Learning) (`Transfer Learning`)
روشی که در آن دانش کسب‌شده از یک تسک جامع (مثل خواندن اینترنت) به یک تسک خاص و جدید منتقل می‌شود.

> *English Reference:* Taking a model trained on one task and adapting it to a different task. The early layers learn general features (edges, syntax patterns) that transfer. Only the later layers need task-specific training. This is why you can fine-tune BERT for any NLP task.

---

### ترنسفورمر (Transformer) (`Transformer`)
معماری انقلابی شبکه عصبی معرفی‌شده در سال ۲۰۱۷ که با اتکا به مکانیزم Attention، ستون فقرات تمامی مدل‌های مدرن هوش مصنوعی شد.

> *English Reference:* A neural network architecture that processes sequences using self-attention (letting every position attend to every other position) instead of recurrence, enabling massive parallelization

---

### کم‌برازش (Underfitting) (`Underfitting`)
وضعیتی که مدل آن‌قدر ساده یا آموزش ناکافی است که حتی قادر به یادگیری الگوهای داده‌های آموزشی هم نیست.

> *English Reference:* The model is too simple to capture the patterns in the data. Training loss stays high. Fix with: more parameters, more layers, longer training, lower regularization, better features.

---

### خودرمزگذار متغیر (VAE) (`VAE (Variational Autoencoder)`)
مدل مولدی که داده‌ها را به یک توزیع احتمالاتی پیوسته در فضای نهان فشرده کرده و امکان تولید نمونه‌های جدید و پیوسته را می‌دهد.

> *English Reference:* An autoencoder that learns a smooth latent space by forcing the encoder output to follow a Gaussian distribution. You can sample from this distribution and decode to generate new data. The reparameterization trick makes it trainable via backpropagation.

---

### پایگاه داده برداری (Vector Database) (`Vector Database`)
دیتابیس تخصصی برای ذخیره، ایندکس و جستجوی فوق‌سریع میان میلیون‌ها بردار با الگوریتم‌های همسایگی مانند HNSW.

> *English Reference:* A database optimized for storing vectors (dense arrays of floats) and performing fast approximate nearest-neighbor search. The core operation in similarity search, RAG, and recommendation systems.

---

### وزن شبکه عصبی (Weight) (`Weight`)
ضریب‌های عددی درون لایه‌های شبکه که میزان اثرگذاری یک سیگنال ورودی بر خروجی نورون بعدی را تعیین می‌کنند.

> *English Reference:* A single number in a model's parameter matrix. A linear layer with input size 768 and output size 3072 has 768*3072 = 2,359,296 weights. Training adjusts each weight to minimize the loss function.

---

### تجزیه وزن (Weight Decay) (`Weight Decay`)
روشی برای منظم‌سازی شبکه که در جریان آموزش، جریمه‌ای متناسب با بزرگی وزن‌ها به تابع خطا اضافه می‌کند تا از رشد بی‌رویه وزن‌ها جلوگیری شود.

> *English Reference:* Adding a penalty proportional to the magnitude of weights to the loss function. Equivalent to L2 regularization. Prevents weights from growing too large. Typical value: 0.01-0.1.

---

### یادگیری بدون نمونه (Zero-Shot) (`Zero-Shot`)
توانایی مدل زبانی برای حل یک مسئله بدون نیاز به ارائه هیچ‌گونه نمونه اولیه، صرفاً بر اساس توصیف تسک در پرامپت.

> *English Reference:* Using a model on a task it wasn't explicitly trained for, with no task-specific examples in the prompt. The model generalizes from pre-training. Works because large models have seen enough variety to handle new task formats.

---

## ✅ پایان دوره و آغاز سفر وایب کدینگ
شما اکنون مجهز به تمام دانش مفهومی و ابزارهای عملی وایب کدینگ هستید. برای مرور دوباره به [README.md](./README.md) یا فایل PDF دوره مراجعه کنید.