from django.shortcuts import render
from control.models import Producto
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return render(request, 'informativa/index.html')

# ------------------------------------
def producto(request):
    producto_list = Producto.objects.all()
    context = {'object_list': producto_list}
    return render(request, 'informativa/producto.html', context)

#-------------------------------------
def about(request):
    return render(request, 'informativa/about.html')
#-------------------------------------

#-------------------------------------
def contacto(request):
    return render(request, 'informativa/contacto.html')
#-------------------------------------
from django.views import generic
from informativa.forms import *
from control.models import Producto

# ------------------------------------

class ProductosListView(generic.ListView):
    model = Producto
    # paginate_by = 10
    def dispatch(self, *args, **kwargs):
        return super(ProductosListView, self).dispatch(*args, **kwargs)
        
class ProductoDetailView(generic.DetailView):
    model = Producto




from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

