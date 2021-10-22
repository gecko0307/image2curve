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

bl_info = {
    "name": "GIMP layer to curve",
    "author": "Timur Gafarov",
    "version": (1, 0, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "description": "Blender counterpart of GIMP layer_to_blender_curve plugin",
    "doc_url": "",
    "category": "Add Curve",
}

import os
import bpy

import threading
import tempfile
from xmlrpc.server import SimpleXMLRPCServer

HOST = "127.0.0.1"
PORT = 8000

def launch_server():
    server = SimpleXMLRPCServer((HOST, PORT))
    server.register_function(svg_to_curve)
    server.serve_forever()

def server_start():
    t = threading.Thread(target=launch_server)
    t.daemon = True
    t.start()

def svg_to_curve(svg:str):
    print(svg)
    tmp = tempfile.NamedTemporaryFile(delete=False, mode="w")
    print("Write to %s" % tmp.name)
    tmp.write(svg)
    tmp.close()
    bpy.ops.import_curve.svg(filepath=tmp.name, filter_glob='*')
    os.unlink(tmp.name)
    return {}

def register():
    server_start()

def unregister():
    #TODO
    pass

if __name__ == "__main__":
    register()
