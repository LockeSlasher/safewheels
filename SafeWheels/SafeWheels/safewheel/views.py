from asyncio.windows_events import NULL
from audioop import reverse
from email.policy import default
from http.client import HTTPResponse
from tkinter import Entry
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Estabelecimentos

def index(request): # Working
    estabelecimentos = Estabelecimentos.objects.all
    return render(request, 'safewheel/index.html', {"estabelecimentos": estabelecimentos})

def login_user(request): # Working
    if request.method == "GET":
        return render(request, 'safewheel/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            return HttpResponse('Usuario não encontrado')
        

def mudaSenha(request): # Work in Progress
    return render(request, 'safewheel/mudaSenha.html')

def esqueceuSenha(request): # Working
    if request.method =="GET":
        return render(request, 'safewheel/esqueceuSenha.html')
    else: 
        email = request.POST['email']
    return HttpResponse('Email de confirmação foi enviado com sucesso para '+ str(email))

def cadastroEstabelecimento(request):
    if request.method =="GET":
        return render(request, 'safewheel/cadastroEstabelecimento.html')
    else:
        nomeE = request.POST.get('nomeE')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        horario = request.POST.get('horario')
        imagens = request.FILES.get('imagens')
        rampa_para_acesso = request.POST.get('check1')
        if(rampa_para_acesso == 'on'): rampa_para_acesso = True
        else: rampa_para_acesso = False
        barras_de_apoio = request.POST.get('check2')
        if(barras_de_apoio == 'on'): barras_de_apoio = True
        else: barras_de_apoio = False
        banheiro_adapt = request.POST.get('check3')
        if(banheiro_adapt == 'on'): banheiro_adapt = True
        else: banheiro_adapt = False
        acess_transporte = request.POST.get('check4')
        if(acess_transporte == 'on'): acess_transporte = True
        else: acess_transporte = False
        acess_arquit = request.POST.get('check5')
        if(acess_arquit == 'on'): acess_arquit = True
        else: acess_arquit = False
        acess_comunic = request.POST.get('check6')
        if(acess_comunic == 'on'): acess_comunic = True
        else: acess_comunic == False
        acess_digital = request.POST.get('check7')
        if(acess_digital == 'on'): acess_digital = True
        else: acess_digital = False
        acess_instrument = request.POST.get('check8')
        if(acess_instrument == 'on'): acess_instrument = True
        else: acess_instrument = False
        acess_program = request.POST.get('check9')
        if(acess_program == 'on'): acess_program = True
        else: acess_program = False
        acess_metod = request.POST.get('check10')
        if(acess_metod == 'on'): acess_metod = True
        else: acess_metod = False
        
        Estabelecimentos.objects.create(nome=request.user, nomeE=nomeE, local=local, desc=desc, horario=horario, imagens=imagens, rampa_para_acesso=rampa_para_acesso,
        barras_de_apoio=barras_de_apoio, banheiro_adapt=banheiro_adapt, acess_transporte=acess_transporte, acess_arquit=acess_arquit, acess_comunic=acess_comunic,
        acess_digital=acess_digital, acess_instrument=acess_instrument, acess_program=acess_program, acess_metod=acess_metod)
        estabelecimentos = Estabelecimentos.objects.all()
        return render(request, 'safewheel/cadastroEstabelecimento.html', {"estabelecimentos": estabelecimentos})

def cadastroUsuario(request, id=NULL):
    if request.method == "GET":
        return render(request, 'safewheel/cadastroUsuario.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')   
        password2 = request.POST.get('password2')

        user = User.objects.filter(username=username).first()

        if password != password2:
            return HttpResponse('Senha não estão iguais')
        if user:
            return HttpResponse('Já existe um usuario com este nome')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, f"Sua conta foi criada com sucesso, {username}")

            return redirect('login')


def detalhesEstabelecimentos(request, id):
    estabelecimentos = get_object_or_404(Estabelecimentos, id=id)
    return render(request, 'safewheel/detalhesEstabelecimentos.html', {"estabelecimentos": estabelecimentos})

def editarEstabelecimento(request, id):
    estabelecimento = Estabelecimentos.objects.get(id=id)
    return render(request, 'safewheel/editarEstabelecimento.html', {"estabelecimentos": estabelecimento})

def updateEstabelecimento(request, id):
    nomeE = request.POST.get('nomeE')
    local = request.POST.get('local')
    desc = request.POST.get('desc')
    horario = request.POST.get('horario')
    imagens = request.FILES.get('imagens')
    rampa_para_acesso = request.POST.get('check1')
    if(rampa_para_acesso == 'on'): rampa_para_acesso = True
    else: rampa_para_acesso = False
    barras_de_apoio = request.POST.get('check2')
    if(barras_de_apoio == 'on'): barras_de_apoio = True
    else: barras_de_apoio = False
    banheiro_adapt = request.POST.get('check3')
    if(banheiro_adapt == 'on'): banheiro_adapt = True
    else: banheiro_adapt = False
    acess_transporte = request.POST.get('check4')
    if(acess_transporte == 'on'): acess_transporte = True
    else: acess_transporte = False
    acess_arquit = request.POST.get('check5')
    if(acess_arquit == 'on'): acess_arquit = True
    else: acess_arquit = False
    acess_comunic = request.POST.get('check6')
    if(acess_comunic == 'on'): acess_comunic = True
    else: acess_comunic == False
    acess_digital = request.POST.get('check7')
    if(acess_digital == 'on'): acess_digital = True
    else: acess_digital = False
    acess_instrument = request.POST.get('check8')
    if(acess_instrument == 'on'): acess_instrument = True
    else: acess_instrument = False
    acess_program = request.POST.get('check9')
    if(acess_program == 'on'): acess_program = True
    else: acess_program = False
    acess_metod = request.POST.get('check10')
    if(acess_metod == 'on'): acess_metod = True
    else: acess_metod = False

    estabelecimento = Estabelecimentos.objects.get(id=id)

    estabelecimento.nomeE = nomeE
    estabelecimento.local = local
    estabelecimento.desc = desc
    estabelecimento.horario = horario
    estabelecimento.imagens = imagens
    estabelecimento.rampa_para_acesso = rampa_para_acesso
    estabelecimento.barras_de_apoio = barras_de_apoio
    estabelecimento.banheiro_adapt = banheiro_adapt
    estabelecimento.acess_transporte = acess_transporte
    estabelecimento.acess_arquit = acess_arquit
    estabelecimento.acess_comunic = acess_comunic
    estabelecimento.acess_digital = acess_digital
    estabelecimento.acess_instrument = acess_instrument
    estabelecimento.acess_program = acess_program
    estabelecimento.acess_metod = acess_metod

    estabelecimento.save()

    return redirect('index')

def deletar(request, id):
    estabelecimento = get_object_or_404(Estabelecimentos, id=id)

    estabelecimento.delete()
    return redirect('index')