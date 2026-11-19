# Mobile Builder Kit — مهارات مجانية لتطوير تطبيقات الموبايل بالـAI

باكدج مفتوحة المصدر لأي حد بيطور تطبيقات Android باستخدام AI Coding Agents، خصوصا React Native وExpo.

**مش تطبيق Android أو إضافة بتشتغل لوحدها**. دي ملفات Agent Skills وRules بتتحط في أماكن بتختلف حسب الأداة اللي بتستخدمها.

## المهارات

| Skill | بتعمل إيه؟ |
| --- | --- |
| `mobile-builder-kit` | بتساعدك تمشي من الفكرة لحد إطلاق التطبيق |
| `arabic-rtl` | بتحسن وضوح العربي وبتراجع واجهات RTL |
| `app-discovery` | بتسألك عن فكرتك سؤال سؤال وتطلع مواصفات واضحة |
| `app-blueprint` | بتحول الفكرة لـMVP وMaster Prompt |
| `play-in-app-updates` | تخطيط تحديثات التطبيق الأصلية من Google Play |
| `play-in-app-review` | إضافة طلب تقييم من غير إزعاج المستخدم |
| `mobile-quality-audit` | مراجعة الأمان والأداء والاختبارات |
| `play-launch-checklist` | تجهيز التطبيق للنشر على Google Play |
| `mobile-aso-growth` | تحسين ظهور التطبيق وقياس التسويق |

**مهم:** اسم `grill-me` موجود للتوافق مع النسخة القديمة، لكن أنسب اسم للمهارة بتاعتنا `app-discovery` لأن Antigravity فيه أمر مدمج اسمه `/grill-me`.

## التثبيت

نزّل الريبو وشغل:

```bash
git clone https://github.com/Michaelz1122/mobile-builder-kit.git
cd mobile-builder-kit
python scripts/install.py --agent antigravity --target /path/to/my-app --all --dry-run
python scripts/install.py --agent antigravity --target /path/to/my-app --all
```

غير `antigravity` إلى `claude` أو `codex` أو `cursor` حسب أداة التطوير. ولو عايز كلهم استخدم `--agent all`.

**مسارات التثبيت في المشروع:**

- Antigravity: `.agents/skills/` والقواعد في `.agents/rules/`.
- Claude Code: `.claude/skills/` و`CLAUDE.md`.
- Codex: `.agents/skills/` و`AGENTS.md`.
- Cursor: `.cursor/skills/` و`.cursor/rules/*.mdc`.

للتثبيت على مستوى المستخدم بدل مشروع واحد:

```bash
python scripts/install.py --agent claude --global --all
```

السكريبت مش بيمسح إعداداتك الموجودة ولا بيستبدلها تلقائيا. استخدم `--force` فقط بعد عمل نسخة احتياطية.

## ازاي تستدعي المهارة؟

بعد التثبيت، افتح محادثة جديدة واكتب مثلا:

- `استخدم app-discovery واسألني عن فكرة التطبيق سؤال سؤال.`
- `استخدم arabic-rtl وراجع اتجاه النص العربي وشاشات التطبيق.`
- `استخدم app-blueprint وجهزلي MVP وMaster Prompt واحد.`
- `استخدم play-in-app-updates وراجع توافق التحديثات مع نسخة Expo عندي.`
- `استخدم mobile-quality-audit واكتبلي أهم مشاكل التطبيق قبل النشر.`

بعض الأدوات بتعرض المهارات بأوامر Slash أو من قائمة. ولو الأمر مش ظاهر، اطلب المهارة بالاسم.

## ملاحظات مهمة

- ملف RTL مش بيضمن إن كل موديل وكل واجهة شات هتعرض العربي صح. **مش بنفرض وسوم HTML على كل رد**؛ لأنها ممكن تظهر كنص عادي. لازم نجرب الأداة الفعلية.
- تحديثات Play الأصلية غير تحديثات Expo OTA.
- Google Play ممكن مايعرضش نافذة التقييم بسبب الحدود بتاعته.
- الـSkills مش بتثبت مميزات Native ولا بتنشر تطبيق لوحدها.
- أوامر التعديل الحساسة أو الدفع أو النشر لازم موافقة واضحة.

للتوثيق الإنجليزي بالتفصيل: [README.md](README.md). الترخيص [MIT](LICENSE).
