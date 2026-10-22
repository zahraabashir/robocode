import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
d = [(k, a[k], b[k]) for k in a if k in b and a[k] != b[k]]
print(d)
