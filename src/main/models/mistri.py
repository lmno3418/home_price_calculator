from src.main.models.labour import Labour

class Mistri(Labour):
    def __init__(self, first_name, last_name, wage, role, skills=None):
        super().__init__(first_name, last_name, wage, role)
        self.skills = skills if skills else []

    def to_dict(self):
        data = super().to_dict()
        data.update({"skills": self.skills})
        return data