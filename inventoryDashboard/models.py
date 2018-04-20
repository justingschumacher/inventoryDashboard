from django.db import models


class DjangoReportCore(models.Model):
    id = models.IntegerField(primary_key=True)
    vmname = models.CharField(max_length=102400)
    vmhostname = models.CharField(max_length=102400)
    clustername = models.CharField(max_length=102400)
    dcname = models.CharField(max_length=102400)
    vchostname = models.CharField(max_length=102400)
    support_group = models.CharField(max_length=102400, blank=True, null=True)
    director = models.CharField(max_length=102400, blank=True, null=True)
    decommissioned = models.CharField(max_length=102400, blank=True, null=True)
    mem_gb = models.DecimalField(max_digits=65535, decimal_places=65535)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535)
    cpu = models.IntegerField()
    overall_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    guest_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ostype = models.CharField(max_length=102400, blank=True, null=True)
    state = models.CharField(max_length=102400, blank=True, null=True)
    annotation = models.CharField(max_length=102400, blank=True, null=True)
    vlan = models.CharField(max_length=512, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=20, blank=True, null=True)
    connected = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'django_report_core'


class VwDjangoReportCore(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=False, null=False)
    vmname = models.CharField(max_length=50, blank=True, null=True)
    vmhostname = models.CharField(max_length=50, blank=True, null=True)
    clustername = models.CharField(max_length=50, blank=True, null=True)
    dcname = models.CharField(max_length=24, blank=True, null=True)
    vchostname = models.CharField(max_length=50, blank=True, null=True)
    support_group = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    decommissioned = models.CharField(max_length=10, blank=True, null=True)
    mem_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fraction_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpu = models.IntegerField(blank=True, null=True)
    fraction_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ostype = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    annotation = models.CharField(max_length=1024, blank=True, null=True)
    vlan = models.CharField(max_length=512, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.IntegerField(blank=True, null=True)
    connected = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_memory_cpu_usage_report'
