from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from .forms import UsuarioValidate

import os, json
from django.conf import settings

class MyView(FormView):

	#metodo get para listar todos os usuários
	#caso receba o parametro na url, faz pesquisa
	def get(self, request):
		if request.method == 'GET':

			list = []
			path_file = settings.BASE_FILE_DB

			query = request.GET.get('query', False)			
			
			with open(path_file, 'r', encoding='utf8') as file:
				for i, line in enumerate(file):
					if query:
						if query in line:
							list.append({'id': i+1, 'nome': line})
					else:
						list.append({'id': i+1, 'nome': line})

			return JsonResponse(list, safe=False)

	#metodo post para criar novo usuario
	def post(self, request):
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