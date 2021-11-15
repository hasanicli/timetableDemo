from entities.person import Person
from utils import EditText


class Teacher(Person):
    def __init__(self, identity_number: str, first_name: str, last_name: str, phone: str, email: str, field: str, authority: str):
        super().__init__(identity_number, first_name, last_name, phone, email)
        self.field = field
        self.authority = authority

    def __setattr__(self, key, value):
        if type(value) == "str":
            value = value.strip()
        edit_text = EditText()
        super().__setattr__(key, value)

        if key == 'field':
            assert len(value) > 2, "Alan ismi en az 3 karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == 'authority':
            assert len(value) > 2, "Görevi alanı en az 3 karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_title(value)

    def __delattr__(self, key):
        super().__delattr__(key)
        if key == 'field' or key == 'authority':
            raise AttributeError(key + ' attribute cannot be deleted')


if __name__ == "__main__":
    try:
        tea = Teacher("11111112100", "hasan", "içli", "5056757113", "a@a.com", "elk - elo", "dr.")
        print(tea.__dict__)
    except AssertionError as err:
        print(err)
    except AttributeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
