import random
from fortune import getFortunes
import argparse

parser = argparse.ArgumentParser(description='Python script to randomly generate fortunes')
parser.add_argument('-c', required=False, help='home many to return', dest='count', type=int)
parser.add_argument('-v', action='version', version='1.0')
args = parser.parse_args()

fortunes = getFortunes()

if args.count:
    for i in range(args.count):
        print(random.choice(fortunes))   
else:
    print(random.choice(fortunes))