from django.shortcuts import render

from .services.RoutesProvider import RoutesProvider
from .services.RoutesRankingAlgorithim import RoutesRankingAlgorithim
from .services.ApiFunctions import api_route_post, api_route_delete

from rest_framework.decorators import api_view
from rest_framework.response import Response as ApiResponse
from rest_framework import status

from .models import Route

import datetime


def index(request):
    if request.method == 'POST':
        try:
            init_lat = request.POST['initLatitude']
            init_long = request.POST['initLongitude']
            end_lat = request.POST['endLatitude']
            end_long = request.POST['endLongitude']
        except:
            error_msg = str('Numero de parametros recibido incorrecto')
            return render(request, "index.html", {'error_msg':error_msg}, status=400)

        variation = request.POST.get('variation', 1.5)

        rra = RoutesRankingAlgorithim()
        
        routes_provider = RoutesProvider(init_lat, init_long, end_lat, end_long, variation)
        routes = routes_provider.get_routes()

        response = dict()
        status = None
        if(len(routes) > 0): 
            routes = rra.add_air_quality_puntuation(routes)
            routes = rra.add_ranking_puntuation(routes)
            routes = rra.sort_ranking(routes)
            
            response['routes'] = routes
            status = 200
        else:
            response['error_msg'] = str('Error con la API Graphhopper.')
            status = 500

        return render(request, "index.html", response, status=status)
    else:
        return render(request, "index.html")


def saved_routes(request):
    if request.user.is_authenticated:
        response = dict()
        status = 200
        if request.method == 'POST':
            if 'operation' in request.POST and request.POST['operation'] == 'order-by':
                order_by = request.POST.get('order-by','default')
                if(order_by == 'date-asc'):
                    response['routes'] = Route.objects.filter(user = request.user.email).order_by('date_saved')
                elif(order_by == 'date-desc'):
                    response['routes'] = Route.objects.filter(user = request.user.email).order_by('-date_saved')
                elif(order_by == 'points'):
                    response['routes'] = list(Route.objects.filter(user = request.user.email))
                    response['routes'].sort(reverse = True, key=lambda item: float(item.ranking_puntuation))
                elif(order_by == 'distance'):
                    response['routes'] = list(Route.objects.filter(user = request.user.email))
                    response['routes'].sort(reverse = True, key=lambda item: float(item.distance))
                elif(order_by == 'default'):
                    response['routes'] = Route.objects.filter(user = request.user.email)
                else:
                    response['error_msg'] = str('No se ha incluido el parametro operation correctamente.')
                    status = 400

            elif 'operation' in request.POST and request.POST['operation'] == 'delete':  #Delete route
                if 'user' in request.POST and 'date-saved' in request.POST:
                    user = request.POST['user']
                    date_saved = datetime.datetime.strptime(request.POST['date-saved'], '%d-%m-%Y %H:%M:%S.%f %z')
                    route_db = Route.objects.filter(user = user, date_saved = date_saved)
                    if(len(list(route_db)) != 0):
                        route_db.delete()
                        response['routes'] = Route.objects.filter(user = request.user.email)
                    else:
                        response['error_msg'] = str('El usuario recibido no tiene la ruta que se quiere borrar.')
                        status = 400
                else:
                    response['error_msg'] = str('No se han incluido los parametros necesarios.')
                    status = 400
            else:
                response['error_msg'] = str('No se ha incluido el parametro operation correctamente.')
                status = 400
        else:
            response['routes'] = Route.objects.filter(user = request.user.email)
        return render(request, "saved-routes.html", response, status=status)
    else:
        return render(request, "login.html", status = 401)


@api_view(['POST']) # And DELETE (because of the problem that we can pass data to the ajax request)
def api_route(request):
    data = dict()
    if request.user.is_authenticated:
        try:
            if request.POST['type'] == 'POST':
                response = api_route_post(request)
            elif request.POST['type'] == 'DELETE':
                response = api_route_delete(request)
            else:
                data['error_msg'] = str('El parametro type tiene un valor incorrecto')
                response = ApiResponse(status = status.HTTP_400_BAD_REQUEST, data = data)
        except Exception as e:
            data['error_msg'] = str(e)
            response = ApiResponse(status = status.HTTP_400_BAD_REQUEST, data = data)
    else:
        data['error_msg'] = str('Debes estar autenticado para poder usar la API.')
        response = ApiResponse(status = status.HTTP_401_UNAUTHORIZED, data = data)
    
    return response