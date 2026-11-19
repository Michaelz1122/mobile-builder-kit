# RTL layout verification checklist

## Chat copy

- [ ] Arabic paragraph starts with Arabic text when possible.
- [ ] `React Native`, `(SDK 57)`, decimal numbers, `%`, email and domain names remain in sensible order.
- [ ] Markdown bullets and tables remain readable in the actual target app.
- [ ] No invisible bidi marks were inserted by default.
- [ ] Links are valid and code identifiers are unchanged.

## React Native / Expo UI

- [ ] Arabic text fields use suitable `writingDirection` and `textAlign`.
- [ ] Primary navigation and directional icons behave appropriately in Arabic.
- [ ] Layouts are tested at narrow and wide device sizes with dynamic font scaling.
- [ ] English text, URLs, verification codes and phone fields remain sensible in LTR.
- [ ] The selected locale doesn't unexpectedly flip content that should remain LTR.
- [ ] Alerts, modals, cards, buttons, toasts and PDFs are checked.
- [ ] Right-to-left behavior is tested on a real Android device or emulator after any required app restart.
- [ ] No user data or payment amount is misread due to bidirectional formatting.

## Optional RN implementation sketch

```tsx
import { Text } from 'react-native';

export function LocalizedLabel({ value, isArabic }: { value: string; isArabic: boolean }) {
  return (
    <Text style={{
      writingDirection: isArabic ? 'rtl' : 'ltr',
      textAlign: isArabic ? 'right' : 'left',
    }}>
      {value}
    </Text>
  );
}
```

This only sets **text** direction in one component. It does not solve navigation, row layout, dynamic localization or bidirectional PDF rendering.
