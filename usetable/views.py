

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Use
from .forms import UsetableForm
from django.core.paginator import Paginator

def index(request, num=1):
    data = Use.objects.all().order_by('date','start').reverse()
    page = Paginator(data, 5)
    params = {
            'title': 'usetable',
            'message': 'time table',
            'data': page.get_page(num),
        }
    return render(request, 'usetable/index.html' , params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Use()
        use = UsetableForm(request.POST, instance=obj)
        use.save()
        return redirect(to='/usetable')
    params = {
        'title': 'usetable',
        'form': UsetableForm(),
    }   
    return render(request, 'usetable/create.html' , params)

def edit(request, num):
    obj = Use.objects.get(id=num)
    if (request.method == 'POST'):
        use = UsetableForm(request.POST, instance=obj)
        use.save()
        return redirect(to='/usetable')
    params = {
        'title': 'usetable',
        'id' : num,
        'form': UsetableForm(instance=obj),
    }   
    return render(request, 'usetable/edit.html' , params)