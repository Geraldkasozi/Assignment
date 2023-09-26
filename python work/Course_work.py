class University():
    
    course = ''
    lecturer = ''
    student = ''

    def Student(self):
       print(f'Am by names of {self.student}')

    def Course(self):
        print(f'I major in {self.course} ')

    def Lecture(self):
        print(f'My lecture is called {self.lecturer} and he teaches OOP')

my_project = University()
my_project.student = 'KASOZI GERALD'
my_project.course = 'BSIT'
my_project.lecturer =  'MR.BRIAN KASOZI'

my_project.Student()
my_project.Course()
my_project.Lecture()