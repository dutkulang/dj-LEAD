from django.shortcuts import render, HttpResponse
from account.models import Profile, Country, Region,Skill
def home(request):
    context = {
        'regions' : Region.objects.all(),
        'countries': Country.objects.all(),
        'skills': Skill.objects.all(),
        'profiles': Profile.objects.all(),
        # Entry.objects.all().filter(pub_date__year=2006)
    }
    return render(request, 'blog/index.html', context)

def create_account(request):
    return render(request, 'blog/create-account.html')  
  
def login(request):
    return render(request, 'blog/login.html')

def profiles(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'blog/profiles.html', context)

def profile(request, pk):
    context = {
        'skills': Skill.objects.all().filter(profile=pk),
        #Skill.objects.filter(profile = 1).all(),
        'profile': Profile.objects.get(pk=pk)
    }
    return render(request, 'blog/profile.html', context) 


def about(request):
    return render(request, "about.html")