import utils
from utils import Mesh
import argparse

paser = argparse.ArgumentParser(description="General mesh library")
paser.add_argument("-i", "--input", type=str, required=True)
paser.add_argument("-o", "--output", type=str, required=True)

FLAGS = paser.parse_args()

for k, v in vars(FLAGS).items():
    print("{:10s}: {}".format(k, v))

mesh = Mesh(FLAGS.input)
o_mesh = utils.uv_mapping(mesh)

utils.write_obj(o_mesh, FLAGS.output)
