from utils import tr_title
import sqlite3


class Person:
    """
    Base class for teacher. Maybe it can be used another class.
    """

    __table_noun = "persons"

    def __init__(self, identity_number: str, first_name: str, last_name: str, phone: str, email: str):
        self.__identity_number = identity_number.strip()
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__phone = phone.strip()
        self.__email = email.strip()

    def __repr__(self):
        return "person"

    @property
    def __identity_number(self):
        return self.identity_number

    @__identity_number.setter
    def __identity_number(self, value):
        assert len(value) == 11, "identity number must be 11 character."
        assert value.isdigit(), "identity number must be digit."
        self.identity_number = value

    @property
    def __first_name(self):
        return self.first_name

    @__first_name.setter
    def __first_name(self, value):
        self.first_name = tr_title(value)

    @property
    def __last_name(self):
        return self.last_name

    @__last_name.setter
    def __last_name(self, value):
        self.last_name = value

    @property
    def __phone(self):
        return self.phone

    @__phone.setter
    def __phone(self, value):
        self.phone = value

    @property
    def __email(self):
        return self.email

    @__email.setter
    def __email(self, value):
        self.email = value

    def create_query(self):
        # print(self.__dict__.keys())
        # types = ["TEXT" if isinstance(x, str) else ("BOOL" if isinstance(x, bool) else ("INTEGER" if isinstance(x, int) else "REAL")) for x in self.__dict__.values()]
        # nouns = [x for x in self.__dict__.keys()]
        # print(types)

        # bunu geliştir ve son halini ver

        sql_text = [self.__repr__() + "_id INTEGER PRIMARY KEY NOT NULL"] + [
            k + " " + ("TEXT" if isinstance(v, str) else ("BOOL" if isinstance(v, bool) else ("INTEGER" if isinstance(v, int) else "REAL"))) for k, v in self.__dict__.items()]

        print(sql_text)


if __name__ == "__main__":
    try:
        per1 = Person("11111111111", "Ali", "Aydın", "5056757113", "mail@mail.com")
        per1.create_query()

        # tup = tuple(per.__dict__.keys())
        # liste = list(per.__dict__.keys())
        # print(liste[0])

        # print(Person.__dict__['__dict__'])
        # print(vars(Person))
        # print(per.__str__())
        # print(per.__dict__)

        # vt = sqlite3.connect('test.db')
        # cur = vt.cursor()
        # cur.execute(f"""CREATE TABLE IF NOT EXISTS teacher(?,?,?,?,?)""", tuple(*per.__dict__.keys()))
        # cur.execute(f"""CREATE TABLE IF NOT EXISTS teacher({liste[0]},{liste[1]},{liste[2]},{liste[3]},{liste[4]})""")
        # cur.execute("""CREATE TABLE IF NOT EXISTS teacher({},{},{},{},{})""".format(*liste))
        # cur.execute("""CREATE TABLE IF NOT EXISTS teacher({},{},{},{},{})""".format(*per.__dict__.keys()))
        # cur.execute("""CREATE TABLE IF NOT EXISTS {}({},{},{},{},{})""".format(per.__repr__(), *per.__dict__.keys()))
        # cur.execute("""CREATE TABLE IF NOT EXISTS {}({},{},{},{},{})""".format(per.__repr__(), *per.__str__()))
        # vt.close()
    except AssertionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
