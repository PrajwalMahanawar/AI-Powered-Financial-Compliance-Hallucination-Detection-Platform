from api.services.data import MODEL_BENCHMARKS


def benchmark_models():
    return sorted(MODEL_BENCHMARKS, key=lambda row: row["faithfulness"], reverse=True)
