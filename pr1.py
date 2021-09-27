class Nout:
    def __init__(self, name, cpu, ram, gpu, hdd, mb, size):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.hdd = hdd
        self.mb = mb
        self.size = size
    def check_nout(self):
        print(f'''
'Название ноутбука': {self.name},
'Процессор': {self.cpu},
'Оперативная память': {self.ram},
'Видеокарта': {self.gpu},
'Жесткий диск': {self.hdd},
'Материнская плата': {self.mb},
'Размер экрана': {self.size}
 ''')
note1 = Nout('Legion', 'Amd ryzen5', '16gb', '1660ti', '512gb', 'none', 15.6)
note1.check_nout()