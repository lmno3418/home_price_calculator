from src.main.models.labour import Labour
from src.main.models.mistri import Mistri
from src.main.models.homebuyer import HomeBuyer

class PersonFactory:
    @staticmethod
    def create_person(person_type, **kwargs):
        if person_type.lower() == "labour":
            return Labour(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"])
        elif person_type.lower() == "mistri":
            return Mistri(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"], kwargs["skill"])
        elif person_type.lower() == "homebuyer":
            return HomeBuyer(kwargs["first_name"], kwargs["last_name"], kwargs["budget"], kwargs["location"])
        else:
            raise ValueError(f"Invalid person type: {person_type}")
