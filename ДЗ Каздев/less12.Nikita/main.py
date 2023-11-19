import str_operation

#02 создать модуль для работы с текстовыми данными, создаль модуль "str_operation"
text = input('ВВедите любой текст: ')

print(f'Сумма слов в введеном текст равна {str_operation.sum_slov(text)}')
print(f'Количество символов в введеном текст равно {str_operation.sum_simbol(text)}')