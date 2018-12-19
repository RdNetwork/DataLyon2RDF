#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Class module for managing users."""
import random
import string
from datetime import datetime
import names
from rdf_utils import write_rdf_prop, random_date


class User(object):
    """Class describing a basic transportation user"""

    GRAPHNAME = "tcl:users"

    def __init__(self, num, name, surname, birthdate, address, subscription):
        """User constructor method."""
        self.number = num
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.subscription = subscription
        self.address = address

    def print_rdf(self, out, graph_name):
        """Outputs the matching rdf properties (in Turtle syntax)
        for a User object on a given file."""
        out.write("\ttcl:u" + str(self.number) + "\n")
        write_rdf_prop(out, 2, "a", "tcl:User", False)
        if not self.subscription is None:
            out.write("\t\tdatex:subscription [\n")
            write_rdf_prop(out, 3, "a", "datex:Subscription", False)
            write_rdf_prop(out, 3, "datex:subscriptionStartTime",
                           '"'+self.subscription["start"]+'"^^xsd:date', False)
            if not self.subscription["stop"] is None:
                write_rdf_prop(out, 3, "datex:subscriptionStopTime",
                               '"'+self.subscription["stop"]+'"^^xsd:date', False)
            write_rdf_prop(out, 3, "datex:subscriptionReference",
                           '"'+self.subscription["ref"]+'"', False)
            out.write("\t\t];\n")
        write_rdf_prop(out, 2, "foaf:givenName", '"'+self.name+'"', False)
        write_rdf_prop(out, 2, "foaf:familyName", '"'+self.surname+'"', False)
        write_rdf_prop(out, 2, "vcard:hasAddress", '"'+self.address+'"', False)
        write_rdf_prop(out, 2, "tcl:birthday", '"'+self.birthdate+'"^^xsd:dateTime', True)

    @staticmethod
    def create_users(users_nb):
        """Create a random set of users with their attributes."""
        users = []
        for i in range(0, users_nb):
            start = datetime.strptime('1/1/1900', '%d/%m/%Y')
            end = datetime.strptime('31/12/1999', '%d/%m/%Y')
            if random.choice([True, False]):
                sub = User.random_sub()
            else:
                sub = None
            adr = User.random_adr()
            curr_user = User(i, names.get_last_name(), names.get_first_name(),
                             random_date(start, end).strftime('%Y-%m-%d'), adr, sub)
            users.append(curr_user)

        return users

    @staticmethod
    def random_adr():
        """Return a random address in the Grand Lyon area."""
        towns = [
            "Albigny-sur-Saône",
            "Bron",
            "Cailloux-sur-Fontaines",
            "Caluire-et-Cuire",
            "Champagne-au-Mont-d'Or",
            "Charbonnières-les-Bains",
            "Charly",
            "Chassieu",
            "Collonges-au-Mont-d'Or",
            "Corbas",
            "Couzon-au-Mont-d'Or",
            "Craponne",
            "Curis-au-Mont-d'Or",
            "Dardilly",
            "Décines-Charpieu",
            "Ecully",
            "Feyzin",
            "Fleurieu-sur-Saône",
            "Fontaines-Saint-Martin",
            "Fontaines-sur-Saône",
            "Francheville",
            "Genay",
            "Givors",
            "Grigny",
            "Irigny",
            "Jonage",
            "La Mulatière",
            "La Tour de Salvagny",
            "Limonest",
            "Lissieu",
            "Lyon",
            "Lyon 1er arrondissement",
            "Lyon 2e arrondissement",
            "Lyon 3e arrondissement",
            "Lyon 4e arrondissement",
            "Lyon 5e arrondissement",
            "Lyon 6e arrondissement",
            "Lyon 7e arrondissement",
            "Lyon 8e arrondissement",
            "Lyon 9e arrondissement",
            "Marcy-l'Etoile",
            "Meyzieu",
            "Mions",
            "Montanay",
            "Neuville-sur-Saône",
            "Oullins",
            "Pierre-Bénite",
            "Poleymieux-au-Mont-d'Or",
            "Quincieux",
            "Rillieux-la-Pape",
            "Rochetaillée-sur-Saône",
            "Saint-Cyr-au-Mont-d'Or",
            "Saint-Didier-au-Mont-d'Or",
            "Saint-Fons",
            "Saint-Genis-Laval",
            "Saint-Genis-les-Ollières",
            "Saint-Germain-au-Mont-d'Or",
            "Saint-Priest",
            "Saint-Romain-au-Mont-d'Or",
            "Sainte-Foy-lès-Lyon",
            "Sathonay-Camp",
            "Sathonay-Village",
            "Solaize",
            "Tassin-la-Demi-Lune",
            "Vaulx-en-Velin",
            "Vénissieux",
            "Vernaison",
            "Villeurbanne",
        ]

        str_types = ["Rue", "Avenue", "Boulevard", "Route", "Place"]

        return random.randint(0, 250) + " " + random.choice(str_types) + " " + random.choice(string.letters) + " " + "69XXX" + " " +  random.choice(towns)

    @staticmethod
    def random_sub():
        """Returns a random subscription object."""
        refs = ["Jeune", "Campus", "Pro", "Sénior", None]
        start_1 = datetime.strptime('1/1/2007', '%d/%m/%Y')
        start_2 = datetime.strptime('31/12/2011', '%d/%m/%Y')
        end_1 = datetime.strptime('1/1/2012', '%d/%m/%Y')
        end_2 = datetime.strptime('31/12/2017', '%d/%m/%Y')

        # Subscription ends with a random proportions
        if random.choice([True, False]):
            sub_end = random_date(end_1, end_2)
        else:
            sub_end = None

        sub_date = random_date(start_1, start_2)
        ref = random.choice(refs)

        if ref is None:
            return None
        else:
            return {
                "start": sub_date.strftime('%Y-%m-%d'),
                "stop": None if (sub_end is None) else sub_end.strftime('%Y-%m-%d'),
                "ref": ref
            }
