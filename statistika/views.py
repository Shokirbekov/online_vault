from django.shortcuts import render, redirect
from django.views import View
from vault.models import *
from .models import *

class StatistikaView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        soz = request.GET.get('q')
        if soz is None or soz == '':
            st = Statistika.objects.filter(ombor=ombor1)
        else:
            st = Statistika.objects.filter(ombor=ombor1, mahsulot__nom__contains=soz) | \
                 Statistika.objects.filter(ombor=ombor1, client__nom__contains=soz) | \
                 Statistika.objects.filter(ombor=ombor1, client__ism__contains=soz) | \
                 Statistika.objects.filter(ombor=ombor1, sana__contains=soz)
        if request.user.is_authenticated:
            data = {
                "stats": Statistika.objects.filter(ombor__user=request.user),
                'mahsulot': Mahsulot.objects.filter(ombor__user=request.user),
                'client': st,
            }
            return render(request, 'stats.html', data)
        return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            Statistika.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('pr')),
                client=Client.objects.get(id=request.POST.get('cl')),
                miqdor=request.POST.get('miqdor'),
                umumiy_summa=request.POST.get('summa'),
                tolandi=request.POST.get('tolandi'),
                nasiya=request.POST.get('nasiya'),
                ombor=Ombor.objects.get(user=request.user)
            )
            m = Mahsulot.objects.get(id=request.POST.get('pr'))
            m.miqdor = int(m.miqdor) - int(request.POST.get('miqdor'))
            m.save()
            c = Client.objects.get(id=request.POST.get('cl'))
            c.qarz = int(c.qarz) + int(request.POST.get('nasiya'))
            c.save()
            return redirect('/stats/')

class StatDelView(View):
    def get(self, request, id):
        to_be_deleted = Statistika.objects.get(id=id)
        if to_be_deleted.ombor.user == request.user:
            to_be_deleted.delete()
        return redirect('/stats/')