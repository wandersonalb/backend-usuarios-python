from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UsuarioValidate

import os, json
from django.conf import settings

#metodo get para listar todos os usuários
def get(request):
	if request.method == 'GET':
		list = []
		path_file = settings.BASE_FILE_DB
		
		with open(path_file, 'r', encoding='utf8') as file:
			for line in file:
				list.append(line)

		return JsonResponse(list, safe=False)

#metodo get para busca de nome via parametro passado na url
def search(request):
	if request.method == 'GET':
		list = []
		path_file = settings.BASE_FILE_DB
		query = request.GET.get('query', None)

		if query is not None:
			with open(path_file, 'r', encoding='utf8') as file:
				for line in file:
					if query in line:
						list.append(line)

			return JsonResponse(list, safe=False)

#metodo post para criar novo usuario
@csrf_exempt
def post(request):
	if request.method == 'POST':
		json_data = json.loads(request.body)
		path_file = settings.BASE_FILE_DB
		
		form = UsuarioValidate(json_data)		
		if form.is_valid():
			with open(path_file, 'a', encoding='utf8') as file:
				file.write(json_data['nome']+"\n")
				file.close()

				return JsonResponse(form.cleaned_data, safe=False)
		else:
			return JsonResponse(form.errors, safe=False)