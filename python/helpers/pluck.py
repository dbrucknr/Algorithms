from uuid import uuid4
from operator import itemgetter
from typing import List

#################################################################
users = [
    {
        "id": 1,
        "name": "Harry Potter"
    },
    {
        "id": 2,
        "name": "Ron Weasley"
    },
    {
        "id": 3,
        "name": "Hermione Granger"
    }
]

names = map(itemgetter("name"), users)
print(list(names))

#################################################################
def pluck(array, key):
    return [x.get(key) for x in array]

names = pluck(users, "name")
print(names)

#################################################################
single_instance = {
    "key": "value",
    "a": "b",
    "test": "me"
}

pluck = lambda dict, *args: (dict[arg] for arg in args)

key, a = pluck(single_instance, "key", "a")
print(key, a)
# OR:
key, a = itemgetter("key", "a")(single_instance)
print(key, a)

#################################################################

nested_instance = [
    [
        {
            "group": 1,
            "uid": uuid4(),
            "status": True
        },
        {
            "group": 1,
            "uid": uuid4(),
            "status": False
        },
        {
            "group": 1,
            "uid": uuid4(),
            "status": True
        }
    ],
    [
        {
            "group": 2,
            "uid": uuid4(),
            "status": True
        },
        {
            "group": 2,
            "uid": uuid4(),
            "status": True
        },
        {
            "group": 2,
            "uid": uuid4(),
            "status": True
        } 
    ],
    [
        {
            "group": 3,
            "uid": uuid4(),
            "status": False
        },
        {
            "group": 3,
            "uid": uuid4(),
            "status": False
        },
        {
            "group": 3,
            "uid": uuid4(),
            "status": False
        } 
    ]
]

index = itemgetter(0)
groups = itemgetter("status")

# Selects the key for the specified index in each nested array
print(list(map(lambda instance: groups(index(instance)), nested_instance)))
print(list(map(lambda array: array[0]['status'], nested_instance)))

# print("*****************************")
# # Get each nested array's value
# print(
#     [
#         list(map(lambda obj: obj['status'], nested_array)) 
#         for nested_array 
#         in nested_instance
#     ]
# )

# Get each nested array's value for specified key
def pluck_nested_values(array_of_arrays: List[List], key: str) -> List:
    return [
        list(map(lambda obj: obj[key], array)) 
        for array 
        in array_of_arrays
    ]

print(pluck_nested_values(nested_instance, 'group'))
print(pluck_nested_values(nested_instance, 'status'))