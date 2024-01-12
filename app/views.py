from django.shortcuts import render

# Create your views here.
def card(request):
    return render(request,'card.html')

def alerts(request):
    return render(request,'alerts.html')

def carousels(request):
    return render(request,'carousels.html')

def badges(request):
    return render(request,'badges.html')

def breadcrump(request):
    return render(request,'breadcrump.html')

def button(request):
    return render(request,'button.html')

def modifiers(request):
    return render(request,'modifiers.html')

def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,'child.html')