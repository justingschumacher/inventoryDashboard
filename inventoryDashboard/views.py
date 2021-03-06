from django.db.models import Q, Count, Avg, Sum
from django_pandas.io import read_frame
import seaborn as sb
from django.views.generic import View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import VwDjangoReportCore
import matplotlib as pl
pl.use('Agg')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

# Create your views here.


class IndexClassView(View):

    context_object_name: 'index'

    model = VwDjangoReportCore

    template_name = 'inventoryDashboard/index.html'

    success_url = reverse_lazy('index')

    fields = ('__all__')

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        high_cpu_count = VwDjangoReportCore.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = VwDjangoReportCore.objects.filter(Q(cpu__gt=4))
        high_memory_count = VwDjangoReportCore.objects.filter(Q(mem_gb__gte=8)).count()
        high_memory_guests = VwDjangoReportCore.objects.filter(Q(mem_gb__gte=8))
        guests_by_director_count = VwDjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
        guests_by_support_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                          ).annotate(VMs=Count('support_group'))
        vm_count_by_os = VwDjangoReportCore.objects.values('ostype').annotate(VMs=Count('ostype'))
        support_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                ).annotate(support_group_count=Count('support_group')
                                                                         ).count()
        director_count = VwDjangoReportCore.objects.values('director'
                                                           ).annotate(director_count=Count('director')).count()
        vm_count_all = VwDjangoReportCore.objects.values('vmname'
                                                         ).annotate(vm_count_all=Count('vmname')).count()
        director_report = VwDjangoReportCore.objects.all()

        qs = VwDjangoReportCore.objects.all()
        df = read_frame(qs, ['director', 'vmname'])

        def get_context_data(self, **kwargs):
            context = super(IndexClassView, self).get_context_data(**kwargs)
            context['DjangoReportCore'] = VwDjangoReportCore.objects.all()
            # context['DjangoReportsDirectors'] = DjangoReportsDirectors.objects.all()
            # And so on for more models
            return context

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests,
                       'high_memory_count': high_memory_count,
                       'high_memory_guests': high_memory_guests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       'support_group_count': support_group_count,
                       'director_count': director_count,
                       'vm_count_all': vm_count_all,
                       'df': df,
                       'director_report': director_report,
                       })

    def post(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        searchterm = ''
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            vmguests = vmguests.filter(Q(vmname__icontains=searchterm) |
                                       Q(vmhostname__icontains=searchterm) |
                                       Q(clustername__icontains=searchterm) |
                                       Q(dcname__icontains=searchterm) |
                                       Q(vchostname__icontains=searchterm) |
                                       Q(cpu__icontains=searchterm) |
                                       Q(ostype__icontains=searchterm) |
                                       Q(state__icontains=searchterm) |
                                       Q(connected__icontains=searchterm) |
                                       Q(director__icontains=searchterm) |
                                       Q(support_group__icontains=searchterm)
                                       )
        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'searchterm': searchterm,
                       })


class DirectorResourceSum(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/director_resource_sum.html'
    success_url = reverse_lazy('index')

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        director_counts = VwDjangoReportCore.objects.values('director'
                                                            ).annotate(cpu_counts=Sum('cpu', distinct=True),
                                                                       mem_gb_counts=Sum('mem_gb', distinct=True),
                                                                       disk_gb_counts=Sum('disk_gb', distinct=True)
                                                                       ).order_by('-cpu_counts')

        def get_context_data(self, **kwargs):
            context = super(IndexClassView, self).get_context_data(**kwargs)
            context['DjangoReportCore'] = VwDjangoReportCore.objects.all()
            # context['DjangoReportsDirectors'] = DjangoReportsDirectors.objects.all()
            # And so on for more models
            return context

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'director_counts': director_counts,
                       })


class SupportGroupResourceSum(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/support_group_resource_sum.html'
    success_url = reverse_lazy('index')

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        support_group_counts = VwDjangoReportCore.objects.values('support_group'
                                                                 ).annotate(cpu_counts=Sum('cpu', distinct=True),
                                                                            mem_gb_counts=Sum('mem_gb', distinct=True),
                                                                            disk_gb_counts=Sum('disk_gb', distinct=True)
                                                                            ).order_by('-cpu_counts')

        def get_context_data(self, **kwargs):
            context = super(IndexClassView, self).get_context_data(**kwargs)
            context['DjangoReportCore'] = VwDjangoReportCore.objects.all()
            # context['DjangoReportsDirectors'] = DjangoReportsDirectors.objects.all()
            # And so on for more models
            return context

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'support_group_counts': support_group_counts,
                       })


class DetailClassView(DetailView):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/item_detail.html'
    success_url = reverse_lazy('index')
    guests_by_director_count = VwDjangoReportCore.objects.values('director'
                                                               ).annotate(VMs=Count('director')
                                                                          ).order_by('VMs').reverse()
    guests_by_support_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                    ).annotate(VMs=Count('support_group')
                                                                               ).order_by('VMs').reverse()
    vm_count_by_os = VwDjangoReportCore.objects.values('ostype'
                                                     ).annotate(VMs=Count('ostype')
                                                                ).order_by('VMs').reverse()


