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
# def recursive_layer_changes():
#     pass

# def dash_sidebar_changes

# Classes are a nice way to organize and navigate the changes you want to make
class derived_map:
    def __init__(self,primary_id, new_id, vis_list=[], del_list=[]):
        self.primary_id = primary_id
        self.new_id = new_id
        self.vis_list = vis_list
        self.del_list = del_list
        self.prim_wm_item = gis.content.get(self.primary_id)
        self.prim_wm_json = self.prim_wm_item.get_data()
    def changes(self, layer_level=self.prim_wm_json['operationalLayers']): # recursive changes to layers
        for i, layer in enumerate(layer_level):
            if layer['id'] in self.vis_list:
                layer_level[i]['visibility'] = True
            else:
                layer_level[i]['visibility'] = False
            if layer['id'] in self.del_list:
                del layer_level[i] # the item to del
            if layer['layerType'] == 'GroupLayer':
                self.changes(layer_level[i])
            pass
        pass
    def push(self): # push changes to the new_id
        pass

class derived_dashboard:
    def __init__(self,primary_id, new_id, del_list):
        self.primary_id = primary_id
        self.new_id = new_id
        self.del_list = del_list
    def changes(self): # deletions for sidebar
        pass
    def push(self): # push changes to the new_id
        pass


# %% 
############ Setting lists of changes

map_changes = [

]

dashboard_changes = [
    
]