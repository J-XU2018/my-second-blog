from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=200, unique=True)
    points = CharField(max_length=100)

    class Meta:
        database=db

students = [{'username': 'Katie', 'points':123},
            {'username': 'Laura', 'points':100},
            {'username': 'Jack', 'points':99}
            ]
def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            # pass, when student already in table, should update it's points
            student_record = Student.get(username=student['username'])
            if student_record.points != student['points']:
                student_record.points = student['points']
                student_record.save()

def top_student():
    # handy way to use sql to get the ordered object,
    # i was thinking to get all, and for loop to find the toppest one,
    student = Student.select().order_by(Student.points.desc()).get()
    # get() get the first one
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("The top student right now is {0.username}".format(top_student()))
    #tricky to use 0.username
