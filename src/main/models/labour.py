from src.main.models.person import Person

class Labour(Person):
    def __init__(self, first_name, last_name, wage, role):
        super().__init__(first_name, last_name)
        self.wage = wage
        self.role = role

    def to_dict(self):
        data = super().to_dict()
        data.update({"wage": self.wage, "role": self.role})
        return data