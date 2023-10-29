from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from communities.models import Event
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def show_books(request):
    data = Book.objects.all()
    books = {
        'book': data
    }
    return render(request, "booklist.html", books)

from django.shortcuts import render
@login_required(login_url='/login')
def show_communities(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "communities.html", context)

def get_event_json(request):
    product_item = Event.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_event_ajax(request):
    if request.method == 'POST':
        nama_event = request.POST.get("nama_event")
        tanggal_pelaksanaan = request.POST.get("tanggal_pelaksanaan")
        harga = request.POST.get("harga")
        foto = request.POST.get("foto")

        event_baru = Event(nama_event=nama_event, tanggal_pelaksanaan=tanggal_pelaksanaan, harga=harga, foto=foto)
        event_baru.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request, id):
    product = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('communities:show_communities'))
    return HttpResponseNotFound
