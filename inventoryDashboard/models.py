from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class vmwareGuest(models.Model):

    vmguestid = models.IntegerField(primary_key=True)
    vm_name = models.CharField(null=True, blank=True)
    vmhostid = models.IntegerField()
    vmhostname = models.CharField()
    clid = models.IntegerField()
    clustername = models.CharField()
    dcid = models.IntegerField()
    dcname = models.CharField()
    vcid = models.IntegerField()
    vchostname = models.CharField()
    fid = models.IntegerField()
    mem_gb = models.IntegerField()
    disk_gb = models.IntegerField()
    cpu = models.IntegerField()
    overall_cpu_usage = models.IntegerField()
    guest_memory_usage = models.IntegerField()
    ostype = models.CharField()
    state = models.CharField()
    annotation = models.TextField()
    vlan = models.TextField()
    ip = models.CharField()
    prefix = models.IntegerField()
    connected = models.TextField()
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.vm_name
