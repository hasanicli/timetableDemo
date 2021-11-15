from entities import Teacher
from utils import EditText


class Course:
    def __init__(self, noun, hour, teacher_id):
        self.__noun = noun
        self.__hour = hour
        self.__teacher_id = teacher_id

    @property
    def __noun(self):
        return self.noun

    @__noun.setter
    def __noun(self, value):
        assert len(value) > 2, "Alan ismi en az 3 karakterden oluşmalıdır."
        self.noun = EditText().tr_title(value)

    @property
    def __hour(self):
        return self.hour

    @__hour.setter
    def __hour(self, value):
        assert isinstance(value, int), "Sayısal bir değer girilmeli."
        assert value > 0, "Kurs saati 1'den küçük olamaz."
        self.hour = value

    @property
    def __teacher_id(self):
        return self.teacher_id

    @__teacher_id.setter
    def __teacher_id(self, value):
        assert isinstance(value, int), "teacher_id sayısal bir değer olmalı"
        assert value > 0, "teacher_id 1'den küçük olamaz."
        self.teacher_id = value


if __name__ == "__main__":
    tea = Teacher("11111112100", "hasan", "içli", "5056757113", "a@a.com", "elk - elo", "dr.")
    cou = Course("mat", 6, 4)
    print(cou.__dict__)
    print(cou.noun, cou.hour, 4)
