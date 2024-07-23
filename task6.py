class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print("Гав")

class Cat(Animal):
    def voice(self):
        print("Мяу")

class Bird(Animal):
    def voice(self):
        print("Чирик")

# Создание экземпляров
dog = Dog()
cat = Cat()
bird = Bird()

# Вызов метода voice() для каждого экземпляра
dog.voice()
cat.voice()
bird.voice()