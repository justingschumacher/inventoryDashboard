# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Q



class Vmguest(models.Model):
    vmguestid = models.IntegerField(primary_key=True)
    vm_name = models.CharField(max_length=50)
    vmhostid = models.IntegerField(blank=True, null=True)
    vmhostname = models.CharField(max_length=50)
    clid = models.IntegerField(blank=True, null=True)
    clustername = models.CharField(max_length=50)
    dcid = models.IntegerField(blank=True, null=True)
    dcname = models.CharField(max_length=24)
    vcid = models.IntegerField(blank=True, null=True)
    vchostname = models.CharField(max_length=50)
    fid = models.IntegerField(blank=True, null=True)
    mem_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    overall_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    guest_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ostype = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    annotation = models.CharField(max_length=1024, blank=True, null=True)
    vlan = models.CharField(max_length=512, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.IntegerField(blank=True, null=True)
    connected = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmguest'

    def oracle_count(self):
        ora_count = Vmguest.objects.filter(Q(ostype__icontains="Ora"))
        return ora_count
