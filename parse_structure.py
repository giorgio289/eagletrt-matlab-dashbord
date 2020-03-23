import json

JSON_PATH = "./structure.json"
CSV_PATH = "./output.csv"

with open(JSON_PATH) as json_file:
    json_text = json_file.read()
structure = json.loads(json_text)

rows = []

def parse(data, path=None):
    if isinstance(data, list):
        message = data[0]
        if isinstance(message["value"], dict):
            values = message["value"]
            columns = [
                dict(
                    name = f"{path}__{value}",
                    path = f"{path.replace('__', '.')}.value",
                    prop = value 
                ) 
                for value in values
            ]
            rows.extend(["{name},{path},{prop}".format(**c) for c in columns ])
        else:
            column = dict(
                    name = path,
                    path = f"{path.replace('__', '.')}.value",
                    prop = "" 
            ) 
            rows.append("{name},{path},{prop}".format(**column))
    elif isinstance(data, dict):
        for (key, value) in data.items():
            parse(value, f"{path}__{key}" if path is not None else key)

parse(structure)

with open(CSV_PATH, "w") as csv_file:
    csv_file.write("name,path,property\n")
    csv_file.write("\n".join(rows))