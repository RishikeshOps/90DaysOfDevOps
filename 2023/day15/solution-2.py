import yaml
import json

# Read YAML file
with open("services.yaml") as f:
    output = yaml.load(f,Loader=yaml.FullLoader)

# Convert YAML to JSON
JSON_data = json.dumps(output)

# Write JSON to a file
with open("services.json", "w") as JSON_file:
   JSON_file.write(JSON_data)


