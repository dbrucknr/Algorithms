from operator import itemgetter

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

key, a = itemgetter("key", "a")(single_instance)
print(key, a)