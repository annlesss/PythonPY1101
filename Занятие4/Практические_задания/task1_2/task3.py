import re
result1 = re.findall(r"\w*", "Everest is the largest mount in the world")
print(result1)
result2 = re.findall(r"\w+", "Everest is the largest mount in the world")
print(result2)