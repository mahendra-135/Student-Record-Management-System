file_name='Management.py'

def add_student():
    name=input('enter a name')
    roll_no=input('enter a roll_num')
    course=input('enter a course')
    with open(file_name,'a')as file:
        file.write(f'{name},{roll_no},{course}n')
        print('student addded successfully')
def view_students():
    with open(file_name,'r')as file:
        view_students=file.readlineas()
        for student in view_students:
            name,roll_no,course=student.strip().split(',')
            print(f'Name:{name},{roll_no},course:{course}')
def search_students():
    roll_no=input('enter roll no to search')
    with open(file_name,'r')as file:
        view_students=file.readlineas()
        for student in view_students:
            name,roll_no,course=student.strip().split(',')
            print(f'Name:{name},{roll_no},course:{course}')
            return
        print('student not found')
while True:
    if __name__=='__main__':
        print('student Management system')
        print('1.add_student')
        print('2.view_students')
        print('3.search_students')
        print('4,exit')
        chose=input('enter your choice')
        if chose=='1':
            add_student()
        elif chose=='2':
            view_students()
        elif chose=='3':
            search_students()
        elif chose=='4':
            break
        else:
            print('invalid choice')