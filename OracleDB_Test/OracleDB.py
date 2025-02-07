import cx_Oracle as oci


oci.init_oracle_client(r"/Users/guryena/Oracle/instantclient_23_3")
##conn = cx_Oracle.connect('system/oracle@localhost:1521/xe')
##print(conn.version)
# Oracle 데이터베이스에 접속
#dsn = cx_Oracle.makedsn(host='192.168.0.127', port='1521', sid='aidb')
#connection = cx_Oracle.connect(user='ejo', password='ejo', dsn=dsn)
dsn = oci.makedsn(host='localhost', port='1521', sid='xe')
connection = oci.connect(user='scott', password='tiger', dsn=dsn)
address = 'scott/tiger@localhost:1521/xe'
# 커넥션 상태 확인
if connection:
    print("Oracle DB 연결 성공")
else:
    print("Oracle DB 연결 실패")
    exit(100)

# 접속된 데이터베이스에서 쿼리 실행
#cursor = connection.cursor()
#cursor.execute("SELECT * FROM CART")
#result = cursor.fetchall()

# 쿼리 결과 출력
#for row in result:
 #   print(row)

def insert_emp():
    try:

        connection = oci.connect(address)
        cursor = connection.cursor()
        # 정보(사번, 이름 등) 입력 받아 insert
        empno = int(input('empno->'))
        ename = input('name->')
        job = input('job->')
        sal = int(input('sal->'))

        # DB에 입력
        sql = """
        INSERT INTO emp (empno, ename, job, sal)
        values(:1, :2, :3, :4)
        """
        cursor.execute(sql, (empno, ename, job, sal))
        connection.commit()
        print("Insert EMP info Complete")
    except oci.DatabaseError as e:
        error, = e.args
        print('Error: ', error.message)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# 사원정보 출력
def print_emp():
    try :
        connection = oci.connect(address)
        cursor = connection.cursor()
        sql = """
            SELECT * FROM emp ORDER BY empno
        """
        cursor.execute(sql)
        datas = cursor.fetchall()
        for row in datas:
            print(row)

    except oci.DatabaseError as e:
        error, = e.args
        print('Error: ', error.message)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# 사원정보 삭제
def delete_emp():
    try :
        connection = oci.connect(address)
        cursor = connection.cursor()
        ename = input('Delete Name : ')
        sql = """
            DELETE FROM emp WHERE ename = :1
        """

        cursor.execute(sql, (ename,))
        connection.commit()
        print("Delete " + ename)

    except oci.DatabaseError as e:
        error, = e.args
        print('Error: ', error.message)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



# 사원정보 변경 (사번, 직책, 급여)
def change_emp():
    try :
        connection = oci.connect(address)
        cursor = connection.cursor()
        empno = int(input('Choose EMP NO : '))
        job = input('Change Job : ')
        sal = float(input('Change sal : '))

        sql = """
            UPDATE emp 
            SET job = :2, sal = :3 
            WHERE empno = :1
        """
        cursor.execute(sql, (empno, job, sal))
        connection.commit()

        print("Update Complete")

    except oci.DatabaseError as e:
        error, = e.args
        print('Error: ', error.message)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()




# 사용자에게 입력/출력/삭제/변경의 선택을 받아서 DB에 접근하여 처리
def show_menu():
    while True:

        #sql = ('SELECT * FROM emp ORDER BY empno DESC')

        #cursor.execute(sql)
        #datas = cursor.fetchall()
        #for i in range(10):
        #   print(datas[i])

        print('\n1. EmpNO. insert')
        print('2. EmpInfo select')
        print('3. EmpInfo delete')
        print('4. EmpInfo update')
        print('5. System EXIT')
        choice = input('Menu : ')

        if choice == '1':
            insert_emp()
        elif choice == '2':
            print_emp()
        elif choice == '3':
            delete_emp()
        elif choice == '4':
            change_emp()
        elif choice == '5':
            print('System EXIT.')
            break


# 프로그램 시작 함수
def main():
    show_menu()


if __name__ == '__main__':
    main()
