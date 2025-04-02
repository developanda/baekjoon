import re

A = input()

B = re.sub(r'[^a-zA-Z]','',A)

print(len(B))