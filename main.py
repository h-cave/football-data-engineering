import json

open_data_path = "/home/harry/projects/open-data/data"

with open(f"{open_data_path}/events/3749493.json", "r") as file:
    data = json.load(file)

print(data)
print("Data type")
print(type(data))

records = 0
for data in data:
    records += 1
    print(f"Record {records}: {data['type']['name']}")


print ("#########RECORDS#########")
print(f"Total Records: {records}")

print ("#########data#########")
print(f"LENGTH:{len(data)}")


res = next(iter(data))
print(f"First record: {res}")
