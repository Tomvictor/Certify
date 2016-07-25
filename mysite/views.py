from django.shortcuts import render,redirect,get_object_or_404
from mysite.models import Candidate

# Create your views here.

def Home(request):
    query = request.POST.get("q")
    print(query)
    if query:
        CandidateDetails = get_object_or_404(Candidate, VerificationCode = query)
        return render(request,'page.html',{"item":CandidateDetails})
    else:
        return render(request, 'home.html', {})