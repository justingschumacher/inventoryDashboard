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

    # director_image = models.ImageField()
    # slug = models.SlugField(unique=True)

    class Meta:
        managed = True
        db_table = 'django_report_core'

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'DjangoReportCore.id', (self.slug, )


class DjangoReportsDirectors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    director = models.CharField(max_length=102400, blank=True, null=True)
    total_mem_gb_used = models.BigIntegerField(blank=True, null=True)
    total_cpu_used = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_reports_directors'


class DjangoReportsSupportGroupResources(models.Model):
    id = models.BigIntegerField(primary_key=True)
    support_group = models.CharField(max_length=10240, blank=True, null=True)
    total_mem_gb_used = models.BigIntegerField(blank=True, null=True)
    total_cpu_used = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_reports_support_group_resources'


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
    guest_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpu = models.IntegerField(blank=True, null=True)
    overall_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
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
        db_table = 'vw_django_report_core'

class DjangoReportCoreDim(models.Model):
    id = models.IntegerField(primary_key=True)
    vmname = models.CharField(max_length=50)
    vmhostname = models.CharField(max_length=50)
    clustername = models.CharField(max_length=50)
    dcname = models.CharField(max_length=24)
    vchostname = models.CharField(max_length=50)
    support_group = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    decommissioned = models.CharField(max_length=10, blank=True, null=True)
    mem_gb = models.DecimalField(max_digits=65535, decimal_places=65535)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535)
    cpu = models.IntegerField()
    overall_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    guest_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ostype = models.CharField(max_length=128)
    state = models.CharField(max_length=50)
    annotation = models.CharField(max_length=1024)
    vlan = models.CharField(max_length=512)
    ip = models.CharField(max_length=255)
    prefix = models.IntegerField()
    connected = models.CharField(max_length=50)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_report_core'
