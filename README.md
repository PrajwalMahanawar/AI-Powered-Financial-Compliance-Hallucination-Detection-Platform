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

## Architecture

The project is currently a backend-first AI compliance platform. It exposes REST APIs through Django REST Framework and keeps the AI logic in service modules so the retrieval, hallucination scoring, feedback, and benchmarking layers can evolve independently.

```text
Client / Postman
      |
      v
Django REST API
      |
      +--> RAG Service
      |       |
      |       +--> Synthetic policy, transaction, KYC, AML, and support data
      |       +--> Lightweight context retrieval
      |       +--> Compliance response generation
      |
      +--> Hallucination Detection Service
      |       |
      |       +--> Unsupported-claim detection
      |       +--> Fabricated-rule detection
      |       +--> Confidence mismatch scoring
      |       +--> Risk-level classification
      |
      +--> Feedback Service
      |       |
      |       +--> Human response ratings
      |       +--> Reward score calculation
      |       +--> Preference dataset foundation
      |
      +--> Benchmarking Service
              |
              +--> Model quality comparison
              +--> Accuracy, faithfulness, latency, and compliance scores
```

## Module Map

| Path | Purpose |
| --- | --- |
| `manage.py` | Django command entry point. |
| `compliance_platform/settings.py` | Django project settings. |
| `compliance_platform/urls.py` | Main URL router. |
| `api/views.py` | REST API endpoints. |
| `api/urls.py` | API route definitions. |
| `api/services/data.py` | Synthetic compliance, transaction, and benchmark data. |
| `api/services/rag.py` | Retrieval and compliance answer generation. |
| `api/services/hallucination.py` | Hallucination, groundedness, and risk scoring. |
| `api/services/feedback.py` | RLHF-style rating and reward scoring. |
| `api/services/benchmarking.py` | Multi-LLM leaderboard data. |
| `api/services/text_similarity.py` | Dependency-light cosine similarity helper. |
| `docker-compose.yml` | API, PostgreSQL, and MLflow service layout. |

## Workflow

### 1. RAG Compliance Query

Use this when an analyst wants to know why a transaction or response was flagged.

```text
User question
  -> POST /api/rag/query/
  -> retrieve matching AML/KYC/transaction context
  -> generate grounded compliance explanation
  -> audit generated answer for hallucination risk
  -> return answer, retrieved evidence, and risk metrics
```

Example:

```text
Why was transaction TX-1049 flagged for AML review?
```

The backend retrieves transaction details, AML policy rules, and support conversation evidence, then returns a compliance explanation with an audit score.

### 2. Hallucination Audit

Use this when you already have an AI-generated answer and want to check whether it is safe to trust.

```text
AI response + retrieved context
  -> POST /api/audit/hallucination/
  -> split response into claims
  -> compare each claim against context
  -> flag unsupported claims, fake rules, and excessive certainty
  -> return hallucination rate, faithfulness, groundedness, and risk level
```

### 3. Human Feedback

Use this to collect RLHF-style review data from compliance analysts.

```text
Human reviewer rating
  -> POST /api/feedback/
  -> score accuracy, helpfulness, safety, and compliance
  -> calculate reward score
  -> store preference-style feedback item
```

This becomes the foundation for future preference datasets and reward-model training.

### 4. Multi-LLM Benchmarking

Use this to compare model quality across compliance tasks.

```text
GET /api/benchmark/
  -> return model leaderboard
  -> compare accuracy, faithfulness, latency, and compliance quality
```

The current benchmark data is synthetic and can later be replaced by MLflow or Weights & Biases experiment results.

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
