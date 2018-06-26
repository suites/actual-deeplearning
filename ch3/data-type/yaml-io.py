import yaml

customer = [
    {"name": "InSeong", "age": "24", "gender": "man"},
    {"name": "Akatsuki", "age": "22", "gender": "woman"},
    {"name": "Harin", "age": "23", "gender": "man"},
    {"name": "Yuu", "age": "31", "gender": "woman"}
]

yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

data = yaml.load(yaml_str)

for p in data:
    print(p["name"])
