# this is more useful as meshlab will export textures to e57 pointclouds (not vertex colors though)
# all we want to train our networks on is point clouds, as all we want them to produce are pointclouds
# this segfaults on some GLB files sadly, and even so, objaverse does not convert to point clouds gracefully
# although much easier to filter a bad point cloud than a bad mesh, the resultant quantity of files would be
# much reduced in count over the original dataset.
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
