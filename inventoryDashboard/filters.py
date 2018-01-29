from django.contrib.auth.models import User
from .models import Vmguest
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class VmguestFilter(django_filters.FilterSet):
    class Meta:
        model = Vmguest
        fields = ['vmguestid', 'vm_name', 'vmhostid', 'vmhostname', 'clid', 'clustername', 'dcid',
                  'dcname', 'vcid', 'vchostname', 'fid', 'mem_gb', 'disk_gb', 'cpu', 'overall_cpu_usage',
                  'guest_memory_usage', 'ostype', 'state', 'annotation', 'vlan', 'ip', 'prefix',
                  'connected', 'timestamp', ]

