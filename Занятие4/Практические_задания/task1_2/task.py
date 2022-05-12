import re
result = 'Everest is the largest mount in the world'
pattern_ = re.compile(r".")
print(pattern_.findall((result)))
