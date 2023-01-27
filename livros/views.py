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
    if request.user.is_authenticated:
        formLivros = LivrosForm(request.POST or None)
        if formLivros.is_valid() :
            formLivros.save()
            return redirect("/livrospretendidos")    

        pacote = {"formLivros": formLivros}
        return render(request, "Create/createLivros.html", pacote)
    else:
        return HttpResponse("É preciso estar logado")

#UPDATE
def updateLivros(request, id):
    if request.user.is_authenticated:
        est = Livros.objects.get(pk=id)
        formLivros = LivrosForm(request.POST or None, instance=est)
        if formLivros.is_valid() :
            formLivros.save()
            return redirect("/livrospretendidos")    

        pacote = {"formLivros": formLivros}
        return render(request, "Create/createLivros.html", pacote)
    else:
        return HttpResponse("É preciso estar logado")
#DELETE 

def deleteLivros(request, id):
    if request.user.is_authenticated:
        est = Livros.objects.get(pk=id)
        est.delete()
        return redirect("/livrospretendidos") 

#LOGIN
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
#CADASTRO
def cadastro(request):
    if request.method =="GET":
        return render(request, 'cadastro-usuario.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user1 = User.objects.filter(username=username).first()
        if user1:
            return HttpResponse("Ja existe um usuário com esse nome")
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()    
        return redirect("/")


def listalivrospretendidos(request):
    if request.user.is_authenticated:
        livros = Livros.objects.all().filter(liv_leitura = False) 
        parametros = {
            "livrospretendidos": livros
        }
        return render(request, "livrospretendidos.html", parametros)
    else:
        return HttpResponse("É preciso estar logado")
        
def listalivroslidos(request):
    if request.user.is_authenticated:
        livros = Livros.objects.filter(liv_leitura = True) 
        
        parametros = {
            "livroslidos": livros
        }
        return render(request, "table.html", parametros)
    else:
        return HttpResponse("É preciso estar logado")
# Create your views here.

