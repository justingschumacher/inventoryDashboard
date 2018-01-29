from django.db.models import Q
from django.views.generic import View, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Vmguest

# Create your views here.


class IndexClassView(View):
    model = Vmguest

    template_name = 'inventoryDashboard/index_new.html'

    success_url = reverse_lazy('index')

    fields = ('vmguestid', 'vm_name', 'vmhostid', 'vmhostname', 'clid', 'clustername', 'dcid',
              'dcname', 'vcid', 'vchostname', 'fid', 'mem_gb', 'disk_gb', 'cpu', 'overall_cpu_usage',
              'guest_memory_usage', 'ostype', 'state', 'annotation', 'vlan', 'ip', 'prefix',
              'connected', 'timestamp', )

    # def search(self, request):
    #     vm_list = Vmguest.objects.all()
    #     vm_filter = vm_filter(request.GET, queryset=vm_list)
    #     return render(request, 'inventoryDashboard/index_new.html', {'filter': vm_filter})
    def oracle_count(self):
        ora_count = Vmguest.objects.all()
        ora_count = Vmguest.objects.filter(Q(ostype__icontains="Ora"))
        return ora_count

    def get(self, request):
        vmguests = Vmguest.objects.all()
        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests})

    def post(self, request):
        vmguests = Vmguest.objects.order_by('clustername')
        searchterm = ''
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            vmguests = vmguests.filter(Q(vm_name__icontains=searchterm) |
                                       Q(vmhostname__icontains=searchterm) |
                                       Q(clustername__icontains=searchterm) |
                                       Q(dcname__icontains=searchterm) |
                                       Q(vchostname__icontains=searchterm) |
                                       Q(cpu__exact=searchterm) |
                                       Q(ostype__icontains=searchterm) |
                                       Q(state__icontains=searchterm) |
                                       Q(connected__icontains=searchterm)
                                       )
        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'searchterm': searchterm})
    # def get(self, request):
    #     vmguests = Vmguest.objects.all()
    #     return render(request,
    #                   self.template_name,
    #                   {'Vmguests': vmguests})
    #
    # def post(self, request):
    #     projects = Project.objects.order_by('dueDate')
    #     searchterm = ''
    #     if request.POST and request.POST.get('search'):
    #         searchterm = request.POST.get('search').lower()
    #         projects = projects.filter(Q(group__icontains=searchterm) |
    #                                    Q(name__icontains=searchterm) |
    #                                    Q(projectStatus__icontains=searchterm) |
    #                                    Q(goal__icontains=searchterm) |
    #                                    Q(owner__icontains=searchterm) |
    #                                    Q(projectCompletionStatus__icontains=searchterm)
    #                                    )
    #     if request.POST and request.POST.get('filter'):
    #         filterterm = request.POST.get('filter').lower()
    #         projects = projects.filter(Q(group__icontains=filterterm) |
    #                                    Q(name__icontains=filterterm) |
    #                                    Q(projectStatus__icontains=filterterm) |
    #                                    Q(goal__icontains=filterterm) |
    #                                    Q(owner__icontains=filterterm) |
    #                                    Q(projectCompletionStatus__icontains=searchterm)
    #                                    )
    #     return render(request,
    #                   self.template_name,
    #                   {'Projects': projects,
    #                    'searchterm': searchterm})


class DetailClassView(DetailView):
    model = Vmguest

    template_name = 'inventoryDashboard/item_detail.html'

    success_url = reverse_lazy('index')
