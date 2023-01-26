from pyexpat.errors import messages
from django.shortcuts import HttpResponse, render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.mixins import LoginRequiredMixin
from livros.models import Livros
from livros.form import LivrosForm



 #CREATE 
def createLivros(request):
    formLivros = LivrosForm(request.POST or None)
    if formLivros.is_valid() :
        formLivros.save()
        return redirect("")    

    pacote = {"formLivros": formLivros}
    return render(request, "Create/createLivros.html", pacote)

#UPDATE
def updateLivros(request, id):
    est = Livros.objects.get(pk=id)
    formLivros = LivrosForm(request.POST or None, instance=est)
    if formLivros.is_valid() :
        formLivros.save()
        return redirect("")    

    pacote = {"formLivros": formLivros}
    return render(request, "Create/createLivros.html", pacote)
#DELETE 

def deleteLivros(request, id):
    est = Livros.objects.get(pk=id)
    est.delete()
    return redirect("") 

def login(request):
    if request.method =="GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect("/livrospretendidos")
        else:
            return HttpResponse("Usuário ou senha invalidos")



def listalivrospretendidos(request):
    livros = Livros.objects.all().filter(liv_leitura = False) 
    parametros = {
        "livrospretendidos": livros
    }
    return render(request, "livrospretendidos.html", parametros)
    
def listalivroslidos(request):
    livros = Livros.objects.filter(liv_leitura = True) 
    parametros = {
        "livroslidos": livros
    }
    return render(request, "table.html", parametros)
# Create your views here.

