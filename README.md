# FinGuard AI Compliance Platform

An enterprise-style backend and AI/ML scaffold for financial compliance, RAG analysis, hallucination detection, RLHF-style feedback, and multi-LLM benchmarking.

## What It Includes

- Synthetic banking transactions, KYC/AML policies, support conversations, SEC-style risk text, and fraud patterns.
- A lightweight RAG pipeline using tokenized cosine similarity to retrieve relevant context.
- A generated compliance explanation that cites retrieved evidence.
- Hallucination detection for unsupported claims, fabricated policy references, excessive certainty, and intent overclaims.
- RLHF-style human feedback capture with reward scoring and local preference dataset export.
- Multi-model benchmarking for accuracy, faithfulness, latency, and compliance quality.
- Reasoning audit checks for evidence traceability, confidence alignment, policy adherence, and numeric consistency.

## Backend Scaffold

The repository also includes a Django REST Framework scaffold aligned to the recommended stack:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

The base requirements intentionally install only what is needed to run the API. Install the heavier AI/ML stack separately when you are ready to wire in model training, FAISS, LangChain, MLflow, and Weights & Biases:

```bash
pip install -r requirements-ai.txt
```

For PostgreSQL support, install the optional database driver:

```bash
pip install -r requirements-postgres.txt
```

Or run the API, PostgreSQL, and MLflow services with Docker:

```bash
docker compose up --build
```

See `docs/architecture.md` for the production expansion path.

## API Endpoints

- `POST /api/rag/query/`: retrieve context, generate a compliance answer, and return audit scores.
- `POST /api/audit/hallucination/`: score an existing model output against supplied retrieved context.
- `GET /api/benchmark/`: return multi-LLM benchmark metrics.
- `GET /api/feedback/`: list captured human feedback.
- `POST /api/feedback/`: capture RLHF-style human feedback.

## Notes

The retrieval, generation, and scoring logic are intentionally transparent so the platform can be extended with LangChain, FAISS/Pinecone/Weaviate, OpenAI or local models, contradiction models, and PostgreSQL persistence.
