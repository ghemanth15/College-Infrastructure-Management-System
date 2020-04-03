
from django.shortcuts import render
from .models import Rooms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .choices import block_no_choices, asset_type_choices

# Create your views here.
def index(request):
    rooms = Rooms.objects.all().order_by('-asset_no','-room_no','-date_of_purchase')
    paginator = Paginator(rooms, 5)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)

    context = {
        'rooms' : paged_rooms
    }

    return render(request, 'rooms/rooms.html',context)

def room(request):
    #room = get_object_or_404(Rooms, pk='room_id')

    context = {
        #'room' : room
    }

    return render(request, 'rooms/room.html',context)

def search(request):

    queryset_list = Rooms.objects.order_by('-date_of_purchase')

    # college code
    if 'clg_code' in request.GET:
        clg_code = request.GET['clg_code']
        if clg_code:
            queryset_list = queryset_list.filter(clg_code__icontains=clg_code)

    # block number
    if 'block_no' in request.GET:
        block_no = request.GET['block_no']
        if block_no:
            queryset_list = queryset_list.filter(block_no__iexact=block_no)

    # asset type
    if 'asset_type' in request.GET:
        asset_type = request.GET['asset_type']
        if asset_type:
            queryset_list = queryset_list.filter(asset_type__iexact=asset_type)

    # asset number
    if 'asset_no' in request.GET:
        asset_no = request.GET['asset_no']
        if asset_no:
            queryset_list = queryset_list.filter(asset_no__iexact=asset_no)


    context = {
        'block_no_choices' : block_no_choices,
        'asset_type_choices' : asset_type_choices,
        'rooms' : queryset_list,
        'views' : request.GET,
    }
    return render(request, 'rooms/search.html',context)
