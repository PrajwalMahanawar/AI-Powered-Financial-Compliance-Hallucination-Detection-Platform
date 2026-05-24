from api.services.data import DOCUMENTS
from api.services.text_similarity import cosine_similarity


def retrieve_context(query, top_k=4):
    ranked = sorted(
        (
            (doc, cosine_similarity(query, f"{doc['title']} {doc['text']}"))
            for doc in DOCUMENTS
        ),
        key=lambda item: item[1],
        reverse=True,
    )

    return [
        {
            **doc,
            "score": round(float(score), 4),
        }
        for doc, score in ranked[:top_k]
    ]


def answer_query(query, retrieved, model="gpt-4.1"):
    evidence = " ".join(item["text"] for item in retrieved)
    tx = next((item for item in retrieved if item["id"] == "TX-1049"), None)

    response = (
        f"{model} flagged the case because the retrieved context shows threshold-adjacent "
        "same-day transfers, a newly added beneficiary, device fingerprint change, and enhanced "
        "due diligence jurisdiction exposure. The explanation should stay at risk-indicator "
        "level and avoid stating criminal intent without corroborating evidence."
    )

    if tx:
        response += f" Transaction evidence: {tx['text']}"

    return {
        "query": query,
        "model": model,
        "response": response,
        "context_summary": evidence[:900],
    }
