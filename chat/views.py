from django.shortcuts import render

# Create your views here.
def chat(request, id):
    return render(request, 'chat/index.html')