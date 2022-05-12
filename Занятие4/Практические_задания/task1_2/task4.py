import re
result = re.findall(r"\w+", "Everest is the largest mount in the world")
result = re.findall(r'\b[aeiouAEI]\w+', "Everest is the largest mount in the world")
print(result)