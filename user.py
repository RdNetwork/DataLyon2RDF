#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Class module for managing users."""
import random
from datetime import datetime
import names
from rdf_utils import write_rdf_prop, random_date


class User(object):
    """Class describing a basic transportation user"""

    GRAPHNAME = "tcl:users"

    def __init__(self, num, name, surname, birthdate, subscription):
        """User constructor method."""
        self.number = num
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.subscription = subscription

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
            curr_user = User(i, names.get_last_name(), names.get_first_name(),
                             random_date(start, end).strftime('%Y-%m-%d'), sub)
            users.append(curr_user)

        return users


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
