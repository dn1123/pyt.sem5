def compress_string(line):
    new_string = ""
    count = 1     # счетчик символов
    # начинаем выполнение
    for i in range(len(line)):
        j = i
        j += 1
        try:
            if line[i] == line[j]:
                count += 1
            else:
                # иначе добавим текущий символ
                new_string += line[i]
                new_string += str(count)
                count = 1
        except:
            # последний индекс значения i
            new_string += line[i]
            j = i
            j -= 1
            if line[i] == line[j]:
                new_string += str(count)
            else:
                new_string += '1'
    # return
    if len(new_string) > len(line):
        print(line)
    else:
        print(new_string)

# string = input('Введите строку с повторяющимися иероглифами:\n')
# compress_string(string)

t = open('file1.txt', encoding='UTF-8')
print('Сжимаем текст из файла: ')
compress_string(t.read())
t.close()

t = open('file2.txt', 'w', encoding='UTF-8')
t.write('a3b4D5ы7*5$6ж7@5г2+8й1')
t.close()

# раскодируем текст

def recover_string(line):
    result = ''

    for i in range(0, len(line), 2):
        num = line[i]
        run_length = int(line[i+1])
        for j in range(run_length):
            result += num
    return result

# crypto = input('Введите зашифрованный текст:\n')
# print(recover_string(crypto))

z = open('file2.txt', encoding='UTF-8')
print(F'Раскодируем текст из файла: \n{recover_string(z.read())}')
print(recover_string(z.read()))
z.close()