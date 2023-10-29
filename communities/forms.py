from django.forms import ModelForm
from communities.models import Event

class ProductForm(ModelForm):
    class Meta:
        model = Event
        fields = ["nama_event", "tanggal_pelaksanaan", "foto","harga"]