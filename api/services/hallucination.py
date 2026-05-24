import re

from api.services.text_similarity import cosine_similarity


FABRICATED_RULE_PATTERN = re.compile(
    r"(AML-900|automatic account closure|100% certain|within 24 hours)",
    flags=re.IGNORECASE,
)
INTENT_OVERCLAIM_PATTERN = re.compile(
    r"(laundering money|criminal intent|committed fraud)",
    flags=re.IGNORECASE,
)


def split_sentences(text):
    return [sentence.strip() for sentence in re.split(r"[.!?]\s+", text) if len(sentence.strip()) > 20]


def semantic_support(sentence, context):
    return cosine_similarity(sentence, context)


def audit_response(response, retrieved_context, confidence=0.82):
    context = " ".join(item.get("text", "") for item in retrieved_context)
    claims = []

    for sentence in split_sentences(response):
        similarity = semantic_support(sentence, context)
        fabricated = bool(FABRICATED_RULE_PATTERN.search(sentence))
        intent_overclaim = bool(INTENT_OVERCLAIM_PATTERN.search(sentence))
        supported = similarity > 0.14 and not fabricated and not intent_overclaim
        claims.append(
            {
                "claim": sentence,
                "support": round(similarity, 4),
                "supported": supported,
                "reason": _reason(fabricated, intent_overclaim, supported),
            }
        )

    unsupported_count = len([claim for claim in claims if not claim["supported"]])
    claim_count = max(len(claims), 1)
    hallucination_rate = unsupported_count / claim_count
    groundedness = 1 - hallucination_rate
    confidence_mismatch = float(confidence) > 0.85 and hallucination_rate > 0.2

    return {
        "claims": claims,
        "hallucination_rate": round(hallucination_rate, 4),
        "faithfulness": round(max(0, groundedness - (0.15 if confidence_mismatch else 0)), 4),
        "context_groundedness": round(groundedness, 4),
        "confidence_mismatch": confidence_mismatch,
        "risk_level": "high" if hallucination_rate > 0.35 or confidence_mismatch else "medium" if hallucination_rate else "low",
    }


def _reason(fabricated, intent_overclaim, supported):
    if fabricated:
        return "Potential fabricated policy, deadline, or certainty statement."
    if intent_overclaim:
        return "Intent claim exceeds available evidence."
    if supported:
        return "Grounded in retrieved context."
    return "Weak semantic support from retrieved context."
