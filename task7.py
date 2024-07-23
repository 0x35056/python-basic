class Animal:
    instances_count = 0

    def __init__(self):
        Animal.instances_count += 1

    def voice(self):
        pass

    @staticmethod
    def get_instances_count():
        return Animal.instances_count

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

print("Количество созданных экземпляров:", Animal.get_instances_count())