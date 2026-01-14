from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HTData

class TariffSummaryAPI(APIView):
    def get(self, request):
        qs = HTData.objects.all()

        # filters
        if "year" in request.GET:
            qs = qs.filter(year=request.GET["year"])
        if "month" in request.GET:
            qs = qs.filter(month=request.GET["month"])
        if "dcode" in request.GET:
            qs = qs.filter(dcode=request.GET["dcode"])
        if "scode" in request.GET:
            qs = qs.filter(scode=request.GET["scode"])

        data = (
            qs.values("tariff")
            .annotate(
                consumer_count=Count("ccode", distinct=True),
                total_units=Sum("kwh"),
                total_bill_amount=Sum("net_amt"),
                total_arrears=Sum("arrears"),
            )
            .order_by("-consumer_count")
        )

        return Response({"data": list(data)})

class ConsumerDrillDownAPI(APIView):
    def get(self, request):
        qs = HTData.objects.all()

        # required filter
        if "tariff" in request.GET:
    qs = qs.filter(
        tariff__istartswith=request.GET["tariff"].strip()
    )


        # optional filters  
        if "year" in request.GET:
            qs = qs.filter(year=request.GET["year"])
        if "month" in request.GET:
            qs = qs.filter(month=request.GET["month"])
        if "dcode" in request.GET:
            qs = qs.filter(dcode=request.GET["dcode"])
        if "scode" in request.GET:
            qs = qs.filter(scode=request.GET["scode"])

        data = qs.values(
            "ccode",
            "consno",
            "cname",
            "address",
            "tariff",
        ).annotate(
            total_units=Sum("kwh"),
            total_bill_amount=Sum("net_amt"),
            total_collection=Sum("coll_amt"),
            total_arrears=Sum("arrears"),
        )

        return Response({"data": list(data)})
