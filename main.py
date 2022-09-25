class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail


class Contacts:
    def __init__(self):
        self.bd = [[], [], [], [], [], []]
        #  id=0  фамилия=1 имя=2 отчество=3 номер=4 почта=5

    def __add__(self, contact):
        self.bd[0].append(len(self.bd[0]) + 1)
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.bd[1].append(fio[0])
        self.bd[2].append(fio[1])
        self.bd[3].append(fio[2])
        if contact.phone != '':
            self.bd[4].append(contact.phone)
        else:
            self.bd[4].append(None)
        if contact.mail != '':
            self.bd[5].append(contact.mail)
        else:
            self.bd[5].append(None)

    def Contacts(self, id):
        an = "ID - " + str(self.bd[0][id]) + "\n"
        if self.bd[1][id] != None:
            an += "ФИО: " + self.bd[1][id]
        if self.bd[2][id] != None:
            an += " " + self.bd[2][id]
        if self.bd[3][id] != None:
            an += " " + self.bd[3][id]
        if self.bd[4][id] != None:
            an += "\n" + "Номер телефона: " + self.bd[4][id]
        else:
            an += "\n" + "Номер телефона: " + "None"
        if self.bd[5][id] != None:
            an += "\n" + "Почта: " + self.bd[5][id] + "\n"
        else:
            an += "\n" + "Почта: " + "None" + "\n"
        return an

    def phoneSearch(self, phone):
        if self.bd[4].__contains__(phone):
            id = self.bd[4].index(phone)
            print(self.Contacts(id))
        else:
            print("Ничего не найдено")

    def mailSearch(self, mail):
        if self.bd[5].__contains__(mail):
            id = self.bd[5].index(mail)
            print(self.Contacts(id))
        else:
            print("Ничего не найдено")

    def search(self, fio):
        ils = []
        if fio[0] != None:
            for i in range(len(self.bd[1])):
                if fio[0] == self.bd[1][i]:
                    ils.append(self.bd[0][i] - 1)
        if fio[1] != None:
            if fio[0] != None:
                for id in ils:
                    if fio[1] != self.bd[2][id]:
                        ils.remove(id)
            else:
                for i in range(len(self.bd[2])):
                    if fio[1] == self.bd[2][i]:
                        ils.append(self.bd[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in ids:
                    if fio[2] != self.bd[2][id]:
                        ils.remove(id)
            else:
                for i in range(len(self.bd[3])):
                    if fio[2] == self.bd[3][i]:
                        ils.append(self.bd[0][i] - 1)

        if len(ils) == 0:
            print("Ничего не найдено")
        else:
            for id in ils:
                print(self.Contacts(id))

    def getWithoutPhoneOrMail(self, num):
        # 1 без номера, 2 без почты, 3 без обоих
        if num == 1:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None:
                    print(self.Contacts(i))
            return
        if num == 2:
            for i in range(len(self.bd[5])):
                if self.bd[5][i] == None:
                    print(self.Contacts(i))
            return
        if num == 3:
            for i in range(len(self.bd[4])):
                if self.bd[4][i] == None and self.bd[5][i] == None:
                    print(self.Contacts(i))
            return

    def change(self, id, contact):
        id -= 1
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.bd[1][id] = fio[0]
        self.bd[2][id] = fio[1]
        self.bd[3][id] = fio[2]
        if len(contact.phone) > 0:
            self.bd[4][id] = contact.phone
        else:
            self.bd[4][id] = None
        if len(contact.mail) > 0:
            self.bd[5][id] = contact.mail
        else:
            self.bd[5][id] = None

    def printAll(self):
        for i in range(len(self.bd[0])):
            print(self.Contacts(i))

def printCommands():
    print("Список доступных команд: ")
    print("1 - Вывести все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")


print("Введите название файла")
fileName = input()
file = open(fileName, encoding='utf-8')
base = Contacts()
for strok in file:
    arr = strok.split(",")
    print (arr)
    contact = Contact(arr[0],arr[1].replace(" ",""),arr[2].replace(" ","").replace("\n",""))
    base.__add__(contact)
print("База сформирована")
printCommands()
rty = int(input())
while rty!="akdna@@@kdn":
    if rty==1:
        base.printAll()
    elif rty==2:
        print("Введите телефон")
        phone = input()
        base.phoneSearch(phone)
    elif rty == 3:
        print("Введите почту")
        mail = input()
        base.mailSearch(mail)
    elif rty == 4:
        fio = []
        print("Введите фамилию, либо оставьте пустую строку")
        f = input()
        if f=='':
            fio.append(None)
        else:
            fio.append(f)
        print("Введите имя, либо оставьте пустую строку")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Введите отчество, либо оставьте пустую строку")
        o = input()
        if o == '':
            fio.append(None)
        else:
            fio.append(o)
        base.search(fio)
    elif rty == 5:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        base.getWithoutPhoneOrMail(num)
    elif rty == 6:
        print("Введите id контакта, который хотите изменить и новые данные для него", "(в две разные строки)", sep="\n")
        id = int(input())
        q = input().split(",")
        contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        base.change(id, contact)
    elif rty == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    rty = int(input())