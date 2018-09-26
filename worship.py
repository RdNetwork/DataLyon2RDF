"""Class module for managing places of worship."""
from rdf_utils import write_rdf_prop

class Worship(object):
    """Class describing a place of worship according to the attributes
    provided by the Lyon Metropolis."""

    GRAPHNAME = "gld:worships"

    def __init__(self, num, label, latitude, longitude, internal_id, creation_date):
        """Place of worship object constructor."""
        self.number = num
        self.label = label
        self.latitude = latitude
        self.longitude = longitude
        self.internal_id = internal_id
        self.creation_date = creation_date

    def print_rdf(self, out, graph_name):
        """Outputs the matching rdf properties (in Turtle syntax)
        for a Worship object on a given file."""
        out.write("\tgld:w" + str(self.number) + "\n")
        write_rdf_prop(out, 2, "a", "lgdo:placeOfWorship", False)
        write_rdf_prop(out, 2, "rdfs:label", '"'+self.label+'"', False)
        write_rdf_prop(out, 2, "geo:latitude", str(self.latitude), False)
        write_rdf_prop(out, 2, "geo:longitude", str(self.longitude), False)
        write_rdf_prop(out, 2, "gld:id", '"'+self.internal_id+'"', False)
        write_rdf_prop(out, 2, "gld:creationDate", '"'+self.creation_date+'"^^xsd:date', True)
