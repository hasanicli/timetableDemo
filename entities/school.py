from entities import Teacher


class School:
    def __init__(self, school_name, principal: Teacher = None, phone=None, email=None, fax=None, city=None, district=None, neighborhood=None, address=None):
        self.__name = school_name
        self.__principal = principal
        self.__phone = phone
        self.__email = email
        self.__fax = fax
        self.__city = city
        self.__district = district
        self.__neighborhood = neighborhood
        self.__address = address

    @property
    def __name(self):
        return self.school_name

    @__name.setter
    def __name(self, value):
        self.school_name = value


if __name__ == '__main__':
    sch = School("Osmaniye MTAL")
    print(sch.__dict__)
