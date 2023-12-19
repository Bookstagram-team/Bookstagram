import datetime
import json
from communities.models import Event
from django.forms import ValidationError
from main.forms import ItemForm, AddBookForm, PostForm
from main.models import Item, Comment, Post, Reply
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
from main.models import User, UserProfile
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from book.models import Book
from django.utils.decorators import method_decorator


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

@csrf_exempt
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

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # response = HttpResponseRedirect(reverse("main:show_main")) 
            # response.set_cookie('last_login', str(datetime.datetime.now()))
            return show_main(request)
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


def get_book_json(request):
    Book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json',Book_item ))


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            # Setelah buku ditambahkan, arahkan kembali ke halaman utama (main.html)
            return redirect('main:catalogue_page')

    form = AddBookForm()
    return render(request, 'add_book.html', {'form': form})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    data = {
        'Urutan': book.Urutan,
        'ISBN': book.ISBN,
        'Judul': book.Judul,
        'Penulis': book.Penulis,
        'Publikasi': book.Publikasi,
        'Publisher': book.Publisher,
        'ImageS': book.ImageS,
        'ImageM': book.ImageM,
        'ImageL': book.ImageL,
        'Rating': book.rating,
    }

    return render(request, 'book_detail.html', data)


@login_required(login_url='/login')
def catalogue_view(request):
    # Logika Anda untuk menyiapkan data atau melakukan operasi lainnya
    return render(request, 'catalogue.html')


def sort_book(request):
    sort_order = request.GET.get('sort', 'none')
    if sort_order == 'a_z':
        books = Book.objects.order_by('Judul')
    elif sort_order == 'z_a':
        books = Book.objects.order_by('-Judul')
    else:
        books = Book.objects.all()
    data = [{'fields': {
        'Urutan': book.Urutan,
        'ISBN': book.ISBN,
        'Judul': book.Judul,
        'Penulis': book.Penulis,
        'Publikasi': book.Publikasi,
        'Publisher': book.Publisher,
        'ImageS': book.ImageS,
        'ImageM': book.ImageM,
        'ImageL': book.ImageL,
        'Rating': book.rating,
    }} for book in books]
    return JsonResponse(data, safe=False)

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


def forum(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return render(request, "forum.html", context)

    
    context = {'form': form}
    return render(request, "forum.html", context)


class PostListView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {
            'post_list' : posts,
            'form': form, 
        }

        return render(request, 'post_list.html', context)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'post_list.html', context)

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
    
def handle_reaction(request, post_id, reaction):
    # Lakukan validasi dan logika Anda di sini
    # Misalnya, perbarui model Post dengan respons yang diberikan

    # Contoh:
    post = Post.objects.get(id=post_id)
    if reaction == 'like':
        post.likes += 1
    elif reaction == 'dislike':
        post.dislikes += 1
    post.save()

    return JsonResponse({'success': True})

@login_required(login_url='/login')
def my_view(request):
    # Ambil daftar post dari database
    post_list = Post.objects.all()

    # Di sini Anda dapat memperbarui properti likes pada setiap objek post
    for post in post_list:
        post.likes = post.like_set.count()  # contoh: menghitung jumlah like

    # Kirim post_list yang sudah diperbarui ke template
    return render(request, 'template.html', {'post_list': post_list})

@login_required(login_url='/login')
def reply_to_post(request, post_id):
    # Proses balasan disini
    # ...
    # Balas dengan JSON yang berisi data balasan
    return JsonResponse({'reply_text': 'Balasan berhasil disimpan.'})

