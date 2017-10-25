from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from django.forms.models import model_to_dict
from .models import Hero
import json


def hero_list(request):
	if request.method == 'GET':
		return JsonResponse(list(Hero.objects.all().values()), safe=False)
	elif request.method == 'POST':
		name = json.loads(request.body.decode())['name']
		new_hero = Hero(name=name)
		new_hero.save()
		return HttpResponse(status=201)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])


def hero_detail(request, hero_id):
	hero_id = int(hero_id)
	
	if request.method == 'GET':
		try:
			hero = Hero.objects.get(id=hero_id)
		except Hero.DoesNotExist:
			return HttpResponseNotFound()
		
		return JsonResponse(model_to_dict(hero))
	elif request.method == 'PUT':
		name = json.loads(request.body.decode())['name']
		
		try:
			hero = Hero.objects.get(id=hero_id)
		except Hero.DoesNotExist:
			return HttpResponseNotFound()
		
		hero.name = name
		hero.save()
		return HttpResponse(status=204)
	elif request.method == 'DELETE':
		try:
			hero = Hero.objects.get(id=hero_id)
		except Hero.DoesNotExist:
			return HttpResponseNotFound()
		
		hero.delete()
	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
