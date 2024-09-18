class Interface:
    def __init__(any, animal: str, ready: bool, hunger: float, thirst: float):
        any.animal = animal
        any.ready = ready
        any.hunger = hunger
        any.thirst = thirst

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


ghost = Interface('cow', False, 0.5, 0.7)
ghost.info()