class GuestsbyDirectorClassView(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/guests_by_director.html'
    success_url = reverse_lazy('index')

    def getsbs(request):
        guests_by_director_count = VwDjangoReportCore.objects.values('director'
                                                                     ).annotate(VMs=Count('director')
                                                                                ).order_by('VMs'
                                                                                           ).reverse().order_by('VMs'
                                                                                                                )[:20]
        queryset = guests_by_director_count
        df = read_frame(queryset)

        graph = sb.barplot(data=df, y='VMs', x='director', palette='gray')
        graph.set_ylabel('Virtual Machine Count')
        graph.set_xlabel('Director')
        graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
        graph.set_title('Virtual Machine Count by Director')
        graph.figure.set_size_inches(11, 8)
        response = HttpResponse(content_type="image/jpeg")
        graph.figure.savefig(response, format="png")
        return response

    def get(self, request):
        guests_by_director_count = VwDjangoReportCore.objects.values('director'
                                                                     ).annotate(VMs=Count('director')
                                                                                ).order_by('VMs').reverse()


        return render(request,
                      self.template_name,
                      {'guests_by_director_count': guests_by_director_count,
                       })


class GuestsbySupportGroupClassView(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/guests_by_support_group.html'
    success_url = reverse_lazy('index')

    def getsbs(request):
        guests_by_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                  ).annotate(VMs=Count('support_group')
                                                                             ).order_by('VMs'
                                                                                        ).reverse().order_by('VMs')[:20]
        queryset = guests_by_group_count
        df = read_frame(queryset)

        graph = sb.barplot(data=df, y='VMs', x='support_group', palette='gray')
        graph.set_ylabel('Virtual Machine Count')
        graph.set_xlabel('Service Team')
        graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
        graph.set_title('Virtual Machine Count by Support Group')
        graph.figure.set_size_inches(11, 8)
        response = HttpResponse(content_type="image/jpeg")
        graph.figure.savefig(response, format="png")
        return response

    def get(self, request):
        guests_by_support_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                          ).annotate(VMs=Count('support_group')
                                                                                     ).order_by('VMs').reverse()

        return render(request,
                      self.template_name,
                      {'guests_by_support_group_count': guests_by_support_group_count,
                       })


class OSDistributionClassView(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/os_distribution.html'
    success_url = reverse_lazy('index')
    fields = ('__all__')

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        guests_by_director_count = VwDjangoReportCore.objects.values('director'
                                                                     ).annotate(VMs=Count('director')
                                                                                ).order_by('VMs').reverse()
        guests_by_support_group_count = VwDjangoReportCore.objects.values('support_group'
                                                                          ).annotate(VMs=Count('support_group')
                                                                                     ).order_by('VMs').reverse()
        vm_count_by_os = VwDjangoReportCore.objects.values('ostype'
                                                           ).annotate(VMs=Count('ostype')
                                                                      ).order_by('VMs').reverse()

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       })


class HighCPUCountClassView(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/high_cpu_count.html'
    success_url = reverse_lazy('high_cpu_count')
    fields = ('__all__')

    def getsbs(request):
        cpu_utilization_boxplot = VwDjangoReportCore.objects.values('cpu'
                                                                    ).annotate(count=Count('fraction_cpu_usage')
                                                                               ).aggregate(avg=Avg('count'))
        df = read_frame(cpu_utilization_boxplot)

        graph = sb.boxplot(data=df, y='cpu', x='fraction_cpu_usage', palette='gray')
        graph.set_ylabel('vCPU count')
        graph.set_xlabel('Hertz Used')
        graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
        graph.set_title('CPU utilization by number of vCPUs')
        graph.figure.set_size_inches(11, 8)
        response = HttpResponse(content_type="image/jpeg")
        graph.figure.savefig(response, format="png")
        return response

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        high_cpu_count = VwDjangoReportCore.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = VwDjangoReportCore.objects.filter(Q(cpu__gt=4))
        cpu_utilization_boxplot = VwDjangoReportCore.objects.values('cpu'
                                                                    ).annotate(count=Count('fraction_cpu_usage')
                                                                            ).aggregate(avg=Avg('count'))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests,
                       'cpu_utilization_boxplot': cpu_utilization_boxplot,
                       }
                      )


class HighMemoryCountClassView(View):
    model = VwDjangoReportCore
    template_name = 'inventoryDashboard/high_mem_count.html'
    success_url = reverse_lazy('high_mem_count')
    fields = ('__all__')

    def get(self, request):
        vmguests = VwDjangoReportCore.objects.all()
        high_mem_count = VwDjangoReportCore.objects.filter(Q(mem_gb__gt=8)).count()
        high_mem_guests = VwDjangoReportCore.objects.filter(Q(mem_gb__gt=8))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_mem_count': high_mem_count,
                       'high_mem_guests': high_mem_guests})
