# -*- coding: utf-8 -*-

"""
Перепишите первые 100 байтов одного бинарного файла в другой, ничего не меняя. Если в файле байтов меньше 100, то перепишите все.

Формат ввода
В файле data.bin находятся бинарные данные.

Формат вывода
Запишите часть исходного файла в файл part.dat.

"""



# это просто тест. Если файла data.bin нет, создадим его,
# и положим в него текст в однобайтовой кодировке,
# чтоб на каждый символ получился строго 1 байт

# can you explain why is this code giving different results on Linux and Windows? 
# on linux it is writing cyr symbols, on windows they disappear

import os
fname_in = r'data.bin'
text = u'ЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеж1234'

if not os.path.exists(fname_in):
    with open(fname_in, mode='w', errors='strict', encoding='utf-8') as f:
        print(text, file=f)
        

# Открываем файл для чтения в бинарном режиме (rb). Кодировка не нужна
with open(fname_in, mode='rb') as f:
    data = f.read() 

print(data) # получились байты
print(data.decode('cp1251'))

fname_out = r'part.dat'
# Открываем файл для ЗАПИСИ в бинарном режиме (wb) 
with open(fname_out, mode='wb') as f:
    f.write(data[:10])
    
# и прочитаем, что записали
with open(fname_out, mode='r', encoding='CP1251') as f:
    print(f.read())
    

# "asdf"
# f"asdf"
# f"""asdf{asdf}"""

# 'asdf'
# f'asdf'
# f'''asdf{asdf}'''

class Abyrvalg(str):
