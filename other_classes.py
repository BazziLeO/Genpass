from root_description import *


class Symbolbet:
    def __init__(self, symbolbet=''):
        self.symbolbet = symbolbet
        self.reserve_symbolbet = self.symbolbet
        self.black_string = ''

    def update_reserve(self):
        self.reserve_symbolbet = self.symbolbet

    def add_symbols(self, symbol_list):
        for symbol in symbol_list:
            if len(symbol) != 1:
                return {'Длина всех символов должна быть равна 1':'Length of symbols should be equal 1'}
            elif self.black_string.count(symbol) == 1:
                return {f'Символ "{symbol}" состоит в черном списке!':f'Symbol "{symbol}" is in black list!'}
            elif self.symbolbet.count(symbol) > 0 or symbol_list.count(symbol) > 1:
                return {'Нельзя, чтобы было несколько символов в symbolbet':'Two or more similar symbols arent in symbolbet'}
            else:
                self.symbolbet += symbol
        return {'Символы успешно добавлены':'Symbols correctly added'}

    def delete_symbols(self, symbol_list):
        for e in symbol_list:
            if self.symbolbet.count(e) == 1:
                self.symbolbet = change_symbol(self.symbolbet, e, '')
        return 'Символы успешно удалены'

    def stay_symbols(self, symbol_list):
        for e in self.symbolbet:
            if symbol_list.count(e) == 0:
                self.symbolbet = change_symbol(self.symbolbet, e, '')
        return 'Указанные символы оставлены, остальные - успешно удалены'

    def add_black_symbols(self, list_of_symbols):
        for s in list_of_symbols:
            if self.black_string.count(s) > 0 or list_of_symbols.count(s) > 1:
                return 'Нельзя, чтобы было несколько символов в black string'
            else:
                self.symbolbet = change_symbol(self.symbolbet, s, '')
                self.black_string += s

    def delete_black_symbols(self, list_of_symbols):
        for s in list_of_symbols:
            self.black_string = change_symbol(self.black_string, s, '')
            self.symbolbet += s

    def get(self):
        return self.symbolbet

    def get_black(self):
        return self.black_string


class RangeLen:
    def __init__(self, min_len=10, max_len=20):
        self.min_len = int(min_len)
        self.max_len = int(max_len)

    def set(self, min_len=10, max_len=20):
        if not (min_len.isdigit() and max_len.isdigit()):
            return 'Являются ли ваши числа - числами?'
        elif min_len > max_len:
            return 'Первое число всегда меньше чем второе'
        else:
            self.min_len, self.max_len = int(min_len), int(max_len)
            return 'Диапазон успешно введен'

    def get_random(self):
        return r(self.min_len, self.max_len)

    def get(self):
        return [self.min_len, self.max_len]


class UI:
    def __init__(self):
        self.widget_list = []

    def set_dark(self):
        for element in self.widget_list:
            if type(element).__name__ == 'LabelFrame':
                element.config(fg='white', bg='gray10')
            elif type(element).__name__ == 'Frame':
                element.config(bg='gray10')
            elif type(element).__name__ == 'ClassicButton':
                element.config(fg='white', activeforeground='white', bg='gray21', activebackground='gray20')
            elif type(element).__name__ == 'ClassicLabel':
                element.config(fg='white', bg='gray10')
            elif type(element).__name__ == 'ClassicEntry':
                element.config(fg='white', bg='gray19', insertbackground='white')
            elif type(element).__name__ == 'ClassicRadioButton' and 'ClassicCheckButton':
                element.config(fg='white', activeforeground='white', bg='gray10', activebackground='gray10',
                               selectcolor='gray7')
            elif type(element).__name__ == 'EraseWidget':
                pass
        root.config(bg='gray10')

    def set_white(self):
        for element in self.widget_list:
            if type(element).__name__ == 'LabelFrame':
                element.config(fg='black', bg='gray94')
            elif type(element).__name__ == 'Frame':
                element.config(bg='gray94')
            elif type(element).__name__ == 'ClassicButton':
                element.config(fg='black', bg='gray94')
            elif type(element).__name__ == 'ClassicLabel':
                element.config(fg='black', bg='gray94')
            elif type(element).__name__ == 'ClassicEntry':
                element.config(fg='black', bg='white', insertbackground='black')
            elif type(element).__name__ == 'ClassicRadioButton' or 'ClassicCheckButton':
                element.config(fg='black', activeforeground='black', bg='gray94', activebackground='gray94', selectcolor='white')
        root.config(bg='gray94')





