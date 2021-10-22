# Autotrace
GIMP+Blender plugin bundle to export transparent images from GIMP layers to Blender curves as outlines. This is useful to create complex 2D shapes in Blender that are tedious to create manually. For example, you can create a mesh for a drawn character and animate it with armature or shape keys.

![illustration](/illustration.jpg)

## Installation
Blender 2.9x and GIMP 2.10+ required.

Install `gimp_layer_to_curve.py` in Blender preferences.

Copy `layer_to_blender_curve.py` to GIMP plugins directory (`C:\Users\<user>\AppData\Roaming\GIMP\2.10\plug-ins` under Windows).

The script will be available in `Layer -> To Blender curve` menu in GIMP. There's nothing to be done on Blender part, it works automatically via XML-RPC protocol.
