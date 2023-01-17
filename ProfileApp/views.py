from django.shortcuts import render,HttpResponse


def base(request):
    return render(request,"base.html")

def resume(request):
    return render(request,"resume.html")

def home(request):
    return render(request,"home.html")

def educational(request):
    return render(request,"educational.html")

def interests(request):
    return render(request,"interests.html")

def occupation(request):
    return render(request,"occupation.html")

def roleModel(request):
    return render(request,"roleModel.html")

def sale(request):
    return render(request,"sale.html")

def earphone(reqeust):
    return render(reqeust,"earphone.html")

def speaker(reqeust):
    return render(reqeust,"speaker.html")

def keyboard(reqeust):
    return render(reqeust,"keyboard.html")
