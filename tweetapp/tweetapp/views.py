from django.shortcuts import render

def layout(request):
    return render(request, 'firstpage.html')