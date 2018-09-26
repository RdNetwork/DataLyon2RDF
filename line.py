"""Class module for managing bus lines."""
from rdf_utils import write_rdf_prop, print_stops

class Line(object):
    """Class describing a bus line according to the attributes
    provided by the Grand Lyon Open Data platform."""

    BUS_GRAPHNAME = "tcl:busLines"
    SUB_GRAPHNAME = "tcl:subwayLines"
    TRAM_GRAPHNAME = "tcl:tramLines"

    def __init__(self, num, line, index, color, label, garage, titan, orientation, stops):
        """Line object constructor."""
        self.number = num
        self.index = index
        self.line_number = line
        self.color = color
        self.label = label
        self.garage = garage
        self.titan = titan
        self.orientation = orientation
        self.stops = stops

    def print_rdf(self, out, graph_name):
        """Outputs the matching rdf properties (in Turtle syntax)
        for a Line object on a given file."""
        if graph_name == self.BUS_GRAPHNAME:
            prop = "gtfs:Bus"
            letter = 'b'
        elif graph_name == self.SUB_GRAPHNAME:
            prop = "gtfs:Subway"
            letter = 's'
        elif graph_name == self.TRAM_GRAPHNAME:
            prop = "gtfs:LightRail"
            letter = 't'

        out.write("\ttcl:" + letter + str(self.number) + "\n")
        write_rdf_prop(out, 2, "a", prop, False)
        write_rdf_prop(out, 2, "tcl:lineNumber", '"'+self.line_number+'"', False)
        write_rdf_prop(out, 2, "tcl:indexNumber", '"'+self.index+'"', False)
        write_rdf_prop(out, 2, "rdfs:label", '"'+self.label+'"', False)
        write_rdf_prop(out, 2, "tcl:orientation", '"'+self.orientation+'"', False)
        print_stops(out, self.stops)
        write_rdf_prop(out, 2, "tcl:titanCode", '"'+self.titan+'"', False)
        write_rdf_prop(out, 2, "tcl:garageCode", '"'+self.garage+'"', True)
