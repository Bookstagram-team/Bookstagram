from django.urls import path
from communities.views import *

app_name = 'communities'

urlpatterns = [
    path('booklist/', show_books, name='show_books'),
    path('event/', show_communities, name='show_communities'),
    path("add-book/", add_event_ajax, name="add_event_ajax"),
    path('get-event-json/', get_event_json, name='get_event_json'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('show-json/', show_flutter_json, name='show_json'),
]