
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr
    def print_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone_name)
        print("이메일 : ", self.email)
        print("주소 : ", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    name = input("이름 : ")
    number = input("전화번호 : ")
    mail = input("이메일 : ")
    address = input("주소 : ")
    info = [name, number, mail, address]
    return info

def print_contact(contact_list):
    # 여기에 코드 작성
    for i in contact_list:
        print(i[0])
    search = input("이름 : ")
    for j in contact_list:
        if search in j[0]:
            print(f"이름 : {j[0]}")
            print(f"전화번호 : {j[1]}")
            print(f"이메일 : {j[2]}")
            print(f"주소 : {j[3]}")

def delete_contact(contact_list, name):
    # 여기에 코드 작성
    cList = []
    for i in contact_list:
        if str(name) not in i[0]:
            cList.append(i)
    return cList

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete = delete_contact(contact_list,name)
            contact_list = delete
        # contact_list.sort()

if __name__ == "__main__":
    run()