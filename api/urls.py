from django.urls import path

from api import views

urlpatterns = [
    path("rag/query/", views.RagQueryView.as_view(), name="rag-query"),
    path("audit/hallucination/", views.HallucinationAuditView.as_view(), name="hallucination-audit"),
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    path("benchmark/", views.BenchmarkView.as_view(), name="benchmark"),
]
