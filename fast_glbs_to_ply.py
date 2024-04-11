# problem is trimesh saves the ply's with some bloat so they come out slightly larger than the glbs
# but it does consolidate all the glb's to single mesh files that are simpler to process
from pathlib import Path
import trimesh
import os
root_dir = Path('/media/hpe/SG-20TB/objaverse/glbs')
for file_path in root_dir.glob('**/*'):
    if file_path.is_file():
        mesh = trimesh.load(file_path)
        mesh.export('/media/hpe/SG-20TB/plyverse/' + os.path.splitext(os.path.basename(file_path))[0] + '.ply', file_type='ply')
