from django.db import models
from django.db.models import Count

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


class VwDjangoReportComplete(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vmguestid = models.IntegerField(blank=True, null=True)
    vm_name = models.CharField(max_length=50, blank=True, null=True)
    vmhostname = models.CharField(max_length=50, blank=True, null=True)
    clustername = models.CharField(max_length=50, blank=True, null=True)
    dcname = models.CharField(max_length=24, blank=True, null=True)
    vchostname = models.CharField(max_length=50, blank=True, null=True)
    mem_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    disk_gb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cpu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    overall_cpu_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    guest_memory_usage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ostype = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    annotation = models.CharField(max_length=1024, blank=True, null=True)
    vlan = models.CharField(max_length=512, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.IntegerField(blank=True, null=True)
    connected = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    servername = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    support_group = models.CharField(max_length=100, blank=True, null=True)
    viserver = models.CharField(db_column='VIServer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parent = models.CharField(db_column='Parent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    connection_state = models.CharField(db_column='Connection_State', max_length=128, blank=True, null=True)  # Field name made lowercase.
    powerstate = models.CharField(db_column='PowerState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    build = models.CharField(db_column='Build', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmodel = models.CharField(db_column='vModel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vserialnum = models.CharField(db_column='vSerialNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vcpu = models.CharField(db_column='vCPU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vcores = models.CharField(db_column='vCores', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vspeed = models.CharField(db_column='vSpeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmem = models.CharField(db_column='vMem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fnic = models.CharField(max_length=50, blank=True, null=True)
    enic = models.CharField(max_length=50, blank=True, null=True)
    vdspnic = models.CharField(db_column='vDSPnic', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vds = models.CharField(db_column='vDS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtdevice = models.CharField(db_column='MgtDevice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtportgroup = models.CharField(db_column='MgtPortGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtmac = models.CharField(db_column='MgtMac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtip = models.CharField(db_column='MgtIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtsubnetmask = models.CharField(db_column='MgtSubnetMask', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtgateway = models.CharField(db_column='MgtGateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgtmtu = models.CharField(db_column='MgtMtu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtdevice = models.CharField(db_column='VmtDevice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtportgroup = models.CharField(db_column='VmtPortGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtmac = models.CharField(db_column='VmtMac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtip = models.CharField(db_column='VmtIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtsubnetmask = models.CharField(db_column='VmtSubnetMask', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmtmtu = models.CharField(db_column='VmtMtu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vmswapfiledatastore = models.CharField(db_column='VmSwapfileDatastore', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ucs = models.CharField(db_column='UCS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chassis = models.CharField(db_column='Chassis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blade = models.CharField(db_column='Blade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diskcontroller = models.CharField(db_column='DiskController', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpu_0 = models.CharField(db_column='CPU', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    biosfw = models.CharField(db_column='BiosFW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mgmtfw = models.CharField(db_column='MgmtFW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adaptermodel = models.CharField(db_column='AdapterModel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adapterfw = models.CharField(db_column='AdapterFW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vnicmtu = models.CharField(db_column='vNicMTU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wwnn = models.CharField(max_length=50, blank=True, null=True)
    vhbaa = models.CharField(max_length=50, blank=True, null=True)
    vhbab = models.CharField(max_length=50, blank=True, null=True)
    lm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_django_report_complete'

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