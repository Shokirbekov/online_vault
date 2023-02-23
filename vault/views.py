from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from .models import *
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        a = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        if a:
            login(request, a)
            return redirect("/vault/bolim/")
        return redirect('/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class BolimView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class MahsulotView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        data = {
            "mahsulotlar": Mahsulot.objects.filter(ombor=ombor1)
        }
        return render(request, 'products.html', data)

    def post(self, request):
        Mahsulot.objects.create(
            nom = request.POST.get('pr_name'),
            brend = request.POST.get('pr_brand'),
            narx = request.POST.get('pr_price'),
            miqdor = request.POST.get('pr_amount'),
            olchov = request.POST.get('pr_olchov'),
            kelgan_sana = request.POST.get('pr_date'),
            ombor = Ombor.objects.get(user=request.user),
        )
        return redirect("/vault/products/")

class MahsulotDelView(View):
    def get(self, request, id):
        to_be_deleted = Mahsulot.objects.get(id=id)
        if request.user.is_authenticated and Ombor.objects.get(user=request.user) == to_be_deleted.ombor:
            if to_be_deleted.ombor.user == request.user:
                to_be_deleted.delete()
            return redirect("/vault/products/")

class MahsulotUpdateView(View):
    def get(self, request, id):
        mahsulot = Mahsulot.objects.get(id=id)
        if mahsulot.ombor == Ombor.objects.get(user=request.user):
            data = {
                "product": mahsulot
            }
            return render(request, 'product_update.html', data)
        return redirect('mahsulotlar')

    def post(self, request, id):
        Mahsulot.objects.filter(id=id).update(
            narx = request.POST.get('price'),
            miqdor = request.POST.get('amount'),
        )
        return redirect("/vault/products/")

class ClientView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        soz = request.GET.get('q')
        if soz is None or soz == '':
            st = Client.objects.filter(ombor=ombor1)
        else:
            st = Client.objects.filter(ombor=ombor1, ism__contains=soz)

        data = {
            "client": st
        }
        return render(request, 'clients.html', data)

    def post(self, request):
        Client.objects.create(
            ism = request.POST.get('client_name'),
            nom = request.POST.get('client_shop'),
            manzil = request.POST.get('client_address'),
            tel = request.POST.get('client_phone'),
            qarz = request.POST.get('client_qarz'),
            ombor = Ombor.objects.get(user=request.user),
        )
        return redirect("/vault/clients/")

class ClientDelView(View):
    def get(self, request, id):
        to_be_deleted = Client.objects.get(id=id)
        if request.user.is_authenticated and Ombor.objects.get(user=request.user) == to_be_deleted.ombor:
            if to_be_deleted.ombor.user == request.user:
                to_be_deleted.delete()
            return redirect("/vault/clients/")

class ClientUpdateView(View):
    def get(self, request, id):
        client = Client.objects.get(id=id)
        if client.ombor == Ombor.objects.get(user=request.user):
            data = {
                "client": client
            }
            return render(request, 'client_update.html', data)
        return redirect('client')

    def post(self, request, id):
        Client.objects.filter(id=id).update(
            qarz = request.POST.get('client_qarz'),
            manzil = request.POST.get('client_address'),
            nom = request.POST.get('client_shop'),
            tel = request.POST.get('client_phone'),
        )
        return redirect("/vault/clients/")