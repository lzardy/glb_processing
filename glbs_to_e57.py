# this is more useful as meshlab will export textures to e57 pointclouds (not vertex colors though)
# all we want to train our networks on is point clouds, as all we want them to produce are pointclouds
from pathlib import Path
import os
import pymeshlab as ml
meshlab_server = ml.MeshSet()
root_dir = Path('/media/hpe/SG-20TB/objaverse/glbs')
for file_path in root_dir.glob('**/*'):
    if file_path.is_file():
        try:
            meshlab_server.load_new_mesh(str(file_path))
            meshlab_server.save_current_mesh('/media/hpe/SG-20TB/e57verse/' + os.path.splitext(os.path.basename(file_path))[0] + '.e57')
        except Exception:
            pass
