from django.db import models

class HTData(models.Model):
    # identifiers
    ccode = models.CharField(max_length=50, primary_key=True)
    consno = models.CharField(max_length=50)
    cname = models.CharField(max_length=255, db_column="name")
    address = models.TextField()

    # location hierarchy
    dcode = models.CharField(max_length=50)
    dname = models.CharField(max_length=100)
    scode = models.CharField(max_length=50)
    sname = models.CharField(max_length=100)

    # billing period
    month = models.IntegerField()
    year = models.IntegerField()

    # tariff
    tariff = models.CharField(max_length=50)

    # consumption
    kwh = models.FloatField()
    kvah = models.FloatField()
    kvarh = models.FloatField()

    # financials
    net_amt = models.FloatField()
    coll_amt = models.FloatField()
    arrears = models.FloatField()

    class Meta:
        db_table = "ht_data"
        managed = False
