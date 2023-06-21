def ShowData(namePhoneBook):
    with open(namePhoneBook, 'r', encoding='utf-8') as data:
        print(data.read(), end ='\n')

def AddData(namePhoneBook):
    with open(namePhoneBook, 'a', encoding='utf-8') as data:
        temp = input('Введите ФИО и номер телефона: ')
        data.write(temp)

def FindData(namePhoneBook):
    with open(namePhoneBook, 'r', encoding='utf-8') as f:
        temp = f.read()
    findList = SearchData(temp)
    return findList

def ChangeData(namePhoneBook):
    with open(namePhoneBook, 'r', encoding='utf-8') as data:
        temp = data.read()
    tempLines = temp.split('\n')
    targetline = SearchChangeLine(namePhoneBook)
    while len(targetline) == 0:
        targetline = SearchChangeLine(namePhoneBook)
    changeLine = ChangeLine(targetline)
    tempLines[tempLines.index(targetline)] = changeLine
    print(f'Запись - {targetline}, изменена на - {changeLine}')
    with open(namePhoneBook, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tempLines))

def DeleteData(namePhoneBook):
    with open(namePhoneBook, 'r', encoding='utf-8') as data:
        temp = data.read()
    tempLines = temp.split('\n')
    findList = FindData(namePhoneBook)
    while len(findList) == 0:
        findList = FindData(namePhoneBook)
    if len(findList) > 0:
        print('Найдены записи:')
        for index in range(len(findList)):
            print(f'{index + 1} - {findList[index]}')
        indexDelline = int(
            input('Введите номер строки для удаления, или 0 для удаления всех найденных строк: ')) - 1
        if 0 <= indexDelline < len(findList):
            print(f'Удалена запись: {findList[indexDelline]}')
            tempLines.pop(tempLines.index(findList[indexDelline]))
        elif indexDelline == -1:
            for index in findList:
                tempLines.pop(tempLines.index(index))
            print(f'Удалено записей: {len(findList)}')
        else:
            print('Удалено записей: 0')
    with open(namePhoneBook, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tempLines))

def SearchData(namePhoneBook):
    searchLine = input('Введите ФИО или номер для поиска: ')
    namePhoneBook = namePhoneBook.split('\n')
    result = []
    for i in namePhoneBook:
        if searchLine in i:
            result.append(i)
    return result

def SearchChangeLine(filename: str):
    findList = FindData(filename)
    if len(findList) > 1:
        print('Найдены записи:')
        for index in range(len(findList)):
            print(f'{index + 1} - {findList[index]}')
        index = int(input('Введите номер записи для редактирования: ')) - 1
        print(f'Для редактирования выбрана запись - {findList[index]}')
        return findList[index]
    elif len(findList) == 1:
        print(f'Для редактирования выбрана запись - {findList[0]}')
        return findList[0]
    else:
        print('Поиск не дал результатов.')
        return ''
    
def ChangeLine(line):
    temp = line.split()
    info = input('Введите ФИО и номер телефона: ')
    if len(info) == 0:
        info = temp[0]
    return info

while True:
    print('Добро пожаловать в телефонный справочник!')
    action = int(input('Какое действие хотите совершить:\n 1 - Просмотр данных\n 2 - Добавление данных\n 3 - Поиск данных\n 4 - Изменение данных\n 5 - Удаление данных\n'))
    namePhoneBook = 'phonebook.txt'
    with open(namePhoneBook, 'a', encoding='utf-8') as file:
        file.write('')
    if action == 1:
        ShowData(namePhoneBook)
    elif action == 2:
        AddData(namePhoneBook)
    elif action == 3:
        print(FindData(namePhoneBook))
    elif action == 4:
        ChangeData(namePhoneBook)
    elif action == 5:
        DeleteData(namePhoneBook)
    else:
        print('Вы выбрали неверное действие')
    print('')

 