from django.db import models


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


class Servicenowinfo(models.Model):
    servername = models.CharField(max_length=50, blank=True, null=True)
    decommissioned = models.CharField(max_length=10, blank=True, null=True)
    support_group = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    servicenowtimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicenowinfo'


class Vmhost(models.Model):
    vmhostid = models.IntegerField(primary_key=True)
    vmhostname = models.CharField(max_length=50)
    clid = models.IntegerField(blank=True, null=True)
    clustername = models.CharField(max_length=50)
    dcid = models.IntegerField(blank=True, null=True)
    dcname = models.CharField(max_length=24)
    vcid = models.IntegerField(blank=True, null=True)
    vchostname = models.CharField(max_length=50)
    fid = models.IntegerField(blank=True, null=True)
    hardware_cpuinfo_numcpupackages = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hardware_cpuinfo_numcpucores = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hardware_cpupkg_description = models.CharField(max_length=60, blank=True, null=True)
    hostsystemidentification_servicetag = models.CharField(max_length=50, blank=True, null=True)
    hardware_systeminfo_model = models.CharField(max_length=30, blank=True, null=True)
    hardware_systeminfo_vendor = models.CharField(max_length=30, blank=True, null=True)
    netstackinstanceruntimeinfo_vmknickeys = models.CharField(max_length=30, blank=True, null=True)
    memorysize = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capability_maxregisteredvms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capability_maxhostrunningvms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capability_maxhostsupportedvcpus = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numvms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmhost'


class Vcenter(models.Model):
    vcid = models.IntegerField()
    hostname = models.CharField(max_length=50, blank=True, null=True)
    apitype = models.CharField(max_length=15, blank=True, null=True)
    apiversion = models.CharField(max_length=8, blank=True, null=True)
    ostype = models.CharField(max_length=30, blank=True, null=True)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    build = models.CharField(max_length=10, blank=True, null=True)
    vctimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vcenter'


class Datacenter(models.Model):
    dcid = models.IntegerField()
    dcname = models.CharField(max_length=24)
    vcid = models.IntegerField(blank=True, null=True)
    vchostname = models.CharField(max_length=50)
    dctimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datacenter'


class Cluster(models.Model):
    clid = models.IntegerField()
    clustername = models.CharField(max_length=50)
    dcid = models.IntegerField(blank=True, null=True)
    dcname = models.CharField(max_length=24)
    vcid = models.IntegerField(blank=True, null=True)
    vchostname = models.CharField(max_length=50)
    fid = models.IntegerField(blank=True, null=True)
    summary_effectivecpu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_effectivememory = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_numcpucores = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_effectivecpucores = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_numeffectivehosts = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_totalcpu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_totalmemory = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    summary_usagesummary_totalvmcount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numhosts = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    clustertimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cluster'
