from django.shortcuts import render,redirect,get_object_or_404
from mysite.models import Candidate

# Create your views here.

def Home(request):
    query = request.POST.get("q")
    if query:
        CandidateDetails = get_object_or_404(Candidate, VerificationCode = query)
        return render(request,'candidate.html',{})
    else:
        return render(request, 'home.html', {})