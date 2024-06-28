from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'dashboard.html')
def Posting(request):
    return render(request, 'posting.html')

