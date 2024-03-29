from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'confessions/home.html')

def confession(request, pk):
    return render(request, 'confessions/confession.html', context={'pk': pk})

def confess(request):
    return render(request, 'confessions/confess.html')

def about(request):
    return render(request, 'confessions/about.html')

#sign-up
def signup(request):
    return render(request, 'confessions/sign-up.html')

#sign-in
def signin(request):
    return render(request, 'confessions/sign-in.html')