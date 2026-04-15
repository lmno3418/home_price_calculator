from src.main.models.person import Person

class HomeBuyer(Person):
    def __init__(self, first_name, last_name, budget, location):
        super().__init__(first_name, last_name)
        self.budget = budget
        self.location = location

    def to_dict(self):
        data = super().to_dict()
        data.update({"budget": self.budget, "location": self.location})
        return data