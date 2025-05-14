dict1={
    "name": "manideep",
    "k":[1,2,34,0],
    "h":(1,23,4),
    "r":{
        "phy":98,
        "chem":90
        }
    }
dict1["surname"]="pateru"
print(dict1.keys())
print(len(dict1))
print(dict1.values())
print(dict1.get("name"))
new={"name":"harsha","k":[1]}
dict1.update(new)
print(dict1)