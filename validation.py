"""Class module for managing validation occurences."""
import random
from datetime import datetime
from rdf_utils import write_rdf_prop, random_date

class Validation(object):
    """Class describing a validation occurence, i.e. when a user
    validates their trip using their transportation card or ticket."""

    GRAPHNAME = "tcl:valids"

    def __init__(self, number, validator, time, stop, user):
        """Validation constructor."""
        self.number = number
        self.validator = validator
        self.datetime = time
        self.stop = stop
        self.user = user

    def print_rdf(self, out, graph_name):
        """Outputs the matching rdf properties (in Turtle syntax)
        for a Validation object on a given file."""
        out.write("\ttcl:v" + str(self.number) + "\n")
        write_rdf_prop(out, 2, "a", "tcl:Validation", False)
        write_rdf_prop(out, 2, "tcl:validator", '"'+self.validator+'"', False)
        write_rdf_prop(out, 2, "tcl:validationDatetime", '"'+str(self.datetime)
                       +'"^^xsd:dateTime', False)
        if not self.user is None:
            write_rdf_prop(out, 2, "tcl:user", "\ttcl:u"+str(self.user.number), False)
        write_rdf_prop(out, 2, "geo:latitude", '"'+str(self.stop.latitude)+'"', False)
        write_rdf_prop(out, 2, "geo:longitude", '"'+str(self.stop.longitude)+'"', True)

    @staticmethod
    def create_traffic(validations_nb, lineset, userset):
        """Create a random set of validations with their attributes."""
        valids = []
        for i in range(0, validations_nb):
            validator = str(random.randint(0, 5000))
            start_d = datetime.strptime('1/1/2017', '%d/%m/%Y')
            end_d = datetime.strptime('30/6/2017', '%d/%m/%Y')
            date = random_date(start_d, end_d)
            stop = random.choice(random.choice(lineset).stops)
            if random.choice([True, False]):
                user = random.choice(userset)
            else:
                user = None
            curr_valid = Validation(i, validator, date, stop, user)
            valids.append(curr_valid)

        return valids
