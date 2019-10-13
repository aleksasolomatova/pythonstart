#задание 1
import math

class Triangle:

    def __init__(self, f, t, p):
        self.f = f
        self.t = t
        self.p = p

        def length(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        self.ft = length(self.f, self.t)
        self.tp = length(self.t, self.p)
        self.fp = length(self.f, self.p)

    def perimeter(self):
        return (self.ft + self.tp + self.fp)

    def area(self):
        p = (self.ft + self.tp + self.fp) / 2
        return math.sqrt(p * (p - self.fp) * (p - self.ft) * (p - self.tp))

    def height(self):
        return self.area() / (self.ft / 2)

objectTriangle = Triangle((1, 3), (2, -5), (-8, 4))
print(objectTriangle.height())
print(objectTriangle.area())

#задание2
class Trapeze:
    def __init__(self, A1, A2, A3, A4):
        self.A = A1
        self.B = A2
        self.C = A3
        self.D = A4

        def sideLen(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2
            return math.sqrt(semi_perimeter * (semi_perimeter - len1) * (semi_perimeter - len2) * (semi_perimeter - len3))

        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)

        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) + areaTriangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapeze(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False

#задание3

class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())

class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class

class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject


class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}


if __name__ == '__main__':
    teachers = [Teacher('Денис', 'Юрьевич', 'Усов', 'География'),
                Teacher('Михаил', 'Петрович', 'Шилюк', 'Физика'),
                Teacher('Эдуард', 'Михайлович','Перепечай','История'),
                Teacher('Александр', 'Александрович', 'Греков', 'Физическая культура'),
                Teacher('Никита', 'Владимирович', 'Гурылев', 'Математика')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Алексей', 'Викторович', 'Соломатов'),
               People('Юлия', 'Владимировна', 'Соломатова'),
               People('Константин', 'Романович', 'Романов'),
               People('Роза', 'Петровна', 'Романова'),
               People('Сергей', 'Владимирович', 'Черняев'),
               People('Татьяна', 'Викторовна', 'Черняева')]
    students = [Student('Игорь', 'Алексеевич', 'Соломатов', parents[0], parents[1], classes[0]),
                Student('Юлия', 'Константиновна', 'Романова', parents[2], parents[3], classes[1]),
                Student('Арсений', 'Сергеевич', 'Черняев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)

    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())

