with open('file1.txt', 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)

c = input('Додати цитату?')
if c == 'так':
    q = input('Введфть цитату:')
    b = input('Введіть автора: ')
    with open('file1.txt', 'a', encoding = 'utf-8') as file:
        file.write('\n'+q+'\n')
        file.write('\n'+b+'\n')
else:
    pass

with open('file1.txt', 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)




