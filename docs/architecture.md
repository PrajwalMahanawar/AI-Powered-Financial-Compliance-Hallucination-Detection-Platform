# Architecture

## Recommended Stack Mapping

| Layer | Technology | Role |
| --- | --- | --- |
| Core AI/ML | Python, PyTorch, Hugging Face Transformers, scikit-learn, NumPy, Pandas | Model evaluation, NLI/contradiction detection, metrics, synthetic dataset processing |
| LLM/RAG | LangChain, FAISS/Pinecone, Sentence Transformers, OpenAI API/Ollama | Retrieval, vector indexing, local or hosted generation |
| Backend | Django REST Framework, PostgreSQL | API, users, feedback, audit events, benchmark runs |
| MLOps | Docker, MLflow, Weights & Biases | Experiment tracking, model comparison, reproducible services |
## Backend API Shape

- `POST /api/rag/query/`: retrieve context, generate a compliance answer, and return audit scores.
- `POST /api/audit/hallucination/`: score an existing model output against supplied retrieved context.
- `GET /api/benchmark/`: return multi-LLM benchmark metrics.
- `GET/POST /api/feedback/`: collect RLHF-style human ratings and preference pairs.

## Production Expansion Path

1. Replace the TF-IDF retriever in `api/services/rag.py` with Sentence Transformers embeddings and FAISS.
2. Add optional Pinecone or Weaviate adapters for managed vector search.
3. Swap the deterministic answer stub with LangChain chains backed by OpenAI or Ollama.
4. Extend `api/services/hallucination.py` with a Hugging Face NLI model for contradiction detection.
5. Persist feedback, audit events, benchmark runs, and vector metadata in PostgreSQL models.
6. Track benchmark experiments in MLflow and send model-quality runs to Weights & Biases.
