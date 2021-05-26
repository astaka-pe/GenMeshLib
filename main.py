from utils import Mesh
import argparse

paser = argparse.ArgumentParser(description="General mesh library")
paser.add_argument("-i", "--input", type=str, required=True)

FLAGS = paser.parse_args()

for k, v in vars(FLAGS).items():
    print("{:10s}: {}".format(k, v))

mesh = Mesh(FLAGS.input)

import pdb;pdb.set_trace()