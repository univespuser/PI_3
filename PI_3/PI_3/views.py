from django.http import HttpResponse

def hello_world(request):
	return HttpResponse("Seja bem vindo! A Oficina e Auto-Eletrico Dois Amigos agradece a sua visita.")