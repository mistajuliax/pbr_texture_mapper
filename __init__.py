bl_info = {
    "name": "PBR Texture Mapper",
    "description": "Map image nodes from tools like Substance Painter to principled shader",
    "author": "Jayanam",
    "version": (0, 9, 0, 1),
    "blender": (2, 80, 0),
    "location": "NodeEditor",
    "category": "Material"}

# Blender imports
import bpy

from bpy.props import *

from . ptm_mapping_op    import PTM_MappingOperator
from . ptm_align_op      import PTM_AlignOperator
from . ptm_icon_manager  import PTM_IconMgr
from . ptm_panel         import PTM_Panel

addon_keymaps = []
iconMgr = None

def register():
   iconMgr = PTM_IconMgr()
   iconMgr.load()
   
   bpy.utils.register_class(PTM_MappingOperator)
   bpy.utils.register_class(PTM_AlignOperator)
   bpy.utils.register_class(PTM_Panel)
   

    
def unregister():
   iconMgr.unload()
   bpy.utils.unregister_class(PTM_MappingOperator)
   bpy.utils.unregister_class(PTM_AlignOperator)
   bpy.utils.unregister_class(PTM_Panel)
  
   
   # remove keymap entry
   for km, kmi in addon_keymaps:
       km.keymap_items.remove(kmi)
   addon_keymaps.clear()

    
if __name__ == "__main__":
    register()