class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if number_of_floors % 10 == 1:
            print(f'ЖК "{self.name}", {self.number_of_floors} этаж.')
        elif number_of_floors % 10 == 2 or 3 or 4:
            print(f'ЖК "{self.name}", {self.number_of_floors} этажа.')
        elif number_of_floors % 10 == 5 or 6 or 7 or 8 or 9:
            print(f'ЖК "{self.name}", {self.number_of_floors} этажей.')

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor}? Такого этажа не существует!')
        else:
            print(*range(1, new_floor + 1), sep='\n')


h1 = House('Marble', 22)
print()
h1.go_to(22)
print()
h1 = House('Chesterfield', 101)
h1.go_to(402)

