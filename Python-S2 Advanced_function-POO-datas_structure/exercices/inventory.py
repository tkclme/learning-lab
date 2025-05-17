inventory = {}

def update(collection:dict, **object):
    for key, value in object.items():
        collection.update({key: value})


def display(collection):
    sorted_collection = sorted([(key, value) for key, value in collection.items()])
    for object in sorted_collection:
        print(object)
    # [print(f'- {key} : {value}') for key, value in collection.items()]

update(inventory, pasta=32, bread=44, cheese=12)
display(inventory)

