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
    def changes(self, layer_level="initial"): # recursive changes to layers
        if layer_level == "initial":
            layer_level=self.prim_wm_json['operationalLayers']
        for i in reversed(range(len(layer_level))):
            if layer_level[i]['id'] in self.vis_list:
                layer_level[i]['visibility'] = True
            else:
                layer_level[i]['visibility'] = False
            if layer_level[i]['id'] in self.del_list: # causes indexing issues
                del layer_level[i] # the item to del
            elif layer_level[i]['layerType'] == 'GroupLayer':
                self.changes(layer_level[i]['layers'])
    def push(self): # push changes to the new_id
        self.deriv_wm_item = gis.content.get(self.new_id)
        self.deriv_wm_item.update(data = self.prim_wm_json)

class derived_dashboard:
    def __init__(self,primary_id, new_id, del_list):
        self.primary_id = primary_id
        self.new_id = new_id
        self.del_list = del_list
        self.prim_db_item = gis.content.get(self.primary_id)
        self.prim_db_json = self.prim_db_item.get_data()
    def changes(self): # deletions for sidebar
        for i, selector in enumerate(self.prim_db_json['sidebar']['selectors']):
            if selector[id] in self.del_list:
                del self.prim_db_json['sidebar']['selectors'][i]
    def push(self): # push changes to the new_id
        self.deriv_wm_item = gis.content.get(self.new_id)
        self.deriv_wm_item.update(data = self.prim_db_json)

# %% 
############ Setting lists of changes

map_list = [
    derived_map(
        "8aab32af2c4d48b091dadb55592f723b",
        "33b382a5fda74641a658128f7c3513b4",
        ["182cc61d735-layer-4"], 
        ["18517e8ca9d-layer-10"]
        ) # initial example
]

dashboard_list = [
    
]

# %% 
############ Running the code

for in_map in map_list:
    in_map.changes()
    in_map.push()

for in_db in dashboard_list:
    in_db.changes()
    in_db.push()