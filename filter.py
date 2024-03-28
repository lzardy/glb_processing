import os
import shutil
import sys
import pygltflib

def load_glb_folder(folder_path):
    gltf_files = [f for f in os.listdir(folder_path) if f.endswith('.glb')]
    gltf_data = []
    for file in gltf_files:
        gltf_path = os.path.join(folder_path, file)
        gltf = pygltflib.GLTF.load(gltf_path)
        gltf.path = gltf_path
        gltf_data.append(gltf)
    return gltf_data

def filter_meshes(gltf_data, min_vertex_count):
    filtered_meshes = []
    merged_mesh = None

    for gltf in gltf_data:
        for mesh in gltf.meshes:
            for primitive in mesh.primitives:
                if 'POSITION' in primitive.attributes and 'TEXCOORD_0' in primitive.attributes:
                    accessor = gltf.accessors[primitive.attributes['POSITION']]
                    vertex_count = accessor.count
                    if vertex_count >= min_vertex_count:
                        if merged_mesh is None:
                            # Create a new mesh if it doesn't exist
                            merged_mesh = mesh
                        else:
                            # Merge the current mesh into the existing merged mesh
                            merged_mesh.primitives.extend(mesh.primitives)
    if merged_mesh is not None:
        # Add the merged mesh to the filtered meshes
        filtered_meshes.append(merged_mesh)

    return filtered_meshes

def move_filtered_meshes_to_path(folder_path, filtered_meshes):
    for _, gltf in enumerate(filtered_meshes):
        file_path = gltf.path
        # Get file name + extension
        file_name = os.path.basename(file_path)
        destination_folder = os.path.join(folder_path, 'filtered')
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:  # Updated to expect 3 arguments
        print("Usage: python script_name.py folder_path min_vertex_count")
        sys.exit(1)

    folder_path = sys.argv[1]
    min_vertex_count = int(sys.argv[2])  # Added to get min_vertex_count from command line
    gltf_data = load_glb_folder(folder_path)
    filtered_meshes = filter_meshes(gltf_data, min_vertex_count)
    move_filtered_meshes_to_path(folder_path, filtered_meshes)