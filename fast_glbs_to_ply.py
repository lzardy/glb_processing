# problem is trimesh saves the ply's with some bloat so they come out slightly larger than the glbs
# but it does consolidate all the glb's to a single mesh files that are simpler to process
from pathlib import Path
import trimesh
root_dir = Path('/media/hpe/SG-20TB/objaverse/glbs')
for file_path in root_dir.glob('**/*'):
    if file_path.is_file():
        mesh = trimesh.load(input_file)
        mesh.export('/media/hpe/SG-20TB/plyverse/' + os.path.splitext(os.path.basename(input_file))[0], file_type='ply')
