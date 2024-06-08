from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None
}

weekly_challenges = {
    "monday" : "Study Python and JavaScript and do Chest/Back Day at the gym",
    "tuesday" : "Study Java and for Network+ exam and do Arms/Shoulders Day at the gym",
    "wednesday" : "Study Django and JavaScript and do Legs Day at the gym",
    "thursday" : "Study Java and for Network+ exam and do cardio/core exercise",
    "friday" : "Study Python and JavaScript and do Chest/Back Day at the gym",
    "saturday" : "Study Java and for Network+ exam and do Arms/Shoulders Day at the gym",
    "sunday" : "Study Django and JavaScript and do Legs Day at the gym"
}

def index(request):
    months = list(monthly_challenges.keys())
    
    days = list(weekly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
        "days" : days
    })

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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
