"""Utility functions manipulating RDF."""
import random
from datetime import timedelta

def write_rdf_prop(out, depth, prop, value, end):
    """Outputs a properly formatted Turtle line for a property-value couple."""
    tabs = '\t' * depth
    if value and prop:
        if end is None:
            last = "]\n"
        else:
            last = '.\n' if end else ';\n'
        out.write(tabs+prop+"\t\t"+value+last)

def write_headers(out):
    """Writing RDF prefixes to the output file."""
    out.write("@prefix rdf:	<http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
    out.write("@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .\n")
    out.write("@prefix owl:    <http://www.w3.org/2002/07/owl#> .\n")
    out.write("@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .\n")
    out.write("@prefix dc:     <http://purl.org/dc/elements/1.1/> .\n")
    out.write("@prefix dcterms:<http://purl.org/dc/terms/> .\n")
    out.write("@prefix foaf: 	<http://xmlns.com/foaf/0.1/> .\n")
    out.write("@prefix geo:	<http://www.w3.org/2003/01/geo/wgs84_pos#> .\n")
    out.write("@prefix datex: 	<http://vocab.datex.org/terms#> .\n")
    out.write("@prefix lgdo:	<http://linkedgeodata.org/ontology/> .\n")
    out.write("@prefix tcl: 	<http://localhost/> .\n")
    out.write("@prefix gld: 	<http://data.grandlyon.com/> .\n")
    out.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
    out.write("@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .\n")
    out.write("@prefix gtfs: 	<http://vocab.gtfs.org/terms#> .\n\n")


def print_stops(out, stops):
    """Write stops data individually for an array of stops provided (a stop = 2 coordinates)."""
    out.write("\t\ttcl:stops\t\t( \n")
    for stop in stops:
        out.write("\t\t\t[")
        write_rdf_prop(out, 0, "a", "gtfs:Stop", False)
        write_rdf_prop(out, 3, "geo:latitude", '"'+str(stop.latitude)+'"', False)
        write_rdf_prop(out, 3, "geo:longitude", '"'+str(stop.longitude)+'"', None)
    out.write("\t\t);\n")


def print_comment(out, comment):
    """Write a properly formatted one-line comment to the RDF file."""
    res = "\n### " + comment + " ###\n\n"
    out.write(res)

def random_date(start, end):
    """
    This function will return a random datetime between two date objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)
