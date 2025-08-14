from django.shortcuts import render, HttpResponse
from openai import OpenAI
from schluesselwoerter import openAI_key
from .models import TodoItem

#openAI API key
OPENAI_API_KEY = openAI_key
client = OpenAI(api_key=OPENAI_API_KEY)


# Create your views here.
def home(request):
    location = request.GET.get("location")  # Get search from form
    year = request.GET.get("year")
    llm_response = None

    #TODO get region as well as city

    if location:
        # call forecast API function
        prompt = f"What will {location} look like in the year {year}. "

        completion = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You are a climate researcher and social policy analyst focusing on the affects of climate change and economic policy on wealth inequality. Limit your answer to less than 100 words."},

                {"role": "user", "content": prompt}
            ]
        )

        llm_response = completion.choices[0].message.content

    return render(request, 'home.html', {
        "location": location,
        "forecast_result": llm_response
    })

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')



def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})