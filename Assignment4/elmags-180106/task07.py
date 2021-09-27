# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nj3HeGMmnmG4RPmdnaqWSKFzWwQPFYdD

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

#RDFLib

print(" -- RDFLib -- \n")

for subClass, a, b in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(subClass)

#SPARQL

print("\n -- SPARQL -- \n")

q1 = prepareQuery('''
  SELECT ?class
    WHERE { ?class rdfs:subClassOf ns:Person }
  ''',
  initNs={"rdfs": RDFS, "ns":ns}
)

for r1 in g.query(q1):
  print(r1)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

#RDFLib

print(" -- RDFLib -- \n")

for individuals, a, b in g.triples((None, None, ns.Person)):
  print(individuals)

#SPARQL

print("\n -- SPARQL -- \n")

q2 = prepareQuery('''
  SELECT ?class ?prop
    WHERE { ?class ?prop ns:Person }
  ''',
  initNs={"ns":ns}
)

for r2 in g.query(q2):
  print(r2)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

#RDFLib

print(" -- RDFLib -- \n")

for individuals in g.triples((None, None, ns.Person)):
  print(individuals)

#SPARQL

print("\n -- SPARQL -- \n")

q3 = prepareQuery('''
  SELECT ?class ?prop
    WHERE { ?class ?prop ns:Person }
  ''',
  initNs={"ns":ns}
)

for r3 in g.query(q3):
  print(r3)