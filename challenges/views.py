from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Eat no meat for the entire month!",
    "july": "Walk for at least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "Eat no meat for the entire month!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Eat no meat for the entire month!"
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Djanggo for at least 20 minutes every day!")



# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "Eat no meat for the entire month!"
#     elif month == 'february':
#         challenge_text = "Walk for at least 20 minutes every day!"
#     elif month == 'march':
#         challenge_text = "Learn Django for at least 20 minutes every day!"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        month_text = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month_text 
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

