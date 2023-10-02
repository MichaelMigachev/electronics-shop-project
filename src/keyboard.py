from src.item import Item

class MixinKeyb:
    """Инициализация миксин-класса MixinKeyboard"""
    Language = 'EN'

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        """Вывод языка раскладки клавиатуры"""
        return self.__language

    def change_lang(self):
        '''Изменить раскладку клавиатуры'''
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language



class Keyboard(Item, MixinKeyb):
    '''Инициализация подкласса клавиатуры'''
    pass
