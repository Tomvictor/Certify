from django.shortcuts import render, redirect, get_object_or_404
from mysite.models import Candidate


# Create your views here.

def Home(request):
    return render(request, 'home.html', {})


def Details(request):
    query = request.GET.get("q")
    if query:
        CandidateDetails = get_object_or_404(Candidate, VerificationCode=query)
        return render(request, 'page.html', {"item": CandidateDetails})
    return redirect("mysite:home-page")
