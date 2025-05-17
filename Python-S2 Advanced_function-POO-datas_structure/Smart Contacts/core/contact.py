class Contact:
    def __init__(self, dict):
        self.name = dict.get("name")
        self.email = dict.get("email")
        self.lastname = dict.get("lastname")
        self.phone = dict.get("phone")


    def to_dict(self):
        """Change contact into dict"""
        return {
            'name': self.name,
            'email': self.email,
            'lastname': self.lastname,
            'phone': self.phone
        }
