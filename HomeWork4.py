#Создать класс Student: id, Фамилия, Имя, Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс,#
#Группа. Функции-члены реализуют запись и считывание полей (проверка корректности), расчет
#возраста студента Создать список объектов. Вывести:
#a) список студентов заданного факультета;
#d) список учебной группы.
class Student:
    __idStud = 0
    __surnameStud = ' '
    __nameStud = ' '
    __middlenameStud = ' '
    __datebirthStud = 0
    __addressStud = ' '
    __phoneStud = 0
    __facultyStud = ' '
    __courseStud = 0
    __groupStud = 0

    def __init__(self,idStud0,surnameStud0,nameStud0,middlenameStud0,datebirthStud0,addressStud0,
                 phoneStud0,facultyStud0,courseStud0,groupStud0):
        self.__idStud = idStud0
        self.__surnameStud = surnameStud0
        self.__nameStud = nameStud0
        self.__middlenameStud = middlenameStud0
        self.__datebirthStud = datebirthStud0
        self.__addressStud = addressStud0
        self.__phoneStud = phoneStud0
        self.__facultyStud = facultyStud0
        self.__courseStud = courseStud0
        self.__groupStud = groupStud0
        print('New object created!')

    def get_idStud(self):
        return self.__idStud
    def get_surnameStud(self):
        return self.__surnameStud
    def get_middlenameStud(self):
        return self.__middlenameStud
    def get_datebirthStud(self):
        return self.__datebirthStud
    def get_addressStud(self):
        return self.__addressStud
    def get_phoneStud(self):
        return self.__phoneStud
    def get_facultyStud(self):
        return self.__facultyStud
    def get_courseStud(self):
        return self.__courseStud
    def get_groupStud(self):
        return self.__groupStud

    def StudAge(self, currYear=2020):
        return currYear - self.get_datebirthStud()

def StudInfoOut(i):

    print( 'Stud id : ' + str(StudInfo[i].get_idStud()))
    print ('Stud name : ' +StudInfo[i].get_surnameStud())
    print ('Stud middlename : ' + StudInfo[i].get_middlenameStud())
    print (str(StudInfo[i].StudAge()) + ' years old ')
    print ('Faculty : ' + StudInfo[i].get_facultyStud())
    print ('Course : ' + str(StudInfo[i].get_courseStud()))
    print ('Group : ' + str(StudInfo[i].get_groupStud()))
i=0
StudInfo=[Student(1 , 'Kopat', 'Svetlana ' , 'Igorevna' , 1999 , 'Grodno' , 22334456 , 'FITU', 3 ,720604),
          Student(2,'Plashko' , 'Sasha' , 'Nikolaevich' , 1998,'Brest' , 45775466 , 'FKP' , 3 , 720601),
          Student(3 , 'Tihonovich' , 'Aleksandra','Maksimovna' , 2000, 'Minsk',4565543 ,'FITU',3,720601 ),
          Student(4, 'Tkachuk','Alecksey','Viktorovich' , 2000 ,'Baranovichi' , 6758493,'FITU',2,720601),
          Student(5,'Malash','Anastasia','Viktoronna',1999,'Minsk',23456,'IEF',2,920597),
          Student(6,'Belaya','Karyna','Anatoylevna',1998,'Globin',654536347,'IEF',4,567301)]

faculty = ' '
group = 0
faculty = str(input('Input faculty \n'))
while i < len(StudInfo):
    if StudInfo[i].get_facultyStud() == faculty:
        StudInfoOut(i)
    i+=1
i=0
group = int(input('Input group \n'))
while i < len(StudInfo):
    if StudInfo[i].get_groupStud() == group:
        StudInfoOut(i)
    i+=1

