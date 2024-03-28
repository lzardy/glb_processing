import bpy
import glob
import os
import pathlib
importDir = "/home/r/Desktop/GLB/"
outputDir = "/home/r/Desktop/PLY/"
print(importDir)
os.chdir(importDir)

counter = 0
for file in glob.glob("*.glb"):
    model_name = pathlib.Path(file).stem
    if pathlib.Path(outputDir+model_name+'.ply').is_file() == True: continue
    #print("Model: " + model_name)
    bpy.ops.import_scene.gltf(filepath=file)
    if bpy.context.active_object.type != 'MESH': 
        bpy.ops.object.delete(use_global=False)
        bpy.ops.outliner.orphans_purge()
        bpy.ops.outliner.orphans_purge()
        bpy.ops.outliner.orphans_purge()
    for obj in bpy.context.selected_objects: obj.name = model_name
    counter = counter + 1
    if counter > 10:
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.001)
        bpy.ops.object.mode_set(mode='OBJECT')
        
        mesh_obs = (o for o in bpy.context.selected_objects
        if o.type == 'MESH' and o.dimensions.length)
        for o in mesh_obs:
            o.scale *= 2 / max(o.dimensions)
            o.scale *= 0.55
            
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')
        
        for obj in bpy.context.selected_objects: obj.location = (0,0,0)
    
        for obj in bpy.context.selected_objects:
            obj.data.color_attributes.new("Color", 'FLOAT_COLOR', 'CORNER')
        bpy.ops.object.bake(type='DIFFUSE')
        for obj in bpy.context.selected_objects:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            bpy.ops.wm.ply_export(
                                    filepath=outputDir+obj.name+'.ply',
                                    filter_glob='*.ply',
                                    check_existing=False,
                                    ascii_format=False,
                                    export_selected_objects=True,
                                    apply_modifiers=True,
                                    export_triangulated_mesh=True,
                                    export_normals=True,
                                    export_uv=False,
                                    export_colors='SRGB',
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

for file in glob.glob("*.glb"):
    model_name = pathlib.Path(file).stem
    if pathlib.Path(outputDir+model_name+'.ply').is_file() == True: continue
    #print("Model: " + model_name)
    bpy.ops.import_scene.gltf(filepath=file)
    for obj in bpy.context.selected_objects: obj.name = model_name
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.001)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    mesh_obs = (o for o in bpy.context.selected_objects
    if o.type == 'MESH' and o.dimensions.length)
    for o in mesh_obs:
        o.scale *= 2 / max(o.dimensions)
        o.scale *= 0.55
        
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')
    
    for obj in bpy.context.selected_objects: obj.location = (0,0,0)
    
    for obj in bpy.context.selected_objects:
        obj.data.color_attributes.new("Color", 'FLOAT_COLOR', 'CORNER')
    bpy.ops.object.bake(type='DIFFUSE')
    for obj in bpy.context.selected_objects:
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.ops.wm.ply_export(
                                filepath=outputDir+obj.name+'.ply',
                                filter_glob='*.ply',
                                check_existing=False,
                                ascii_format=False,
                                export_selected_objects=True,
                                apply_modifiers=True,
                                export_triangulated_mesh=True,
                                export_normals=True,
                                export_uv=False,
                                export_colors='SRGB',
                                global_scale=1.0,
                                forward_axis='Y',
                                up_axis='Z'
                            )
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()

    
