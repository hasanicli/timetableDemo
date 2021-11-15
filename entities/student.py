import datetime
from time import strftime

from utils import EditText
from entities.person import Person
from utils import check_date


class Student(Person):
    def __init__(self, identity_number, first_name, last_name, phone, email, number, classroom, father, mother, birthdate: datetime, birthplace, gender):
        super().__init__(identity_number, first_name, last_name, phone, email)
        self.number = number
        self.classroom = classroom
        self.father = father
        self.mother = mother
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.gender = gender

    def __setattr__(self, key, value):
        if type(value) == "str":
            value = value.strip()
        edit_text = EditText()
        super().__setattr__(key, value)

        if key == "number":
            assert value.isdigit(), "Öğrenci no sayısal olmalı"
            assert int(value) > 0, "Öğrenci no sıfırdan olmalı"
            self.__dict__[key] = value

        elif key == "classroom":
            assert len(value) > 1 or value == "", "sınıf alanı en az iki karakter olmalı"
            self.__dict__[key] = edit_text.tr_upper(value)

        elif key == "father":
            assert len(value) > 2 or value == "", "baba adı en az üç karakter olmalı"
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == "mother":
            assert len(value) > 2 or value == "", "anne adı en az üç karakter olmalı"
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == 'birthdate':
            # assert check_date(value), "Tarih girişi hatalı"
            self.__dict__[key] = value

        elif key == "birthplace":
            assert len(value) > 2 or value == "", "doğum yeri adı en az üç karakter olmalı"
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == "gender":
            assert len(value) == 1, "Cinsiyet alanı 1 karakter olmalı"
            assert (value == "E" or value == "K"), "Cinsiyet alanı 'E' yada 'K' olabilir"
            self.__dict__[key] = edit_text.tr_upper(value)

    def __delattr__(self, key):
        super().__delattr__(key)
        if key == 'number' or key == 'classroom' or key == 'father' or key == 'mother' or key == 'birthdate' or key == 'birthplace' or key == 'gender':
            raise AttributeError(key + ' attribute cannot be deleted')


if __name__ == "__main__":
    std = Student("11111112100", " mehmet", "erhan", "1234567894", "me@me.com", "123", "", "hasan", "elif", datetime.date(2009, 11, 11).strftime('%d.%m.%Y'), "Düziçi", "E")
    print(std.__dict__)
