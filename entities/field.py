from utils import EditText


class Field:
    def __init__(self, noun, alias):
        self.noun = noun
        self.alias = alias

    def __setattr__(self, key, value):
        edit_text = EditText()
        if key == 'noun':
            assert (len(value.strip()) > 2), "Alan kısmı en az 3 karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_title(value)

        elif key == 'alias':
            assert (len(value) > 1), "Kısaltma kısmı en az 2 karakterden oluşmalıdır."
            self.__dict__[key] = edit_text.tr_title(value)

    def __delattr__(self, key):
        if key == 'noun' or key == 'alias':
            raise AttributeError(key + ' attribute cannot be deleted')


if __name__ == "__main__":
    aut = Field("Elektrik", "Elk")
    print(aut.__dict__)
