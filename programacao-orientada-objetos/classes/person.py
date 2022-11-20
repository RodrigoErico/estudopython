class Person:
    def __init__(self, name, age, reading=False, writing=False):
        self.name = name
        self.age = age
        self.reading = reading
        self.writing = writing

    def is_reading(self):
        print(f'{self.name} is reading.')
        self.reading = True
