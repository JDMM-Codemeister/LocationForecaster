from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    location = request.GET.get('location', '')  # Get input, or empty string if none
    forecast_result = None

    if location:
        # Find coordinates on map and load forecasts
        forecast_result = f"Forecast for {location} is sunny!"  # TODO REPLACE WITH TRIGGER MAP UPDATE

    return render(request, 'home.html', {
        'location': location,
        'forecast_result': forecast_result,
    })

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')



def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})