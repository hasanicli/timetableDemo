from entities.person import Person
from utils import EditText


class Teacher(Person):
    def __init__(self, identity_number: str, first_name: str, last_name: str, abbreviation_name: str, phone: str, email: str, field: str, authority: str):
        super().__init__(identity_number, first_name, last_name, phone, email)
        self.__abbreviation_name = abbreviation_name
        self.__phone = phone
        self.__email = email
        self.__field = field
        self.__authority = authority

    @property
    def __field(self):
        return self.field

    @__field.setter
    def __field(self, value):
        self.field = value

    @property
    def __authority(self):
        return self.authority

    @__authority.setter
    def __authority(self, value):
        self.authority = value

    @property
    def __abbreviation_name(self):
        return self.abbreviation_name

    @__abbreviation_name.setter
    def __abbreviation_name(self, value):
        assert len(value) <= 4, "Abbreviation name must have less than five characters"
        if value == "":
            value = self.first_name[:1] + "." + self.last_name[:2]
        self.abbreviation_name = value


if __name__ == "__main__":
    try:
        tea = Teacher("11111112100", "hasan", "içli", "","5056757113", "a@a.com", "elk - elo", "dr.")
        print(tea.__dict__)
    except AssertionError as err:
        print(err)
    except AttributeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
