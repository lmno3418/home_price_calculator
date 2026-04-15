from src.main.models.labour import Labour

class Mistri(Labour):
    def __init__(self, first_name, last_name, wage, role, skill):
        super().__init__(first_name, last_name, wage, role)
        self.skill = skill

    def to_dict(self):
        data = super().to_dict()
        data.update({"skill": self.skill})
        return data