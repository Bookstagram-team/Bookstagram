from django.urls import path
from .views import PostListView
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, forum
from main.views import register, login_user, logout_user, edit_item, delete_item, get_item_json, add_item_ajax
from main.views import UserSearch, ProfileView, ProfileEditView, display_books
from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [

    path('', PostListView.as_view(), name='post-list'),
    path('create-item', create_item, name='create_item'),
    path('forum.html', forum, name='forum_html'),
    path('xml/', show_xml, name='show_xml'),
    path('reply/<int:post_id>/', views.reply_to_post, name='reply_to_post'),
    path('add_reply_ajax/', views.add_reply_ajax, name='add_reply_ajax'),
     
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('handle_reaction/<int:post_id>/<str:reaction>/', views.handle_reaction, name='handle_reaction'),
    
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    #buku
    path('books/', display_books, name='display_books'),


]