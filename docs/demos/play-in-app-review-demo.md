# Practical Demo: Google Play In-App Review with Expo & React Native

This guide demonstrates how to plan, implement, and audit Google Play in-app rating and review prompts using the `play-in-app-review` Agent Skill.

---

## 1. Overview & Best Practice Guidelines

Google Play In-App Review allows users to submit ratings and feedback directly inside your Android app without leaving to the Play Store.

### Recommended Trigger Moments
- ✅ After a positive milestone (e.g. completing a workout, saving a recipe, finishing a game level).
- ✅ After repeated productive engagement (e.g. 5th active day or 3rd successful export).

### Anti-Patterns (Strictly Avoid)
- ❌ **Never** prompt on first app open or during onboarding.
- ❌ **Never** interrupt a high-focus task (payment, checkout, account setup).
- ❌ **Never** prompt immediately following a crash or network error.
- ❌ **Never** offer rewards or incentives in exchange for ratings (violates Google Play Policy).

---

## 2. Implementation with Expo (`expo-store-review`)

Below is a robust, production-ready milestone review trigger using Expo's official `expo-store-review` package and local storage tracking:

```typescript
// reviewService.ts
import * as StoreReview from 'expo-store-review';
import AsyncStorage from '@react-native-async-storage/async-storage';

const STORAGE_KEYS = {
  ACTIONS_COUNT: '@app/milestone_count',
  LAST_PROMPT_DATE: '@app/last_review_prompt',
};

const MINIMUM_ACTIONS_BEFORE_REVIEW = 5;
const COOLDOWN_DAYS = 90; // Don't re-prompt within 90 days

export async function recordMilestoneAndPromptReview(): Promise<boolean> {
  try {
    // 1. Check if the environment supports in-app reviews
    const isSupported = await StoreReview.isAvailableAsync();
    if (!isSupported) {
      return false; // Silently exit on unsupported platforms (e.g. web/emulators without Play Store)
    }

    // 2. Check cooldown period
    const lastPromptStr = await AsyncStorage.getItem(STORAGE_KEYS.LAST_PROMPT_DATE);
    if (lastPromptStr) {
      const daysSincePrompt = (Date.now() - parseInt(lastPromptStr, 10)) / (1000 * 60 * 60 * 24);
      if (daysSincePrompt < COOLDOWN_DAYS) {
        return false;
      }
    }

    // 3. Increment milestone counter
    const currentCountStr = await AsyncStorage.getItem(STORAGE_KEYS.ACTIONS_COUNT);
    const count = (currentCountStr ? parseInt(currentCountStr, 10) : 0) + 1;
    await AsyncStorage.setItem(STORAGE_KEYS.ACTIONS_COUNT, count.toString());

    // 4. Trigger review only when target milestone is achieved
    if (count >= MINIMUM_ACTIONS_BEFORE_REVIEW) {
      await StoreReview.requestReview();

      // Record prompt timestamp and reset counter
      await AsyncStorage.setItem(STORAGE_KEYS.LAST_PROMPT_DATE, Date.now().toString());
      await AsyncStorage.setItem(STORAGE_KEYS.ACTIONS_COUNT, '0');
      return true;
    }

    return false;
  } catch (error) {
    // In-app review errors should never crash or interrupt the user experience
    console.warn('In-app review request failed silently:', error);
    return false;
  }
}
```

---

## 3. Important Google Play Quota & Platform Limitations

The `play-in-app-review` skill emphasizes several crucial facts that developers and AI coding agents often misunderstand:

1. **The Dialog is Not Guaranteed**:
   Google Play applies a strict, undisclosed internal quota. If a user recently reviewed an app or has already seen a prompt, the Google Play Core API will silently ignore the request and return success.
2. **No Feedback Callback**:
   Your app will **never know** whether the dialog was shown, whether the user submitted a 5-star review, or whether they dismissed it. The API deliberately protects user privacy.
3. **Expo Go vs Standalone / Development Build**:
   `StoreReview.isAvailableAsync()` returns `true` on Android only if the device has the Google Play Store installed and the app is running in a development build (`expo run:android`) or Play-distributed binary. It does not display real Play dialogs in Expo Go.
4. **Internal Testing Track**:
   To test the actual native UI, upload your Android App Bundle (`.aab`) to the Google Play Console **Internal Testing Track** and test with an account that has not recently submitted a review.
