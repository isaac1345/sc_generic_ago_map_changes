'''
Author: Isaac Cave
Date: 15th Dec, 2022
Demonstration of using arcgis api to automatically derive new maps and dashboards from a source.
This script is set up in sections, with '# %%' delineating sections, and allowing cell based running in Visual Studio Code.
This code is set up to be content agnostic; you should be able to copy and paste it into your project and adapt it to work with your data for most common usages

Updates:
v0.1


'''


# %%
############ Imports
from arcgis.gis import GIS

# %% 
############ log in and set up your AGO connection
# Depending on your script, you may want to handle passwords differently
url = 'http://governmentofbc.maps.arcgis.com' # change to your url, whether maphub, geohub, or other
username = 'foo'
password = 'bar'
gis = GIS(url, username, password)

# %% 
############ Functions and classes

# Recursion required if layers are nested in groups
def recursive_layer_changes():
    pass

# Classes are a nice way to organize and navigate the changes you want to make
class derived_map:
    def __init__(self,):
        pass

class derived_dashboard:
    def __init__(self,):
        pass


# %% 
############ Setting lists of changes

map_changes = [

]

dashboard_changes = [
    
]