@csrf_exempt
def add_reply_ajax(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        reply_text = request.POST.get('reply')

        # Assuming you have a model named Reply with fields 'post' and 'text'
        post = Post.objects.get(id=post_id)
        reply = Reply(post=post, text=reply_text)
        reply.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def discussion_view(request):
    # Logika Anda untuk menyiapkan data atau melakukan operasi lainnya
    return render(request, 'post_list.html')

@csrf_exempt
def create_event_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        # Ensure the user is authenticated before trying to access request.user
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=403)

        new_product = Event.objects.create(
            nama_event=data.get("nama_event", ""),
            harga=data.get("harga", 0),
            foto=data.get("foto", ""),
            tanggal_pelaksanaan=data.get("tanggal_pelaksanaan", ""),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def create_comment_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Comment.objects.create(
            name = data["name"],
            rate = int(data["rating"]),
            comments = data["comment"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
#json untuk profile - yg sedang login 
def show_profile_flutter_json_single(request):
    # Ambil data dari model UserProfile
    user_profile = UserProfile.objects.get(user=request.user)

    # Buat dictionary dengan data yang ingin Anda sertakan dalam respons JSON
    user_profile_data = {
        'name': user_profile.name,
        'bio': user_profile.bio,
        'role' : user_profile.user.role,
        #'picture': user_profile.picture.url if user_profile.picture else '',
    }

    # Kembalikan respons JSON
    return JsonResponse(user_profile_data)


@csrf_exempt
def show_profile_flutter_json_all(request):
    # Ambil semua data dari model UserProfile
    all_user_profiles = UserProfile.objects.all()

    # Buat list untuk menyimpan data dari setiap profil pengguna
    profiles_list = []

    # Iterasi melalui setiap objek UserProfile dan tambahkan data ke list
    for user_profile in all_user_profiles:
        profile_data = {
            'name': user_profile.user.username,
            'bio': user_profile.bio,
            'role_author' : user_profile.user.is_employee,
            'role_reader' : user_profile.user.is_customer,
            #'picture': user_profile.picture.url if user_profile.picture else '',
        }
        profiles_list.append(profile_data)

    # Kembalikan respons JSON dengan list dari data profil pengguna
    return JsonResponse({'user_profiles': profiles_list})

#untuk update bio
@csrf_exempt
@login_required
def update_bio(request):
    if request.method == 'POST':
        # Ambil data dari request JSON
        bio_data = json.loads(request.body.decode('utf-8'))

        # Validasi data
        if 'bio' not in bio_data:
            return JsonResponse({'status': 'error', 'message': 'Bio is required'}, status=400)

        # Dapatkan profil pengguna yang sedang login
        user_profile = UserProfile.objects.get(user=request.user)

        # Perbarui bio
        user_profile.bio = bio_data['bio']
        user_profile.save()

        # Kirim respons berhasil
        updated_profile_data = {
            'name': user_profile.user.username,
            'bio': user_profile.bio,
            # Tambahkan atribut lain sesuai kebutuhan
        }
        return JsonResponse({'status': 'success', 'user_profile': updated_profile_data})

    else:
        # Metode HTTP yang diizinkan hanya POST
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

#profile edit
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
   # fields = ['name', 'bio', 'picture']
    fields = [ 'bio']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:profile', kwargs={'pk': pk})
        # return render(self.request, 'profile_edit.html', {'profile_edit_url': reverse('profile-edit', args=[10])})


    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

def book_list(request):
    # Mendapatkan parameter sorting dari query
    sorting = request.GET.get('sort', '')

    # Mengambil semua buku dari database
    books = Book.objects.all()

    # Mengurutkan buku berdasarkan parameter sorting
    if sorting == 'az':
        books = books.order_by('title')
    elif sorting == 'za':
        books = books.order_by('-title')

    # Mengubah buku menjadi JSON dan mengirim respons
    book_list = list(books.values())
    return JsonResponse(book_list, safe=False)


def get_book_json(request):
    Book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json',Book_item ))

def get_book_details(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        book_data = serializers.serialize('json', [book])
        return JsonResponse(book_data, safe=False)

@csrf_exempt
def add_book_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_book = Book.objects.create(
            ISBN = data["isbn"],
            Judul = data["judul"],
            Penulis = data["penulis"],
            Publikasi = data["publikasi"],
            Publisher = data["publisher"],
            ImageS = data["imageS"],
            ImageM = data["imageM"],
            ImageL = data["imageL"],
            Rating = data["rating"],
            Urutan = data["urutan"],
        )

        new_book.save()

        return JsonResponse({"status": "success"}, status=201)
    else:
        return JsonResponse({"status": "error", "message": "Only POST method is allowed"}, status=405)

# fungsi view untuk halaman web
def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:catalogue_page')

    form = AddBookForm()
    return render(request, 'add_book.html', {'form': form})

def sort_az(request):
    data = Book.objects.order_by('title')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def sort_za(request):
    data = Book.objects.order_by('-title')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    data = {
        'Urutan': book.Urutan,
        'ISBN': book.ISBN,
        'Judul': book.Judul,
        'Penulis': book.Penulis,
        'Publikasi': book.Publikasi,
        'Publisher': book.Publisher,
        'ImageS': book.ImageS,
        'ImageM': book.ImageM,
        'ImageL': book.ImageL,
        'Rating': book.Rating,
    }

    return render(request, 'book_detail.html', data)


@login_required(login_url='/login')
def catalogue_view(request):
    # Logika Anda untuk menyiapkan data atau melakukan operasi lainnya
    return render(request, 'catalogue.html')

# nambahin ini
@csrf_exempt
def show_books_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/show-json")

@csrf_exempt
def get_books_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def sort_book(request):
    sort_order = request.GET.get('sort', 'none')
    if sort_order == 'a_z':
        books = Book.objects.order_by('Judul')
    elif sort_order == 'z_a':
        books = Book.objects.order_by('-Judul')
    else:
        books = Book.objects.all()
    data = [{'fields': {
        'Urutan': book.Urutan,
        'ISBN': book.ISBN,
        'Judul': book.Judul,
        'Penulis': book.Penulis,
        'Publikasi': book.Publikasi,
        'Publisher': book.Publisher,
        'ImageS': book.ImageS,
        'ImageM': book.ImageM,
        'ImageL': book.ImageL,
        'Rating': book.rating,
    }} for book in books]
    return JsonResponse(data, safe=False)

def show_json_posts(request):
    posts = Post.objects.all().order_by('-created_on')
    post_data = [
        {
            'id': post.id,
            'author': post.author,
            'title': post.title, 
            'content': post.body,  # Update to use 'body'
            'created_on': post.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for post in posts
    ]
    return JsonResponse({'post_list': post_data}, safe=False)

def show_xml_posts(request):
    posts = Post.objects.all().order_by('-created_on')
    data = serialize_posts(posts)
    return HttpResponse(data, content_type="application/xml")


def serialize_posts(posts):
    post_data = [
        {
            'id': post.id,
            'author': post.author.username,
            'title': post.title, 
            'content': post.body,  # Update to use 'body'
            'created_on': post.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for post in posts
    ]
    return serializers.serialize("json", post_data)

def show_xml_by_id(request, id):
    post = Post.objects.get(pk=id)
    data = {
        'id': post.id,
        'author': post.author.username,
        'title': post.title,
        'content': post.body,
        'created_on': post.created_on.strftime('%Y-%m-%d %H:%M:%S'),
    }
    xml_data = serializers.serialize("xml", [data])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    post = Post.objects.get(pk=id)
    data = {
        'id': post.id,
        'author': post.author.username,
        'title': post.title,
        'content': post.body,
        'created_on': post.created_on.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return JsonResponse(data)

@csrf_exempt
def create_flutter_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Set the author to "Anonymous"
        anonymous_user, created = User._default_manager.get_or_create(username='Anonymous')
        username = data.get("author")
        new_post = Post.objects.create(
            author = username,
            title=data["title"],
            body=data["body"]
            # Add other fields as needed
        )

        new_post.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
