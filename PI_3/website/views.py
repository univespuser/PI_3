from django.shortcuts import render
#from django.http import HttpResponse

def hello_PI_3(request):
#    return HttpResponse("Aqui voce pode fazer uma agenda previa do servico que deseja")
    lista = ['mecanica motor/cambio', 'mecanica outros', 'eletrica injecao eletronica', 'eletrica outros']
    data = {'name': 'Agendamento Servico', 'relacao_servivos_disponiveis': lista}
    return render(request, 'index.html', data)