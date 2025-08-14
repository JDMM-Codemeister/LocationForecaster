from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    location = request.GET.get("location")  # Get search from form
    forecast_result = None

    if location:
        # TODO call forecast API function
        forecast_result = f"Example forecast for {location}"

    return render(request, 'home.html', {
        "location": location,
        "forecast_result": forecast_result
    })

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')



def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})