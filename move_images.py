import argparse
import os

parser = argparse.ArgumentParser(
    prog='move_images',
    description='Moves images from date folders to sample ID folders')
parser.add_argument('-p', '--path', type=str, required=True)
args = parser.parse_args()

root_path = os.path.abspath(args.path)
print('Using root path:', root_path)