import sqlite3, hashlib
from datetime import datetime



def con():
    return sqlite3.connect('baza.db')


def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            id integer not null primary key autoincrement,
            first_name varchar(30),
            last_name varchar(30),
            birth_day data,
            phone varchar(13),
            username varchar(50),
            password varchar(150),
            is_active boolean default false
        )
    """)
    conn.commit()
    conn.close()


def register(data:dict):
    sha256 = hashlib.sha256()
    sha256.update(data['password'].encode('utf-8'))
    data['password'] = sha256.hexdigest()
    query = """
        insert into user(
            first_name,
            last_name,
            birth_day,
            phone,
            username,
            password
        ) values (?,?,?,?,?,?)
    """
    values = (data['first_name'], data['last_name'], data['birth_day'], data['phone'], data['username'], data['password'], False)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    conn.close()


def create_table_courses():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists courses(
            id integer not null primary key autoincrement,
            course_name varchar(50),
            number_of_students int,
            is_active bolean default true
        )
    """)
    conn.commit()
    conn.close()


def insert_cours(data:dict):
    conn = con()
    cur = conn.cursor()
    query = """
        insert into courses(
            name,
            number_of_students
        ) values (?,?)
    """
    values = tuple(data.values())
    cur.execute(query, values)
    conn.commit()
    conn.close()


def create_table_add_students_course():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists sign_up_course(
            id integer not null primary key autoincrement,
            user_id integer,
            foreign key(user_id) references user(id),
            usernmae varchar(50),
            course_name varchar(30),
            register data
        )
    """)
    conn.commit()
    conn.close()


def insert_add_courses(data:dict):
    conn = con()
    cur = conn.cursor()
    query = """
        insert into sign_up_course(
            id integer not null primary key autoincrement,
            user_id,
            foreign key(user_id) reference user(id),
            username,
            course_name,
            register_time
        ) values (?,?,?,?,?)
    """
    values = (data['user_id'], data['username'], data['course_name'], datetime.now())
