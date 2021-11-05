# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OdhDD8AEKIOdW7LgURWgWhd3__-JQAqK

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

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""
#RDFLib
from rdflib.plugins.sparql import prepareQuery
for s, p, o in g.triples((None, RDFS.subClassOf, NS.Person)):
  print(s)

#SPARQL

NS = Namespace("http://somewhere#")
ORG = Namespace("http://www.w3.org/2000/01/rdf-schema#")
q1 = prepareQuery('''
  SELECT ?Subject  WHERE {
    ?Subject org:subClassOf ns:Person.
  }  
  '''
    ,
  initNs = { "ns": NS, "org" : ORG}
)

# Visualize the results
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

#RDFLib
from rdflib.plugins.sparql import prepareQuery

subclass = g.value(subject=None, predicate=RDF.type, object=NS.Researcher) 
print(subclass)
for s, p, o in g.triples((None, RDF.type, NS.Person)):
  print(s)

#SPARQL
NS = Namespace("http://somewhere#")
ORG = Namespace("http://www.w3.org/2000/01/rdf-schema#")
ORG2 = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
q2 = prepareQuery('''
  SELECT DISTINCT ?Instance  WHERE {
     {?Subject org:subClassOf ns:Person.
     ?Instance ?X ?Subject.}
      UNION
     {?Instance rdf:type ns:Person.} 
  }  
  '''
    ,
  initNs = { "ns": NS, "org" : ORG,"org2" : ORG2}
)

# Visualize the results
for r in g.query(q2):
  print(r.Instance)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

#RDFLib
subc= g.value(None, RDFS.subClassOf, NS.Person)
subper= g.value(None, RDF.type, subc)
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  for a,b,c in g.triples((s, None, None)):
    print(a,b)

for s,p,o in g.triples((subper, None, None)):
  print(s,p)

#SPARQL
NS = Namespace("http://somewhere#")
ORG = Namespace("http://www.w3.org/2000/01/rdf-schema#")
ORG2 = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
q3 = prepareQuery('''
  SELECT DISTINCT ?Instance ?X ?Subject  WHERE {
     {?Subject org:subClassOf ns:Person.
     ?Instance ?X ?Subject.}
      UNION
     {?Instance rdf:type ns:Person.
      ?Instance ?X ?Subject.} 
  }  
  '''
    ,
  initNs = { "ns": NS, "org" : ORG,"org2" : ORG2}
)

# Visualize the results
for r in g.query(q3):
  print(r.Instance,r.X,r.Subject)