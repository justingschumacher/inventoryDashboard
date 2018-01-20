from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class vmwareGuest(models.Model):


    vmguestid = models.IntegerField(primary_key=True)
    vm_name = models.CharField(null=True, blank=True, max_length=128)
    vmhostid = models.IntegerField()
    vmhostname = models.CharField(max_length=128)
    clid = models.IntegerField()
    clustername = models.CharField(max_length=128)
    dcid = models.IntegerField()
    dcname = models.CharField(max_length=128)
    vcid = models.IntegerField()
    vchostname = models.CharField(max_length=128)
    fid = models.IntegerField()
    mem_gb = models.IntegerField()
    disk_gb = models.IntegerField()
    cpu = models.IntegerField()
    overall_cpu_usage = models.IntegerField()
    guest_memory_usage = models.IntegerField()
    ostype = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    annotation = models.TextField()
    vlan = models.TextField()
    ip = models.CharField(max_length=128)
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
