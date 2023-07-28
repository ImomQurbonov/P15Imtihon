from database import create_table_user, register, create_table_courses, create_table_add_students_course
from utilis import login, login_admin, active_courses, students_courses
create_table_user()
create_table_courses()
# create_table_add_students_course()


def start():
    while True:
        print("Xush kelibsiz")
        print("1.Adminstrator\n2. Foydalanuvchi")
        n = int(input('bo\'imni tanlang >>> '))
        if n == 1:
            def retry_login():
                username = input('usernam kiriting >>> ')
                password = input('Password kiriting >>> ')
                if login_admin(username, password):
                    print('1. Kurs qo\'shish\n2. Kurslardagi o\'quvchilar ro\'yxati')
                    b = int(input('>>> '))
                    if b == 1:
                        data = dict(
                            course_name = input('Kurs nomi >>> '),
                            number_of_students = input('O\'quvchilar sig\'imi >>> ')
                        )
                        insert_cours(data)
                        print('Success ')
                    elif b == 2:
                        students_courses()
                else:
                    return retry_login()
            retry_login()
        elif n == 2:
            print('1. Ro\'yxatdan o\'tish\n2. Kirish\n0. Dasturdan chiqb ketish')
            a = int(input('>>> '))
            if a == 1:
                def retry():
                    first_name = input('Ismingiz >>> '),
                    last_name = input('Familiyangiz >>> '),
                    birth_day = input('Tug\'ilgan sana(YYYY-OO-KK)>>> '),
                    phone = input('Telefon raqamingiz(+99801234567) >>> '),
                    username = input('Username >>> '),
                    password1 = input('Password >>> ')
                    password2 = input('Password confirm >>> ')
                    if password1 == password2:
                        data = dict(first_name=first_name, last_name=last_name,birth_day=birth_day,phone=phone,username=username,password=password2)
                        register(data)
                        print('Success')
                    else:
                        print('ERROR password !!!')
                        return retry()
                retry()
            elif a == 2:
                def retry_user():
                    username = input('Username kiriting >>> ')
                    password = input('Password kiriting >>> ')
                    if login(username, password):
                        print('1. Aktiv kurslarga yozilish\n2. Yozilgan kurslar ro\'yxati')
                        c = int(input('>>> '))
                        if c == 1:
                            active_courses()
                            d = int(input('Yo\'nalish ID sini kiriting >>> '))
                            data = dict(
                                username=username,

                            )
                    else:
                        return retry_user()
                retry_user()

        else:
            print('Mavjud bo\'lmagan bo\'limni tanladingiz !')
            return start()

start()
