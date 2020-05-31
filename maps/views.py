from django.shortcuts import render
# from .models import ImgModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiZnJlYWtjYXAiLCJhIjoiY2thdDVwY25uMHFiajMwbXNyankxM3hhciJ9.jvvDKXA3O8cQwqt2d9zK3A'
    return render(request, 'default.html', 
        { 'mapbox_access_token' : mapbox_access_token })
    # if request.method == 'POST':
    #     if request.data:
    #         imgModel=ImgModel()
    #         imgModel.imgUrl= request.data
    #         imgModel.save()
            
    #         return render(request, 'default.html', 
    #     { 'mapbox_access_token' : mapbox_access_token })

    # else:
    #         return render(request, 'default.html', 
    #     { 'mapbox_access_token' : mapbox_access_token })