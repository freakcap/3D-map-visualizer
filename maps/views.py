from django.shortcuts import render

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiZnJlYWtjYXAiLCJhIjoiY2thdDVwY25uMHFiajMwbXNyankxM3hhciJ9.jvvDKXA3O8cQwqt2d9zK3A'
    return render(request, 'default.html', 
                { 'mapbox_access_token' : mapbox_access_token })

