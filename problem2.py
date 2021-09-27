colors = {
    "black": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,255,1],
    "hex": "#000"
    }
},
    "white": {
    "category": "value",
    "type": "primary",
    "code": {
    "rgba": [0,0,0,1],
    "hex": "#FFF"
    }
},
    "red": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,0,0,1],
    "hex": "#FF0"
    }
},
    "blue": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [0,0,255,1],
    "hex": "#00F"
    }
},
    "yellow": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,0,1],
    "hex": "#FF0"
    }
},
    "green": {
    "category": "hue",
    "type": "secondary",
    "code": {
    "rgba": [0,255,0,1],
    "hex": "#0F0"
    }
}
}
class Parser:
    def __init__(self, text):
        self.text = text

    def get_keys_tuple(self):
        inner_keys = list(self.text.keys())
        for i in colors:
            inner_keys+=list(self.text[i].keys())
            for j in self.text[i]:
                try:
                    inner_keys += list(self.text[i][j].keys())
                except AttributeError:
                    continue
        return tuple(set(inner_keys))


    def get_values_tuple(self):
        somedict1 = self.text.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    if j not in values:
                        values.append(j)
                try:
                    values+=list(j.values())
                except AttributeError:
                    continue
        return tuple(values)


    def get_keys_list(self):
        inner_keys = list(self.text.keys())
        for i in self.text:
            inner_keys += list(self.text[i].keys())
            for  j in self.text[i]:
                try:
                    inner_keys += list(self.text[i][j].keys())
                except AttributeError:
                    continue
        return list(set(inner_keys))


    def get_values_list(self):
        somedict1 = self.text.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    if j not in values:
                        values.append(j)
                try:
                    values += list(j.values())
                except AttributeError:
                    continue
        return values


    def get_keys_set(self):
        inner_keys = list(self.text.keys())
        for i in self.text:
            inner_keys += list(self.text[i].keys())
            for j in self.text[i]:
                try:
                    inner_keys += list(self.text[i][j].keys())
                except AttributeError:
                    continue
        return set(inner_keys)


    def get_values_set(self):
        somedict1 = self.text.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    values.append(j)
                try:
                    for q in j.values():
                        if type(q) == list:
                            values.append(tuple(q))
                        else:
                            values.append(q)
                except AttributeError:
                    continue
        return set(values)

my_class = Parser(colors)
data = {
    1:my_class.get_keys_tuple(),
    2:my_class.get_values_tuple(),
    3:my_class.get_keys_list(),
    4:my_class.get_values_list(),
    5:my_class.get_keys_set(),
    6:my_class.get_values_set(),
}
while True:
    print('''1. Получить все ключи в TUPLE.
2. Получить все значения в TUPLE.
3. Получить все ключи в LIST.
4. Получить все значения в LIST.
5. Получить все ключи в SET.
6. Получить все значения в SET.
0. Выход.
    ''')

    exit = int(input('Выберите действие - '))
    if exit == 0:
        break
    for i in data[exit]:
        print(i)