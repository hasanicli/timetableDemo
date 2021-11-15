from utils import EditText, check_identity_number, check_phone, check_email


class Person:
    def __init__(self, identity_number: str, first_name: str, last_name: str, phone: str, email: str):
        self.identity_number = identity_number
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __setattr__(self, key, value: str):
        edit_text = EditText()

        if key == "identity_number":
            assert check_identity_number(value.strip()), "Geçerli bir 'TC Kimlik Numarası' giriniz."
            self.__dict__[key] = value

        elif key == "first_name":
            assert (len(value.strip()) > 2), "İsim alanı en az 3 karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == "last_name":
            assert (len(value.strip()) > 1), "Soyisim alanı en az iki karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_upper(value)

        elif key == 'phone':
            assert check_phone(value) or len(value) == 0, "Geçerli bir telefon numarası giriniz.\n(Boş geçebilirsiniz.)"
            self.__dict__[key] = value

        elif key == 'email':
            assert (check_email(value) or len(value) == 0), "Geçerli bir email adresi giriniz.\n(Boş geçebilirsiniz.)"
            self.__dict__[key] = value

    def __delattr__(self, key):
        if key == 'identity_number' or key == 'first_name' or key == 'last_name' or key == "phone" or key == "email":
            raise AttributeError(key + ' attribute cannot be deleted')


if __name__ == "__main__":
    try:
        per = Person("12222222228", "abbas", "çiçek ", "5056757113", "aP@a.com")

        print(per.__dict__)

    except AttributeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
