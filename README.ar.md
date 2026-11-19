# Mobile Builder Kit — مساعد بناء تطبيقات الموبايل بالـAI

باكدج Skills و Rules مجانية ومفتوحة المصدر متوافقة مع كافة موديلات الذكاء الاصطناعي: **Claude (Anthropic)** و **Codex / ChatGPT (OpenAI)** و **Gemini / Antigravity (Google)** لبناء تطبيقات Android بـ **React Native + Expo**.

**دي ملفات تعليمات للأدوات اللي بتدعم Agent Skills، مش تطبيق بيتثبت من Google Play.**

## دعم كافة الموديلات (Multi-Model Support)

| الموديل / الأداة | طريقة الدعم | ملف الإعدادات |
| --- | --- | --- |
| **Claude (Anthropic)** | يدعم Claude Code CLI و Claude 3.5 & 3.7 Sonnet | `CLAUDE.md` + `.agents/skills/` |
| **Codex / ChatGPT (OpenAI)** | يدعم Codex CLI و GPT-4o و Copilot | `AGENTS.md` + `.agents/skills/` |
| **Gemini (Google)** | يدعم Google Antigravity بالكامل | `GEMINI.md` + `.agents/` |
| **Cursor** | يدعم محرر Cursor مع Claude أو GPT-4o | `.cursorrules` + `.agents/skills/` |

### ذكاء التعامل مع بيئات العرض (RTL Surface Awareness)
- **في واجهات الشات والـ Webview (مثل Antigravity, Cursor, VS Code):** يتم تغليف الردود بـ `<div dir="rtl">` لضمان المحاذاة من اليمين لليسار.
- **في شاشات الطرفية و CLI (مثل Claude Code CLI و Codex Terminal):** يتم تعطيل وسوم HTML تلقائياً لمنع تشويه التيرمينال، مع الالتزام التام بسلامة علامات الترقيم (BiDi Hygiene) وبدء الفقرات بالعربي.

## الباكدج فيها إيه؟

| الـSkill | بتساعدك في إيه؟ |
| --- | --- |
| `mobile-builder-kit` | تنظيم رحلة إنشاء التطبيق من الفكرة لحد النشر. |
| `arabic-rtl` | تحسين ردود الـAI بالعربي واتجاه النصوص في التطبيق. |
| `grill-me` | أسئلة مركزة عشان نحسم قرارات المشروع قبل البرمجة. |
| `app-blueprint` | تحويل فكرتك لمتطلبات واضحة وMaster Prompt واحد. |
| `play-in-app-updates` | إضافة تحديثات التطبيق الأصلية من Google Play. |
| `play-in-app-review` | طلب تقييم التطبيق في الوقت المناسب. |
| `mobile-quality-audit` | مراجعة جودة التطبيق والأمان والتجربة والأداء. |
| `play-launch-checklist` | تجهيز Google Play واختبارات النشر والخصوصية والربح. |
| `mobile-aso-growth` | تحسين ASO ومتابعة التحميلات والحملات. |

### ملفات الـ Rules الدائمة (Always-on Rules)
بجانب الـ Skills، تحتوي الباكدج على ملف Rules جاهز (`rules/arabic-rtl.md` و `rules/AGENTS.md`). يضمن هذا الملف تطبيق قواعد الـ RTL وتغليف الردود بـ `<div dir="rtl">` تلقائياً في كل رسالة دون انتظار تفعيل المهارة حسب سياق الحديث.

## التثبيت السريع

1. نزّل ملفات الباكدج أو اعمل Clone للـRepository بعد رفعها على GitHub.
2. حط فولدرات الـSkills داخل `.agents/skills/` في مشروعك على Antigravity.
3. أو شغّل أمر التثبيت التالي من فولدر الباكدج:

```bash
python scripts/install.py --target /path/to/your-project --all
```

ولو عايز تثبتها لكل مشاريعك على جهازك:

```bash
python scripts/install.py --global --all
```

**ملاحظة:** اختيار `--global` مخصص لمسار Antigravity الافتراضي. أدوات الـAI التانية ممكن تحتاج مسار مختلف.

## أمثلة استخدام

- `استخدم grill-me واسألني عن فكرة التطبيق سؤال سؤال لحد ما نبقى متفقين على المواصفات.`
- `استخدم arabic-rtl وخلي ردودك بالمصري واتجاه النص من اليمين للشمال، وخلي المصطلحات الإنجليزي واضحة.`
- `استخدم app-blueprint وحوّل فكرتي لخطة MVP وMaster Prompt واحد لـAntigravity.`
- `راجع تطبيق Expo الحالي وأضف خطة In-App Updates وIn-App Review مناسبة للنسخة عندي.`
- `اعمل Mobile Quality Audit للتطبيق قبل ما أرفعه على Google Play.`

## حاجات لازم تعرفها

- الـSkill بتحسن تعليمات الرد العربي، لكن مش بتتحكم 100% في طريقة عرض الشات أو التزام كل موديل.
- In-App Updates الخاصة بـGoogle Play مختلفة عن تحديثات Expo OTA.
- ظهور نافذة التقييم مش مضمون، لأن Google Play عنده حدود لعدد مرات عرضها.
- أي مميزات Native لازم تتجرب على نسخة مناسبة، ومش كل حاجة بتشتغل داخل Expo Go.
- الـSkills مش هتنشر التطبيق أو تشتري خدمات أو تعدل إعدادات حساسة بدون موافقة.

## الملفات والدعم

تفاصيل كل مهارة في `skills/<skill-name>/SKILL.md`، والتجارب في `examples/prompts.md`.

راجع [README الإنجليزي](README.md) للمصادر الرسمية والتفاصيل الكاملة. الباكدج مرخصة MIT.
