/**
 * Example only. Run after a meaningful successful action, never from an explicit
 * "Rate now" button. Track `lastAttemptAt` in local storage in the actual app.
 * A successful promise DOES NOT mean the UI was displayed or a review was submitted.
 */
import * as StoreReview from 'expo-store-review';

type ReviewEligibility = {
  completedMilestones: number;
  lastAttemptAt?: number | null;
  now?: number;
};

const MIN_MILESTONES = 3;
const LOCAL_COOLDOWN_MS = 90 * 24 * 60 * 60 * 1000;

export async function maybeRequestReview({
  completedMilestones,
  lastAttemptAt,
  now = Date.now(),
}: ReviewEligibility): Promise<'requested' | 'not-eligible' | 'unavailable' | 'failed'> {
  if (completedMilestones < MIN_MILESTONES) return 'not-eligible';
  if (lastAttemptAt && now - lastAttemptAt < LOCAL_COOLDOWN_MS) return 'not-eligible';

  try {
    if (!(await StoreReview.hasAction())) return 'unavailable';
    await StoreReview.requestReview();
    // Your caller should persist this attempt timestamp regardless of dialog visibility.
    return 'requested';
  } catch {
    return 'failed';
  }
}
