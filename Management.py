file_name = 'students.txt'

def add_student():
    name = input('Enter name: ')
    roll_no = input('Enter roll number: ')
    course = input('Enter course: ')

    with open(file_name, 'a') as file:
        file.write(f'{name},{roll_no},{course}\n')

    print('Student added successfully')


def view_students():
    try:
        with open(file_name, 'r') as file:
            students = file.readlines()
            if not students:
                print("No records found")
                return

            for student in students:
                name, roll_no, course = student.strip().split(',')
                print(f'Name: {name}, Roll No: {roll_no}, Course: {course}')
    except FileNotFoundError:
        print("No records found")


def search_students():
    search_roll = input('Enter roll number to search: ')

    try:
        with open(file_name, 'r') as file:
            students = file.readlines()
            for student in students:
                name, roll_no, course = student.strip().split(',')
                if roll_no == search_roll:
                    print(f'Name: {name}, Roll No: {roll_no}, Course: {course}')
                    return

            print('Student not found')
    except FileNotFoundError:
        print("No records found")


if __name__ == '__main__':
    while True:
        print('\nStudent Management System')
        print('1. Add Student')
        print('2. View Students')
        print('3. Search Student')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_students()
        elif choice == '4':
            break
        else:
            print('Invalid choice')
