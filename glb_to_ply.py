# takes a folder of GLB files and processes them into PLY files
import bpy
import glob
import os
from os import mkdir
from os.path import isdir
import pathlib

# ---

importDir = "GLB/"
outputDir = "PLY0/"
if not isdir(outputDir): mkdir(outputDir)

for file in glob.glob(importDir + "*.glb"):
    model_name = pathlib.Path(file).stem
    if pathlib.Path(outputDir+model_name+'.ply').is_file() == True: continue
    try:
        bpy.ops.import_scene.gltf(filepath=file)
    except:
        continue
    bpy.ops.wm.ply_export(
                            filepath=outputDir+model_name+'.ply',
                            filter_glob='*.ply',
                            check_existing=False,
                            ascii_format=False,
                            export_selected_objects=True,
                            apply_modifiers=True,
                            export_triangulated_mesh=True,
                            export_normals=True,
                            export_uv=False,
                            export_colors='NONE',
                            global_scale=1.0,
                            forward_axis='Y',
                            up_axis='Z'
                        )
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()

# ---

importDir = "PLY0/"
outputDir = "PLY1/"
if not isdir(outputDir): mkdir(outputDir)

counter = 0
for file in glob.glob(importDir + "*.ply"):
    model_name = pathlib.Path(file).stem
    if pathlib.Path(outputDir+model_name+'.ply').is_file() == True: continue
    bpy.ops.wm.ply_import(filepath=file)
    counter = counter + 1
    if counter > 10:
        bpy.ops.object.select_all(action='SELECT')
        
        mesh_obs = (o for o in bpy.context.selected_objects
        if o.type == 'MESH' and o.dimensions.length)
        for o in mesh_obs:
            o.scale *= 2 / max(o.dimensions)
            o.scale *= 0.55
            
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')
        
        for obj in bpy.context.selected_objects: obj.location = (0,0,0)

        for obj in bpy.context.selected_objects:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            bpy.ops.wm.ply_export(
                                    filepath=outputDir+model_name+'.ply',
                                    filter_glob='*.ply',
                                    check_existing=False,
                                    ascii_format=False,
                                    export_selected_objects=True,
                                    apply_modifiers=True,
                                    export_triangulated_mesh=True,
                                    export_normals=True,
                                    export_uv=False,
                                    export_colors='NONE',
                                    global_scale=1.0,
                                    forward_axis='Y',
                                    up_axis='Z'
                                )
                                
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        bpy.ops.outliner.orphans_purge()
        bpy.ops.outliner.orphans_purge()
        bpy.ops.outliner.orphans_purge()
        counter = 0
        
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()

for file in glob.glob(importDir + "*.ply"):
    model_name = pathlib.Path(file).stem
    if pathlib.Path(outputDir+model_name+'.ply').is_file() == True: continue
    bpy.ops.wm.ply_import(filepath=file)
    
    bpy.ops.object.select_all(action='SELECT')
    
    mesh_obs = (o for o in bpy.context.selected_objects
    if o.type == 'MESH' and o.dimensions.length)
    for o in mesh_obs:
        o.scale *= 2 / max(o.dimensions)
        o.scale *= 0.55
        
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')
    
    for obj in bpy.context.selected_objects: obj.location = (0,0,0)
    
    for obj in bpy.context.selected_objects:
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.ops.wm.ply_export(
                                filepath=outputDir+model_name+'.ply',
                                filter_glob='*.ply',
                                check_existing=False,
                                ascii_format=False,
                                export_selected_objects=True,
                                apply_modifiers=True,
                                export_triangulated_mesh=True,
                                export_normals=True,
                                export_uv=False,
                                export_colors='NONE',
                                global_scale=1.0,
                                forward_axis='Y',
                                up_axis='Z'
                            )
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
