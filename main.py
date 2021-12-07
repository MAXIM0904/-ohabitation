from random import randint


class House:
    def __init__(self):
        self.money_table = 100
        self.food_fridge = 50
        self.food_cat = 30
        self.mud = 0

    def count_mud(self):
        self.mud += 5


class Cat:
    def __init__(self, name_cat):
        self.name_cat = name_cat
        self.satiety_cat = 30
        self.house_cat = None
        self.life_cat = True

    def eat_cat(self):
        print(f"\n{self.name_cat} голоден. Пошел есть.\n")
        eat_cat = randint(5, 10)
        if self.house_cat.food_cat <= 0:
            print("Сегодня голодаем...")
        else:
            self.satiety_cat += 10
            self.house_cat.food_cat -= eat_cat
            self.satiety_cat += eat_cat * 2

    def sleep_cat(self):
        print(f"\n{self.name_cat} спит.")

    def tear_wallpaper(self):
        print(f"\n{self.name_cat} дерет обои.\n")
        self.house_cat.mud += 5

    def activity_cat(self):
        if self.satiety_cat <= 0:
            print(f"\n{self.name_cat} умер.")
            self.life_cat = False

        if self.life_cat:
            choice = randint(0, 1)
            if self.satiety_cat <= 10:
                self.eat_cat()
            elif choice == 0:
                self.sleep_cat()
            elif choice == 1:
                self.tear_wallpaper()
            self.satiety_cat -= 10
        else:
            self.life_cat = False


class Person:
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.house = None
        self.cat = None
        self.life_user = True

    def petting_cat(self):
        print(f"\n{self.name} гладит кота!")
        self.happiness += 5

    def house_user(self, class_house_objekt):
        self.house = class_house_objekt

    def cat_user(self, class_cat_objekt, class_house=None):
        # Лучше class_cat_objekt = self.house
        self.cat = class_cat_objekt
        self.cat.house_cat = class_house

    def eat(self):
        print(f"\n{self.name} голоден. Пошел есть.")
        self.satiety += 10
        eat_person = randint(20, 30)
        if self.house.food_fridge <= 0:
            print("Сегодня голодаем...")
        else:
            self.house.food_fridge -= eat_person
            self.satiety += eat_person

    def life_activity(self):
        if self.life_user:
            if self.house.mud > 95:
                self.happiness -= 10

            if self.satiety <= 0:
                print(f"\n{self.name} умер от голода!\n")
                return False

            if self.happiness <= 10:
                print(f"\n{self.name} умер от тоски!\n")
                return False
            self.satiety -= 10
            return True
        else:
            return False

    def get_user_status(self):
        print(f"\n{self.name}:\nСытость: {self.satiety}\nСчастье: {self.happiness}\n"
              f"В холодильнике {self.house.food_fridge} еды.\nДенег: {self.house.money_table}\n"
              f"Еды для кота: {self.house.food_cat}\nГрязь в доме: {self.house.mud}")

    def activity(self):
        return self.satiety


class Husband(Person):

    def game(self):
        print(f"\n{self.name} пошел играть.")
        self.happiness += 60

    def work(self):
        print(f"\n{self.name} пошел работать.")
        self.house.money_table += 150

    def activity(self):
        self.life_user = self.life_activity()
        if self.life_user:
            if self.satiety <= 10:
                self.eat()
            elif self.happiness <= 40:
                self.game()
            elif self.house.money_table <= 300:
                self.work()
            else:
                self.petting_cat()
            self.get_user_status()


class Wif(Person):

    def shop_products(self):
        print(f"\n{self.name} пошла в магазин.")
        if self.house.money_table <= 0:
            print("Денег нет и еды нет!")
        else:
            self.house.money_table -= 40
            self.house.food_fridge += 40

    def shop_products_cat(self):
        print(f"\n{self.name} пошла за едой коту.")
        if self.house.money_table <= 10:
            print("Денег на кота нет!")
        else:
            self.house.money_table -= 30
            self.house.food_cat += 30

    def shop_fur_coat(self):
        print(f"\n{self.name} купила шубу. :=)")
        if self.house.money_table < 350:
            print("Денег нет и шубы нет!")
        else:
            self.house.money_table -= 350
            self.happiness += 60

    def cleaning(self):
        print(f"\n{self.name} прибирается в доме.")
        if self.house.mud <= 100:
            self.house.mud = 0
        else:
            self.house.mud -= 100

    def activity(self):
        self.life_user = self.life_activity()
        if self.life_user:
            if self.satiety <= 20 and self.house.food_fridge >= 0:
                self.eat()
            elif self.house.food_fridge <= 40:
                self.shop_products()
            elif self.house.mud >= 80:
                self.cleaning()
            elif self.happiness <= 30:
                self.shop_fur_coat()
            elif self.cat.satiety_cat <= 10:
                self.shop_products_cat()
            else:
                self.petting_cat()
            self.get_user_status()


victor = Husband("Виктор")
macha = Wif("Маша")
murca = Cat("Мурка")
victor.house_user(House())
macha.house_user(victor.house)
macha.cat_user(murca)
victor.cat_user(murca, victor.house)

for i_namber in range(1, 366):
    print(f"День {i_namber}")
    victor.house.count_mud()
    victor.activity()
    macha.activity()
    murca.activity_cat()

# зачёт!
