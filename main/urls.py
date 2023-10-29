from django.urls import path
from main.views import *
from main.views import UserSearch, ProfileView, ProfileEditView, display_books
app_name = 'main'


urlpatterns = [
    path('discussion/', PostListView.as_view(), name='discussion_page'),
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_rating_ajax, name='add_rating_ajax'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    #buku
    path('books/', display_books, name='display_books'),
    path('get_book/', get_book_json, name='get_book_json' ),
    path('add_book/', add_book, name='add_book'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('catalogue/', catalogue_view, name='catalogue_page'),
    path('sort_book/', sort_book, name='sort_book'),
    path('handle_reaction/<int:post_id>/<str:reaction>/', handle_reaction, name='handle_reaction'),
    path('reply/<int:post_id>/', reply_to_post, name='reply_to_post'),
    path('add_reply_ajax/', add_reply_ajax, name='add_reply_ajax'),

]