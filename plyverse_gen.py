# long winded but does the job
# the initial trimesh will dump st as doubles (bad)
# the meshlab will cull the st but dump xyz as doubles (bad)
# the final trimesh pass saves only xyz as floats (yay) with faces ofc
# result: one big consolidated mesh, no particles like lights or animations, no materials, in a nice condense binary format
# a binary format well supported by pretty much all 3D software (PLY) https://paulbourke.net/dataformats/ply
from pathlib import Path
import pymeshlab
import trimesh
import os
meshlab_server = pymeshlab.MeshSet()
root_dir = Path('/media/hpe/SG-20TB/objaverse/glbs')
for file_path in root_dir.glob('**/*'):
    if file_path.is_file():
        save_path = '/media/hpe/SG-20TB/plyverse/' + os.path.splitext(os.path.basename(file_path))[0] + '.ply'
        if not Path(save_path).is_file():
            try:
                mesh = trimesh.load(file_path)
                mesh.export('/tmp/o1.ply', file_type='ply')
                meshlab_server.load_new_mesh('/tmp/o1.ply')
                meshlab_server.save_current_mesh('/tmp/o1.ply')
                mesh = trimesh.load('/tmp/o1.ply')
                mesh.apply_scale(1.0/mesh.scale) # (2/scale)*0.55 well, 1/scale is slightly smaller so, same difference it's still fits in the unit sphere
                mesh.export(save_path, file_type='ply')
            except Exception:
                pass
