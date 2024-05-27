#!/usr/bin/env python

import glob
import sys
import ruamel.yaml

dir = sys.argv[1]

seen = 0
invalid = 0

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.explicit_start = True

for filename in glob.glob(dir + "/*"):
    seen += 1
    try:
        d = yaml.load(open(filename))
    except Exception as e_info:
        print("failed to load file %s: " % filename, e_info)
        invalid += 1
print(f"seen    {seen}")
print(f"invalid {invalid}")
