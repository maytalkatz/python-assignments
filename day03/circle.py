import argparse
import math

parser = argparse.ArgumentParser(description="Calculate properties of a circle")
parser.add_argument("radius", type=float, help="Radius of the circle")

args = parser.parse_args()
radius = args.radius

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius


print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
