# "The Peculiar Form"

__author__ = 'Kaushik LS'
__email__ = 'kaushiklsk96@gmail.com'

# - - - - - - - - CODE

import Rhino

def GetRadius(circle):
    return circle.Radius

CirclesList = [geo for geo in x if geo.GetType() == Rhino.Geometry.Circle]

CirclesList.sort(key = GetRadius)

big, small = CirclesList[-1], CirclesList[0]




# - - - - - - - - EXPLANATION

# TIP
# I know it is easier to use ghpythonlib, I started there too.
# But try to start using the RhinoCommon API. It has much more flexibility.   
import Rhino

# Created a function so I can use the result as a sorting parameter.

def GetRadius(circle):
    return circle.Radius

# List comprehension.
CirclesList = [geo for geo in x if geo.GetType() == Rhino.Geometry.Circle]

# NOTE
# I am checking the geometry type before adding them to my list.
# It is always better to do this, because we cannot control what
# stupid geometry a random user might connect. Without this check,
# if the user inputs polygons, polylines, meshes, my code will try
# to get the radius, and result in a error. I'm simply avoiding all
# that by filtering.

""" The above statement is the same as:

OPTION A:

CirclesList = []
for geo in x:
    if geo.GetType() == Rhino.Geometry.Circle:
        CirclesList.append(geo)
        
OPTION B:

CirclesList = []
for i in range(len(x)):
    if x[i].GetType() == Rhino.Geometry.Circle:
        CirclesList.append(x[i])
"""


# Here, I am sorting the circles by their Radius in ascending order.
CirclesList.sort(key = GetRadius)

# This is same as your code. Getting the first and the last items.
big, small = CirclesList[-1], CirclesList[0]

""" It is same as: 

big = CirclesList[-1]
small = CirclesList[0]

"""
