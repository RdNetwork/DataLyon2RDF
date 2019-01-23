"""Main module."""
import sys
import os
from parse import *
from rdf_utils import write_headers, print_comment

DIR = os.path.dirname(__file__)                 #Root directory
OUTFILE = os.path.join(DIR, "out/output.ttl")   #Output file
NB_USERS = 30                                   #Number of users to be generated
NB_TRAFFIC = 50                                 #Number of travels to be generated


def main():
    """Main process function."""
    if not os.path.exists(os.path.join(DIR, "out")):
        os.makedirs(os.path.join(DIR, "out"))

    with open(OUTFILE, "w+") as out:
        print "Writing RDF prefixes..."
        write_headers(out)

        print_comment(out, "Lyon Metropolis data: Places of Worship")
        print "Writing places of worship..."
        write_graph(out, parse_worships(), Worship.GRAPHNAME)

        print_comment(out, "SYTRAL data: Transportation lines")
        print "Writing bus lines..."
        bus_lines = parse_lines("bus")
        write_graph(out, bus_lines, Line.BUS_GRAPHNAME)
        print "Writing subway lines..."
        subway_lines = parse_lines("subway")
        write_graph(out, subway_lines, Line.SUB_GRAPHNAME)
        print "Writing tramway lines..."
        tram_lines = parse_lines("tram")
        write_graph(out, tram_lines, Line.TRAM_GRAPHNAME)

        print_comment(out, "Artificial SYTRAL private data: Transportation users")
        print "Writing artificial user data..."
        users = User.create_users(NB_USERS)
        write_graph(out, users, User.GRAPHNAME)

        print_comment(out, "Artificial SYTRAL private data: Traffic information")
        print "Writing traffic data..."
        valids = Validation.create_traffic(NB_TRAFFIC, subway_lines, users)
        write_graph(out, valids, Validation.GRAPHNAME)

if __name__ == "__main__":
    sys.exit(main())
