#!/usr/bin/env python

"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

import xmlrpclib
from gimpfu import *

def export_svg(svg):
    proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
    try:
        proxy.svg_to_curve(svg)
    except xmlrpclib.Fault as err:
        pdb.gimp_message(err.faultString)

def layer_to_blender_curve(image, layer):
    if not pdb.gimp_item_is_group(layer):
        mask = layer.mask
        if not mask:
            mask = layer.create_mask(ADD_ALPHA_TRANSFER_MASK)
            layer.add_mask(mask)
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, mask)
        path = pdb.plug_in_sel2path(image, None)
        pdb.gimp_selection_none(image)
        
        vector_name = pdb.gimp_path_list(image)[1][0]
        vec = pdb.gimp_image_get_vectors_by_name(image, vector_name)
        vec.name = "mask_path"
        
        svg = pdb.gimp_vectors_export_to_string(image, path)
        export_svg(svg)
        
        pdb.gimp_image_remove_vectors(image, vec)
        pdb.gimp_layer_remove_mask(layer, 0)
    

register(
    "python_fu_layer_to_blender_curve",
    "Layer to Blender curve",
    "Exports layer alpha channel to Blender curve via RPC",
    "Timur Gafarov",
    "CC-0",
    "2021",
    "<Image>/Layer/To Blender curve",
    "*",
    [],
    [],
    layer_to_blender_curve)

main()
