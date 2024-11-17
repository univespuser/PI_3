from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post, Solicitacao

def hello_PI_3(request):
#    return HttpResponse("Aqui voce pode fazer uma agenda previa do servico que deseja")
    lista = ['mecanica motor/cambio', 'mecanica outros', 'eletrica injecao eletronica', 'eletrica outros']
    
    list_posts = Post.objects.all()
    
    data = {
        'name': 'Agendamento Servico', 
        'relacao_servivos_disponiveis': lista, 
        'posts': list_posts 
        }
    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post':post})

def ss_form(request):
    nome = request.POST['nome']
    Solicitacao.objects.create(
        nome=nome,
        cpf=request.POST['cpf'],
        celular=request.POST['celular'],
        placa=request.POST['placa'],
        modelo=request.POST['modelo'],
        descricao=request.POST['descricao'],
        )
    return render(request, 'confirma_ss.html', {'nome_ss': nome})