from django.urls import path
from .views import TariffSummaryAPI, ConsumerDrillDownAPI

urlpatterns = [
    path("tariff-summary/", TariffSummaryAPI.as_view()),
    path("consumer-drilldown/", ConsumerDrillDownAPI.as_view()),
]
