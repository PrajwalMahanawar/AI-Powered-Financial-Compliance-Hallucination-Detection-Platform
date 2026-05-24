import math
import re
from collections import Counter


STOP_WORDS = {
    "and",
    "are",
    "for",
    "from",
    "into",
    "that",
    "the",
    "this",
    "when",
    "with",
}


def tokenize(text):
    return [
        token
        for token in re.sub(r"[^a-zA-Z0-9\s-]", " ", text.lower()).split()
        if len(token) > 2 and token not in STOP_WORDS
    ]


def cosine_similarity(left, right):
    left_counts = Counter(tokenize(left))
    right_counts = Counter(tokenize(right))
    vocabulary = set(left_counts) | set(right_counts)
    if not vocabulary:
        return 0.0

    dot_product = sum(left_counts[token] * right_counts[token] for token in vocabulary)
    left_norm = math.sqrt(sum(value * value for value in left_counts.values()))
    right_norm = math.sqrt(sum(value * value for value in right_counts.values()))
    if not left_norm or not right_norm:
        return 0.0

    return dot_product / (left_norm * right_norm)
