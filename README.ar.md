# Mobile Builder Kit — مهارات مجانية لتطوير تطبيقات الموبايل بالـAI

**باكدج مهارات (Agent Skills) وقواعد دائمة ومفتوحة المصدر لبناء وتطوير تطبيقات Android بـ React Native و Expo بالذكاء الاصطناعي.**  
متوافقة وجاهزة للعمل فوراً مع: **Claude Code Skills** و **Google Antigravity Skills** و **OpenAI Codex Skills** و **Cursor Skills**.

[English Documentation (README.md)](README.md) · [مواصفة Agent Skills الرسمية](https://agentskills.io/specification) · [أمثلة عملية كاملة (Demos)](docs/demos/)

---

## إيه هو Mobile Builder Kit؟

**Mobile Builder Kit** عبارة عن باكدج منظمة من مهارات الذكاء الاصطناعي (**Android Agent Skills**) وقواعد التوجيه الدائمة. هدفها إنها ترشد الـ AI Coding Agents خلال كل مراحل بناء تطبيق الموبايل—بداية من مرحلة تفكيك الفكرة والمواصفات، وكتابة الـ Master Prompt، وتظبيط الـ Arabic RTL، ولحد مراجعة الجودة، وتحديثات Google Play، وإطلاق التطبيق على المتجر.

> ⭐ **اعمل Star للريبو** لو بتعمل تطبيقات موبايل بالـ AI ومحتاج توجيهات دقيقة بدون تخمين أو هلوسة من الموديل.

---

## أدوات وموديلات الذكاء الاصطناعي المدعومة

كل مهارة مكتوبة حسب مواصفة الـ [Agent Skills](https://agentskills.io/specification) القياسية (`SKILL.md`) مع ملفات التكوين الدائمة المناسبة لكل أداة:

| أداة الـ AI | مسار تثبيت الـ Skills | ملف الـ Rules الدائم | أنسب استخدام |
| :--- | :--- | :--- | :--- |
| **Claude Code** (Anthropic) | `.claude/skills/` | `CLAUDE.md` | البرمجة الذاتية عبر سطر الأوامر (Terminal) |
| **Google Antigravity** | `.agents/skills/` | `.agents/rules/` و `GEMINI.md` | بيئة التطوير المتكاملة والموديلات متعددة الوسائط |
| **OpenAI Codex / ChatGPT** | `.agents/skills/` | `AGENTS.md` | تنفيذ الميزات خطوة بخطوة بالمهام المحددة |
| **Cursor IDE** | `.cursor/skills/` | `.cursor/rules/*.mdc` | البرمجة التفاعلية داخل المحرر مع Claude و GPT-4o |

---

## المشاكل اللي بتحلها الباكدج

- **الطلبات العامة وتشتت الـ MVP (Scope Creep):** بتمنع الـ AI إنه يخمن شاشات ملهاش لازمة أو سيرفرات معقدة من خلال جلسة أسئلة محددة سؤال بسؤال.
- **مشاكل الـ Arabic RTL والـ BiDi في الموبايل:** بتضبط اتجاه النصوص، وانعكاس أزرار الرجوع، وعلامات الترقيم اللي بتتشقلب، وحقول الأرقام في تطبيقات **Arabic RTL React Native** و **Expo RTL**.
- **اللخبطة بين أنواع التحديثات:** بتوضح للموديل الفرق المعماري بين تحديثات المتجر الأصلية (**Google Play In-App Updates**) وتحديثات الـ JavaScript الهوائية (**Expo OTA Updates**).
- **أخطاء تقييم التطبيق (In-App Review):** بتساعدك تطلب التقييم في اللحظة الصح بعد إنجاز حقيقي للمستخدم، مع مراعاة القيود السرية لـ Google Play.
- **مفاجآت ما قبل النشر:** بتفحص كود التطبيق قبل الرفع لاكتشاف ثغرات الأمان، مشاكل زر الرجوع في Android، وشروط Google Play Console وسياسات الخصوصية.

---

## طرق التثبيت السريعة

اختار الطريقة اللي تناسب بيئة شغلك:

### الطريقة الأولى — الأسرع بأمر واحد (Agent Skills CLI)

لو عايز تثبت المهارات فقط مباشرة داخل أدوات الـ AI الموجودة في مشروعك عبر أداة [skills.sh](https://skills.sh):

```bash
# تثبيت كل المهارات في أدوات الـ AI المكتشفة في مشروعك
npx skills add Michaelz1122/mobile-builder-kit --all
```

لو عايز تثبت مهارة معينة (مثلاً `arabic-rtl` و `app-discovery`):
```bash
npx skills add Michaelz1122/mobile-builder-kit --skill arabic-rtl app-discovery
```

> **ملاحظة بخصوص الـ Rules الدائمة:** أمر `npx skills` بيثبت فولدرات المهارات (`SKILL.md`). لو محتاج كمان تثبت ملفات القواعد الدائمة (`AGENTS.md` و `CLAUDE.md` و `rules/arabic-rtl.md`) عشان تفضل نشطة في كل رسالة، استخدم الطريقة التانية تحت.

---

### الطريقة الثانية — التثبيت الكامل مع الـ Rules (Python Installer)

نزّل الريبو وشغل سكريبت التثبيت الآمن:

```bash
git clone https://github.com/Michaelz1122/mobile-builder-kit.git
cd mobile-builder-kit

# تجربة التثبيت بدون كتابة ملفات (Dry-run)
python scripts/install.py --agent all --target /path/to/your-app --all --dry-run

# التثبيت الكامل للمهارات والـ Rules لكل الأدوات
python scripts/install.py --agent all --target /path/to/your-app --all
```

تقدر تخصص أداة واحدة بتغيير `--agent all` لـ `antigravity` أو `claude` أو `codex` أو `cursor`.  
وللتثبيت العام على مستوى جهازك لكل المشاريع:
```bash
python scripts/install.py --agent claude --global --all
```

*السكريبت آمن ومش بيمسح أو يستبدل أي ملفات موجودة بدون كتابة `--force`.*

---

## المهارات المتاحة في الباكدج

| المهارة | الوصف | الاستخدام الأساسي |
| :--- | :--- | :--- |
| [`mobile-builder-kit`](skills/mobile-builder-kit/SKILL.md) | منسق خطة العمل الشامل | توجيه رحلة بناء التطبيق من الصفر لحد النشر |
| [`app-discovery`](skills/app-discovery/SKILL.md) | استجواب المتطلبات بذكاء | حسم متطلبات المشروع سؤال بسؤال (**الاسم المفضل** لمنع التضارب مع أمر Antigravity الداخلي) |
| [`arabic-rtl`](skills/arabic-rtl/SKILL.md) | جودة العربي واتجاه الواجهات | تحسين نصوص الشات وفحص شاشات **React Native & Expo RTL** |
| [`app-blueprint`](skills/app-blueprint/SKILL.md) | تخطيط الـ MVP والـ Master Prompt | تحويل الفكرة لمواصفات برمجية واضحة وبرومبت تنفيذي واحد |
| [`play-in-app-updates`](skills/play-in-app-updates/SKILL.md) | تحديثات Google Play الأصلية | تخطيط التحديثات المرنة والفورية (والتفرقة بينها وبين تحديثات Expo OTA) |
| [`play-in-app-review`](skills/play-in-app-review/SKILL.md) | طلب تقييم التطبيق بدون إزعاج | إضافة نافذة التقييم بعد إنجاز محدد مع مراعاة قيود المتجر |
| [`mobile-quality-audit`](skills/mobile-quality-audit/SKILL.md) | فحص الجودة والأمان | مراجعة شاملة لثغرات الأمان، التخزين المحلي، والأداء قبل النشر |
| [`play-launch-checklist`](skills/play-launch-checklist/SKILL.md) | جاهزية الإطلاق على Google Play | فحص الـ AAB، الـ targetSdk، شروط الـ 14 يوم للمطورين الجدد، ونماذج الخصوصية |
| [`mobile-aso-growth`](skills/mobile-aso-growth/SKILL.md) | تحسين ظهور التطبيق والتسويق | اختيار الكلمات المفتاحية، تحسين صفحة المتجر، وقياس الـ CPI والتحميلات |
| [`grill-me`](skills/grill-me/SKILL.md) | اسم قديم متوافق | متوفر للتوافق القديم؛ ونوصي باستخدام `app-discovery` داخل Antigravity |

---

## إزاي تستدعي أول مهارة؟

بعد التثبيت، افتح شات مع أداة الـ AI بتاعتك (Claude Code، Antigravity، Codex، أو Cursor) واطلب بالاسم:

### 1. تحديد متطلبات التطبيق
```text
استخدم app-discovery. عندي فكرة تطبيق أذكار ومتابعة عادات يومية بـ React Native.
اسألني سؤال بسؤال عشان نحدد المتطلبات وماتخمنش أي حاجة لوحدك.
```

### 2. مراجعة اتجاه النصوص وواجهات الـ RTL
```text
استخدم arabic-rtl. راجع شاشات التطبيق وحقول الإدخال واتجاه القوائم،
وأصلح أي مشكلة في علامات الترقيم أو الأرقام المتشقلبة في Expo.
```

### 3. تجهيز الـ Master Prompt للبرمجة
```text
استخدم app-blueprint. حوّل المتطلبات اللي اتفقنا عليها لمواصفات MVP،
واكتبلي Master Prompt واحد متكامل ينفذ المشروع في خطوة واحدة.
```

### 4. فحص الجودة قبل النشر
```text
استخدم mobile-quality-audit. افحص كود المشروع ودور على أي ثغرات أمنية،
أو مشاكل في زرار الرجوع، أو انهيارات ممكن تحصل لما النت يفصل.
```

---

## أمثلة عملية وشروحات تفصيلية (Demos)

تقدر تشوف كود حقيقي وشروحات خطوة بخطوة في فولدر [`docs/demos/`](docs/demos/):

- 📱 [**دليل الـ Arabic RTL في React Native و Expo**](docs/demos/arabic-rtl-demo.md) — مقارنة بين كود فيه أخطاء وكود جاهز للإنتاج مع قائمة فحص على أجهزة حقيقية.
- ⭐ [**دليل Google Play In-App Review**](docs/demos/play-in-app-review-demo.md) — كود حقيقي لحساب الإنجازات والتعامل مع حدود Google Play السرية.
- 🚀 [**دليل بناء تطبيق موبايل كامل بالـ AI من الألف للياء**](docs/demos/end-to-end-mobile-flow.md) — خطة عملية كاملة من أول الفكرة لحد متجر التطبيقات.

---

## حقائق وقيود لازم تعرفها

1. **طريقة عرض الـ Chat بتختلف حسب الأداة:** الـ Skills مش بتتحكم 100% في محرك عرض الشات؛ في واجهات الـ Webview بنستخدم `<div dir="rtl">`، لكن في سطر الأوامر (Terminal) بنمنع وسوم الـ HTML عشان التيرمينال مايتشوهش.
2. **دعم الـ RTL في التطبيق محتاج كود حقيقي:** تنسيق الشات حاجة، وتطبيق `I18nManager` والستايل المظبوط وتجربته على موبايل حقيقي حاجة تانية تماماً.
3. **تحديثات Google Play غير تحديثات Expo الهوائية:** تحديثات المتجر الأصلية بتنزل ملفات Binary كاملة (`.aab` أو `.apk`). بينما تحديثات Expo EAS بتنزل كود JavaScript فقط.
4. **نافذة التقييم مش مضمونة الظهور:** Google Play بيطبق كوتة سرية صارمة؛ لو المستخدم شاف تقييم قريب، المتجر هيتجاهل الطلب في صمت ومش هيعرض حاجة.
5. **شروط متجر Google Play:** الحسابات الشخصية الجديدة في Google Play بتتطلب اختبار مغلق لمدة 14 يوماً مع 12 مختبراً على الأقل قبل فتح النشر العام. الـ Skills بتساعدك تجهز لكن مش بتلغي شروط جوجل.

---

## الاختبارات والتحقق البرمجي

الباكدج مزودة باختبارات تلقائية وبدون أي مكتبات خارجية:

```bash
# فحص وتأكيد صحة كل ملفات الـ Skills والروابط
python scripts/validate_skills.py

# تشغيل اختبارات الـ Unit Tests للـ Installer والأدوات
python -m unittest discover -s tests -v

# تجربة التثبيت الوهمي على مشروع تجريبي
python scripts/install.py --agent all --target /tmp/test-app --all --dry-run
```

---

## عن المطور (About the Creator)

أهلاً بك! أنا **مايكل زاهي (Michael Zahy)** — مهندس ذكاء اصطناعي ومطور تطبيقات موبايل متخصص في بناء وتطوير تطبيقات الإنتاج بـ React Native و Expo بالتعاون مع أدوات الـ AI Coding Agents.

[![Website](https://img.shields.io/badge/Portfolio-michaelzahy.com-0066cc?style=flat-square&logo=google-chrome&logoColor=white)](https://michaelzahy.com?utm_source=github&utm_medium=readme&utm_campaign=mobile-builder-kit)
[![GitHub](https://img.shields.io/badge/GitHub-@Michaelz1122-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Michaelz1122)

- 💼 **متاح للاستشارات والعمل الحر (Consulting & Freelance):** لو محتاج مساعدة في بناء تطبيق MVP سريع بالذكاء الاصطناعي، أو ضبط واجهات الـ Arabic RTL المعقدة، أو تجهيز ونشر تطبيقك على Google Play.
- 🌐 **تصفح أعمالي ومشاريعي:** تقدر تتعرف على سابقة أعمالي وخدماتي وتتواصل معايا مباشرة عبر موقعي الشخصي: [michaelzahy.com](https://michaelzahy.com?utm_source=github&utm_medium=readme&utm_campaign=mobile-builder-kit).

---

## المساهمة والتوزيع

المستودع مفتوح المصدر ونرحب بالمساهمات المبنية على مصادر رسمية:
- راجع [CONTRIBUTING.md](CONTRIBUTING.md) لمعايير المساهمة وفتح الـ Pull Requests.
- راجع [PUBLISHING.md](PUBLISHING.md) لخطوات الإصدار والوسوم والنشر في أدلة الـ Skills.
- راجع [CHANGELOG.md](CHANGELOG.md) لسجل التغييرات.

**الترخيص:** [MIT License](LICENSE) © 2026 Michael Zahy.
