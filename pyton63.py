class Human:
    def __init__(self, n='Иван', age=0):
        #  Спец. методы. Поле класса, имеет self и принадлежит класcу, члены класса
        self.name = n
        self.age = age
        self.non_legal_names = ['Васек', 'Чертило']

    # Метод класса геттер
    def info(self):
        print(f'Этого человека зовут {self.name}')
        print('Его возраст', self.age)

    # Метод класса setter
    def set_age(self, new_age):
        if new_age < 0:
            self.age = -new_age
        else:
            self.age = new_age

        # Метод класса

    def set_name(self, n):
        if n not in self.non_legal_names:
            self.name = n
        else:
            self.name = 'Не пиши такое имя'


human1 = Human()  # ball1- экземпляр класса Ball #1
# human2 = Human ('Саша', 18)  # ball1- экземпляр класса Ball #1
# human3 = Human ()

human1.set_name('Папуля')
# human2.info()
# human3.info()
