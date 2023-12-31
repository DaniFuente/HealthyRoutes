import requests
from ..models import Route
from django.conf import settings


class RoutesProvider():
    def __init__(self, init_lat, init_long, end_lat, end_long, variation):
        self.init_lat = float(init_lat)
        self.init_long = float(init_long)
        self.end_lat = float(end_lat)
        self.end_long = float(end_long)
        self.variation = float(variation)
        self.graphhopper_api_key = settings.GRAPHHOPPER_API_KEY


    def get_routes(self):
        routes = self.routes_api_request()
        return routes


    def routes_api_request(self):
        routes = list()

        response = requests.get('https://graphhopper.com/api/1/route?point=' + str(self.init_lat) + ',' + str(self.init_long) + '&point=' + str(self.end_lat) + ',' + str(self.end_long) + '&vehicle=foot&locale=es&calc_points=true&key=' + self.graphhopper_api_key + '&instructions=true&algorithm=alternative_route&points_encoded=false&ch.disable=true&alternative_route.max_paths=10&alternative_route.max_weight_factor=' + str(self.variation))
        
        if(response.status_code == 200):
            routes_json = response.json()['paths']      
            for route_json in routes_json:
                route = Route(distance = round(route_json['distance']/1000, 2), time = int(round(route_json['time']/60000,0))) #distancia recibida en metros y convertida a kilometros, y tiempo recibido en milisegundos y convertida a minutos
                
                nodes_json = route_json['points']['coordinates']
                nodes = list()

                for node_json in nodes_json:
                    node = dict()
                    node['longitude'] = node_json[0]
                    node['latitude'] = node_json[1]
                    node['air_quality'] = None

                    nodes.append(node)

                route.nodes = nodes

                instructions_json = route_json['instructions']
                instructions = list()

                for instruction_json in instructions_json:
                    instruction = dict()
                    instruction['distance'] = int(instruction_json['distance'])
                    instruction['text'] = instruction_json['text']
                    instructions.append(instruction)

                route.instructions = instructions

                routes.append(route)
            #endif
        return routes




        