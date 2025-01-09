from curses.ascii import controlnames


class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.__phone_name=phone_number
        self.__email=email
        self.__addr=addr

    def print_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.__phone_name)
        print("이메일 : ", self.__email)
        print("주소 : ", self.__addr)
        print("---------------")
def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 전체 출력')
    print('3. 연락처 출력')
    print('4. 연락처 삭제')
    print('5. 종료')
    menu=input('메뉴선택:')
    print()
    return int(menu)

def set_contact():
    name = input("이름 : ")
    number = input("전화번호 : ")
    mail = input("이메일 : ")
    address = input("주소 : ")

    # info = [name, number, mail, address]
    info = Contact(name, number, mail, address)

    return info

def print_allContract(contact_list):
    for i in contact_list:
        i.print_info()
        print()

def print_contact(contact_list):
    for i in contact_list:
        print(i.name)

    search = input("이름 : ")

    for j in contact_list:
        # if search in j[0]:
        #     Contact(j[0], j[1], j[2], j[3]).print_info()
        if search in j.name:
            j.print_info()

def delete_contact(contact_list, name):
    # cList = []

    for i in contact_list:
        if str(name) in i:
            # contact_list.append(i)
            contact_list.remove(i)

    # return cList

def run():
    contact_list = []

    while True:

        menu=print_menu()

        if menu == 5:
            break

        elif menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        elif menu == 2:
            print_allContract(contact_list)
        elif menu == 3:
            print_contact(contact_list)

        elif menu == 4:
            name = input('삭제할 이름은?')
            # delete = delete_contact(contact_list,name)
            delete_contact(contact_list,name)

        # contact_list.sort()

# if __name__ == "__main__":
#     run()