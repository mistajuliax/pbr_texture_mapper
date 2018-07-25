bl_info = {
    "name": "PBR Texture Mapper",
    "description": "Map image nodes from tools like Substance Painter to principled shader",
    "author": "Jayanam",
    "version": (0, 9, 0, 0),
    "blender": (2, 79, 0),
    "location": "NodeEditor",
    "category": "Object"}

# Blender imports
import bpy

from bpy.props import *

from . ptm_mapping_op    import PTM_MappingOperator
from . ptm_panel         import PTM_Panel

addon_keymaps = []

def register():
   bpy.utils.register_class(PTM_MappingOperator)
   bpy.utils.register_class(PTM_Panel)
    
def unregister():
   bpy.utils.unregister_class(PTM_MappingOperator)
   bpy.utils.unregister_class(PTM_Panel)
  
   
   # remove keymap entry
   for km, kmi in addon_keymaps:
       km.keymap_items.remove(kmi)
   addon_keymaps.clear()

    
if __name__ == "__main__":
    register()