from collections import ChainMap
import os, argparse

defaults = {"color": "red", "user": "guest"}
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)

print(f"color={combined['color']}")
print(f"user={combined['user']}")
