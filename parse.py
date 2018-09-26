"""Main module for I/O (parsing JSON and writing RDF)"""
import json
import os
from worship import Worship
from line import Line
from user import User
from stop import Stop
from validation import Validation

DIR = os.path.dirname(__file__)

def write_graph(out, instances, graph_name):
    """Writing all instances of an object collection in an output RDF file."""
    out.write(graph_name + " {\n")
    for instance in instances:
        instance.print_rdf(out, graph_name)
    out.write("}\n\n")

# Worship methods
def parse_worships():
    """Parsing worships file (containing all places of worship)."""
    datafile = os.path.join(DIR, "data/worship.json")
    with open(datafile) as data_file:
        json_data = json.load(data_file)
        worship_jsonlist = json_data["features"]
        i = 0
        worships = []
        for place in worship_jsonlist:
            worships.append(parse_worship(place, i))
            i += 1

        return worships


def parse_worship(json_node, number):
    """Creating a Worship object for a matching JSON node."""
    label = json_node["properties"]["nom"].encode('utf-8')
    internal_id = json_node["properties"]["identifiant"]
    creation_date = json_node["properties"]["datecreation"]
    latitude = json_node["geometry"]["coordinates"][1]
    longitude = json_node["geometry"]["coordinates"][0]
    return Worship(number, label, latitude, longitude, internal_id, creation_date)



# Utility for all transportation systems
def parse_stops(stops_node):
    """Parsing a list of coordinates couples describing transportation stops."""
    stops = []
    num = 0
    for stop_node in stops_node:
        stop = Stop(num, stop_node[1], stop_node[0])
        stops.append(stop)
        num += 1
    return stops


# Line methods
def parse_lines(means):
    """Parsing a JSON file ith line data."""
    datafile = os.path.join(DIR, "data/"+means+".json")
    with open(datafile) as data_file:
        json_data = json.load(data_file)
        lines_jsonlist = json_data["features"]
        i = 0
        lines = []
        for line in lines_jsonlist:
            lines.append(parse_line(line, i))
            i += 1
        return lines


def parse_line(json_node, number):
    """Creating a Line object for a matching JSON node."""
    line = json_node["properties"]["ligne"]
    index = json_node["properties"]["indice"]
    color = json_node["properties"]["couleur"]
    label = json_node["properties"]["libelle"].encode('utf-8')
    garage = json_node["properties"]["ut"]
    titan = json_node["properties"]["code_titan"]
    orientation = json_node["properties"]["sens"]
    stops = parse_stops(json_node["geometry"]["coordinates"])
    return Line(number, line, index, color, label, garage, titan, orientation, stops)
