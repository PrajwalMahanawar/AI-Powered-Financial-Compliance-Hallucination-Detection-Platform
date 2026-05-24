from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.services.benchmarking import benchmark_models
from api.services.feedback import feedback_store
from api.services.hallucination import audit_response
from api.services.rag import answer_query, retrieve_context


class RagQueryView(APIView):
    def post(self, request):
        query = request.data.get("query", "")
        model = request.data.get("model", "gpt-4.1")
        if not query:
            return Response({"detail": "query is required"}, status=status.HTTP_400_BAD_REQUEST)

        retrieved = retrieve_context(query)
        answer = answer_query(query=query, retrieved=retrieved, model=model)
        audit = audit_response(answer["response"], retrieved, request.data.get("confidence", 0.82))
        return Response({**answer, "retrieved": retrieved, "audit": audit})


class HallucinationAuditView(APIView):
    def post(self, request):
        response = request.data.get("response", "")
        context = request.data.get("context", [])
        confidence = request.data.get("confidence", 0.82)
        if not response or not context:
            return Response(
                {"detail": "response and context are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(audit_response(response, context, confidence))


class FeedbackView(APIView):
    def get(self, request):
        return Response({"items": feedback_store.items})

    def post(self, request):
        item = feedback_store.add(request.data)
        return Response(item, status=status.HTTP_201_CREATED)


class BenchmarkView(APIView):
    def get(self, request):
        return Response({"results": benchmark_models()})
