from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class FeedbackStore:
    items: list[dict] = field(default_factory=list)

    def add(self, payload):
        ratings = payload.get("ratings", {})
        reward = (
            ratings.get("accuracy", 0) * 0.3
            + ratings.get("helpfulness", 0) * 0.2
            + ratings.get("safety", 0) * 0.25
            + ratings.get("compliance", 0) * 0.25
        ) / 5
        item = {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "query": payload.get("query", ""),
            "chosen_response": payload.get("chosen_response", ""),
            "rejected_response": payload.get("rejected_response", ""),
            "ratings": ratings,
            "reward": round(reward, 4),
            "reviewer_note": payload.get("reviewer_note", ""),
        }
        self.items.append(item)
        return item


feedback_store = FeedbackStore()
