from django.shortcuts import render,HttpResponse,redirect

def index(request):
    context = {
        "username":"Leonardo",
        "friends" : ["Isabella", "Juan Jose", "Ana Marìa"]
    }
    return render(request,"index.html", context)

def dogs(request):
    if request.method == "GET":
        return HttpResponse("dogs")
    elif request.methog == "POST":
        dog = request.POST["dogs"]
        return redirect(f'/{dog}')