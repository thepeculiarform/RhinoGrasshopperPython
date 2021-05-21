__author__ = "The Peculiar Form"
__version__ = "2021.05.21"

"""I only need the gypython lib so I have commented out the other
common Rhino Python libraries that I tend to use."""
import ghpythonlib.components as gh
#import Rhino.Geometry as rg
#import rhinoscriptsyntax as rs

#This is a python library outsite of Rhino that I will use to help sort my objects
from operator import itemgetter


#I am creating an empty list here to hold the circles in x
circles = []

#I am iterating the list coming into the x input in my GH component
for circle in x:
    # I deconstruct each circle into parts and give it a variable name for access
    dcon = gh.DeconstructArc(circle)
    #I create a python tuple to hold my object and the radius value from which to sort
    circles.append((circle, dcon.radius))


#Printing the circles so that they can be seen in the output below and I can
#understand the structure to navigate the values and objects. 
print(circles)
#I am creating a newlist from the circles list and sorting them by the value 
# where radius is. 
newlist = sorted(circles, key=itemgetter([1][0]))
newObjList = [item[0] for item in newlist]


#The original list of circles from x-input that have been deconstructed
a = circles
#This is my new list I constructed out of the deconstructed parts
#nd sorted by the radius
b = newlist
#This is a new list of the objects alone without the radius value I was 
#using for sorting
c = newObjList
#I am grabbing the first and last elements of the newObjList I created
#from my sorted list. So, first should be smallest and last is largest
first = newObjList[0]
last = newObjList[-1]
#I am outputting the first and last elements.
d = first
e = last