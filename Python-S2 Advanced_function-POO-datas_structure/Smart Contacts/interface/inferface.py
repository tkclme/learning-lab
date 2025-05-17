
def get_info(requests):
    new_contact = {}
    for key, value in requests.items():
        new_contact.update({key: input(value).strip()})
    return new_contact

