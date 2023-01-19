import json

cloude_VM_name = {}

cloud_VM_name = {
    "aws": "ec2",
    "azure": "VM",
    "gcp": "compute engine"
}

# Write the dictionary to a JSON file
with open("services.json", "w") as json_file:
    json.dump(cloud_VM_name, json_file)

# Read the JSON file
with open("services.json", "r") as JSON_file:
    data = json.load(JSON_file)

# Print the service names of every cloud service provider
for provider, service in data.items():
    print(f"{provider} : {service}")
