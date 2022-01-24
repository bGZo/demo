#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='get several para form terminal')
parser.add_argument('str', metavar='N', type=str, nargs='+',
                    help='desc its usage, then xxxx')
args = parser.parse_args()

# test your object
print(args)