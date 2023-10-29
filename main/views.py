import datetime

from django.forms import ValidationError
from main.forms import ItemForm
from main.models import Item, Comment
from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse;
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .forms import SignUpForm
from django.db.models import Q
from .models import User, UserProfile
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from book.models import Book

# Akun1 -> Ikan, 1234567%
# Akun2 -> Bungres, 0000000!


#buku


def display_books(request):
    books = Book.objects.all()  # Ambil semua objek dari model Book
    return render(request, 'cobabook.html', {'books': books})

def display_books_based_name(request):
    name = request.user.username  # Ini mungkin merupakan objek yang tertunda
    # name_value = name.get()  # Ini akan mengambil nilai aktual dari objek yang tertunda
    first_letter = name[0]  # Mengambil huruf pertama dari nama
    print(first_letter)
    #first_letter = name[0]  # Mengambil huruf pertama dari nama
    books = Book.objects.filter(Q(Judul__icontains=first_letter))  # Mencari buku dengan judul yang mengandung huruf pertama nama
    return books

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'nama_aplikasi': 'Ewod Hearthstone TCG',
        'nama': request.user.username, 
        'kelas': 'PBP F', 
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_item(request, id):
    # Get item berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)


def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))


def get_item_json(request):
    item = Comment.objects.all()
    return HttpResponse(serializers.serialize('json', item))


@csrf_exempt
def add_rating_ajax(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            rating = request.POST.get("rating")
            comments = request.POST.get("description")
            new_comment = Comment(name=name, rate=rating, comments=comments)
            new_comment.save()
            return JsonResponse({"message": "Comment created successfully"}, status=201)
        except ValidationError:
            return HttpResponseBadRequest("Invalid data")
    else:
        return HttpResponseNotFound()


@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

#TAMBAHAN BARU

class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = User.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }
        return render(request, 'search.html', context)
    
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        result = display_books_based_name(request)
        context = {
            'user': user,
            'profile': profile,
            'result': result
        }

        return render(request, 'profile.html', context)
    
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'picture']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:profile', kwargs={'pk': pk})
        # return render(self.request, 'profile_edit.html', {'profile_edit_url': reverse('profile-edit', args=[10])})


    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


