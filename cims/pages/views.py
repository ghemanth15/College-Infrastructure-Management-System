from django.shortcuts import render
from django.http import HttpResponse
from rooms.models import Rooms
from rooms.choices import asset_type_choices,block_no_choices



# index page:
def index(request):
    rooms = Rooms.objects.order_by('-date_of_purchase')[:3]

    context = {
        'rooms' : rooms,
        'asset_type_choices' : asset_type_choices,
        'block_no_choices' : block_no_choices
    }
    return render(request,'pages/index.html',context)

# about page:
def about(request):
    return render(request,'pages/about.html')
