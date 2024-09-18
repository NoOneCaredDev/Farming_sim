from random import randint


class Interface:
    def __init__(self, animal: str, ready: bool, hunger: float, thirst: float):
        self.animal = animal
        self.ready = ready
        self.hunger = hunger
        self.thirst = thirst

    def drink(self):
        self.thirst += 1
        print('Вы напоили животное')
        if self.thirst >= 2:
            print(f'Вы переполнили желудок. {self.animal} не успело в свой туалет..')

    def feed(self):
        self.hunger += 1
        print('Вы накормили животное')
        if self.hunger >= 2:
            print(f'Вы перекормили животное. {self.animal} не успело в свой туалет..')

    def special(self):
        if self.ready:
            match self.animal:
                case 'cow':
                    print('Вы успешно подоили корову')
                case 'sheep':
                    print('Вы успешно постригли овцу')
                case 'dog':
                    print('Вы успешно погоняли овец собакой')
                case 'pig':
                    print('Вы успешно помыли свинку в грязи')
                case 'chicken':
                    print('Вы успешно собрали яица')
            self.ready = False
        else:
            print('Животное ещё не готово.')
        

    def info(any):
        print(f"----the {any.animal} interface----")
        print(f"-Hunger: {any.hunger}-")
        print(f"-Thirst: {any.thirst}-")
        print("-----SPECIAL CHARACTERISTICS-----")
        if any.animal == 'cow':
            if any.ready:
                print(f"{any.animal} is ready to get milked!")
            else:
                print(f"{any.animal} isn't ready to get milked, please wait~!")
        if any.animal == 'sheep':
            if any.ready:
                print(f"{any.animal} is ready to get tonsured!")
            else:
                print(f"{any.animal} isn't ready to get tonsured, please wait~!")
        if any.animal == 'dog':
            if any.ready:
                print(f"{any.animal} is ready!")
            else:
                print(f"{any.animal} is tired, please wait~!")
        if any.animal == 'pig':
            if any.ready:
                print(f"{any.animal} is ready to wash in the dirt!")
            else:
                print(f"{any.animal} don't want this right now, please wait~!")
        if any.animal == 'chicken':
            if any.ready:
                print(f"{any.animal} does eggs!")
            else:
                print(f"{any.animal} isn't ready to poop with eggs, please wait~!")
        print("-----AVAILABLE COMMANDS-----\n-Tip water\n-Tip food\n-Do special command")

    def doing(self):
        while True:
            self.info()
            choice = int(input(f'Выберите действие, которое хотите сделать над {self.animal} (water 1/food 2/special command 3): ' ))
            match choice:
                case 1:
                    self.drink()
                case 2:
                    self.feed()
                case 3:
                    self.special()
            if input('Хотите закончить с этим животным? yes/no ') == 'yes':
                break

            
            


a_cow = Interface('cow', False, 0.5, 0.7)
a_sheep = Interface('sheep', True, 0.1, 0.9)
a_dog = Interface('dog', False, 0.4, 0.6)
a_pig = Interface('pig', False, 0.2, 0.3)
a_chicken = Interface('chicken', True, 0.8, 0.5)
list = ['cow', 'sheep', 'dog', 'pig', 'chicken']
choise = 0
count = 0

def day():
    global count
    count = count + 1
    while True:
        while True:
            animall = input(f'День {count}, \nВыберите животное (cow, sheep, dog, pig, chicken): ')
            if animall in list:
                break
            else:
                print("Нет такого животного!!")
        match animall:
            case 'cow':
                a_cow.doing()
            case 'sheep':
                a_sheep.doing()
            case 'dog':
                a_dog.doing()
            case 'pig':
                a_pig.doing()
            case 'chicken':
                a_chicken.doing()
        if input('Вы хотите законичить сегодняшний день? yes/no ') == 'yes':
            break
    for i in (a_chicken, a_cow, a_dog, a_pig, a_sheep):
        i.thirst = i.thirst -0.4
        i.hunger = i.thirst -0.4
        if randint(0,1):
            i.ready = True

while True:
    day()
    a = input('Играем дальше?  (yes/no)')
    if a == 'no':
        for i in (a_chicken, a_cow, a_dog, a_pig, a_sheep):
            i.info()
            print('\n')
        break
print(f'Ферма прожила {count} дня(ей/)')
