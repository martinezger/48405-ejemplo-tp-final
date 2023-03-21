from django.shortcuts import render
from PedidosHoy.models import Platillo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "PedidosHoy/index.html")


class PlatilloList(ListView):
    model = Platillo
    context_object_name= "platillos"

class PlatilloMineList(LoginRequiredMixin, PlatilloList):
    
    def get_queryset(self):
        return Platillo.objects.filter(propietario=self.request.user.id).all()



class PlatilloUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Platillo
    success_url = reverse_lazy("platillo-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        platillo_id =  self.kwargs.get("pk")
        return Platillo.objects.filter(propietario=user_id, id=platillo_id).exists()


class PlatilloDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Platillo
    context_object_name= "platillo"
    success_url = reverse_lazy("platillo-list")

    def test_func(self):
        user_id = self.request.user.id
        platillo_id =  self.kwargs.get("pk")
        return Platillo.objects.filter(propietario=user_id, id=platillo_id).exists()


class PlatilloCreate(LoginRequiredMixin, CreateView):
    model = Platillo
    success_url = reverse_lazy("platillo-list")
    fields = [ 'nombre' ,'detalle', 'precio' ,'imagen']

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)



class PlatilloSearch(ListView):
    model = Platillo
    context_object_name = "platillos"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Platillo.objects.filter(nombre=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("platillo-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('platillo-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"
