# Practical Demo: Arabic RTL in React Native & Expo

This guide demonstrates how to handle Right-to-Left (RTL) layouts and mixed Arabic/English bidirectional (BiDi) text in React Native and Expo Android apps using the `arabic-rtl` Agent Skill.

---

## 1. The Common Problem

When building an Arabic or bilingual mobile application, standard LTR styling creates several critical UX defects:
1. **Punctuation flipping**: Periods, exclamation points, and parentheses jump from the end of an Arabic sentence to the right side if Latin text is mixed in.
2. **Reversed navigation**: "Back" buttons and directional chevrons point to the left instead of the right.
3. **Misaligned inputs**: Text inputs align to the left, and placeholder cursors appear on the wrong side.
4. **Mangled numbers & codes**: Phone numbers, OTP codes, and currency amounts get flipped or rendered backward.

---

## 2. Problematic Implementation (What to Avoid)

Here is a naive implementation commonly produced by AI without RTL guidance:

```tsx
// ❌ PROBLEMATIC: Assumes LTR layout and ignores BiDi text isolation
import React from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity } from 'react-native';

export function BrokenArabicProfileCard() {
  return (
    <View style={styles.card}>
      {/* Icon and title assume LTR row */}
      <View style={styles.headerRow}>
        <Text style={styles.icon}>➡️</Text>
        <Text style={styles.title}>الملف الشخصي (Profile)</Text>
      </View>

      {/* Input aligns left with hardcoded margins */}
      <TextInput
        style={styles.input}
        placeholder="أدخل رقم الهاتف: +20 100 123 4567"
      />

      {/* Trailing punctuation flips to wrong side */}
      <Text style={styles.footnote}>
        تأكد من صحة بياناتك في Expo SDK 52!
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 16, backgroundColor: '#fff', borderRadius: 8 },
  headerRow: { flexDirection: 'row', alignItems: 'center' },
  icon: { marginRight: 8 }, // Hardcoded left-to-right margin
  title: { fontSize: 18, fontWeight: 'bold' },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginTop: 12,
    textAlign: 'left', // Aligns cursor to the left for Arabic
  },
  footnote: { marginTop: 8, color: '#666', fontSize: 12 },
});
```

---

## 3. Improved Implementation (Production-Ready RTL)

Here is the corrected version using React Native's directional properties and BiDi isolation:

```tsx
// ✅ IMPROVED: Direction-aware styling, localized alignment, and isolated BiDi data
import React from 'react';
import { View, Text, TextInput, StyleSheet, I18nManager } from 'react-native';

interface ProfileCardProps {
  isArabic?: boolean;
}

export function AccessibleArabicProfileCard({ isArabic = true }: ProfileCardProps) {
  const isRTL = isArabic || I18nManager.isRTL;

  return (
    <View style={styles.card}>
      {/* Header with directional spacing */}
      <View style={[styles.headerRow, { flexDirection: isRTL ? 'row-reverse' : 'row' }]}>
        {/* Mirror directional icon only */}
        <Text style={[styles.icon, isRTL && styles.mirroredIcon]}>
          ⬅️
        </Text>
        <Text
          style={[
            styles.title,
            {
              writingDirection: isRTL ? 'rtl' : 'ltr',
              textAlign: isRTL ? 'right' : 'left',
            },
          ]}
        >
          الملف الشخصي (Profile)
        </Text>
      </View>

      {/* Form input with explicit writing direction */}
      <TextInput
        style={[
          styles.input,
          {
            writingDirection: isRTL ? 'rtl' : 'ltr',
            textAlign: isRTL ? 'right' : 'left',
          },
        ]}
        placeholder="أدخل رقم الهاتف"
        placeholderTextColor="#888"
      />

      {/* Phone number and sensitive numeric codes kept strictly LTR */}
      <Text style={[styles.phoneHelper, { writingDirection: 'ltr', textAlign: isRTL ? 'right' : 'left' }]}>
        مثال: <Text style={styles.codeSpan}>+20 100 123 4567</Text>
      </Text>

      {/* Footnote with BiDi isolation using Arabic context */}
      <Text
        style={[
          styles.footnote,
          {
            writingDirection: isRTL ? 'rtl' : 'ltr',
            textAlign: isRTL ? 'right' : 'left',
          },
        ]}
      >
        تأكد من صحة بياناتك في النسخة الحالية (Expo SDK 52)&rlm;.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 16, backgroundColor: '#ffffff', borderRadius: 8 },
  headerRow: { alignItems: 'center' },
  icon: { fontSize: 16 },
  mirroredIcon: {
    transform: [{ scaleX: -1 }], // Flip directional arrows
  },
  title: { fontSize: 18, fontWeight: 'bold', marginHorizontal: 8 },
  input: {
    borderWidth: 1,
    borderColor: '#e0e0e0',
    borderRadius: 6,
    padding: 12,
    marginTop: 12,
  },
  phoneHelper: { marginTop: 6, fontSize: 13, color: '#555' },
  codeSpan: { fontFamily: 'monospace', direction: 'ltr' },
  footnote: { marginTop: 10, color: '#666', fontSize: 12 },
});
```

---

## 4. Why This Change Matters

- **Logical Reading Flow**: Native Arabic speakers immediately feel comfortable reading right-to-left without eye strain.
- **Data Integrity**: Financial amounts, phone numbers, and OTP codes retain their mathematical order, avoiding costly input mistakes.
- **Brand Quality**: Punctuation marks stay in place instead of jumping erratically across lines.

---

## 5. Device Verification Checklist

When reviewing RTL support with `arabic-rtl` or testing on device:

- [ ] **Android System Language**: Test on an emulator or physical device set to Arabic (`ar-EG` or `ar-SA`).
- [ ] **App Restart Behavior**: React Native `I18nManager.forceRTL()` requires a full app restart to take effect.
- [ ] **Text Inputs**: Confirm cursor starts on the right, and input text doesn't unexpectedly wrap backward.
- [ ] **Numbers and Dates**: Confirm dates (e.g. `2026/11/19`) and phone numbers render without flipped tokens.
- [ ] **Navigation Stacks**: Verify back buttons mirror to point right, while media controls (play, pause, fast forward) remain unmirrored.

> **Important Limitation:** An AI coding agent's prompt instructions can guide your code architecture, but they cannot magically alter host chat UI Webviews or terminal font renderers. True RTL verification requires testing on an actual Android device or emulator.
