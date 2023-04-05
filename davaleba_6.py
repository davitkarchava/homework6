# მაგალითი_1

class Currency:
    shedareba = {"USD": 2.7, "EUR": 3}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value:.2f} {self.unit}"

    def change_to(self, new_unit=input("შეიყვანეთ ვალუტა რომელშიც გსურთ არსებული თანხის გადაყვანა: \n ")):
        """აქ დავალებაში რომ ეწერა ეგ რიცხვები გამოვიყენე და არა რეალური ვალუტა"""
        usd_rate = 2.7
        eur_rate = 3
        if self.unit == "GEL" and new_unit == "USD":
            new_value = self.value / usd_rate
            return Currency(new_value, new_unit)
        elif self.unit == "GEL" and new_unit == "EUR":
            new_value = self.value / eur_rate
            return Currency(new_value, new_unit)
        elif self.unit == "USD" and new_unit == "GEL":
            new_value = (self.value * usd_rate)
            return Currency(new_value, new_unit)
        elif self.unit == "USD" and new_unit == "EUR":
            new_value = (self.value * usd_rate) / eur_rate
            return Currency(new_value, new_unit)
        elif self.unit == "EUR" and new_unit == "GEL":
            new_value = (self.value * eur_rate)
            return Currency(new_value, new_unit)
        elif self.unit == "EUR" and new_unit == "USD":
            new_value = (self.value * eur_rate) / usd_rate
            return Currency(new_value, new_unit)
        elif self.unit == new_unit:
            return self

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.unit == other.unit:
                return Currency(self.value + other.value, self.unit)
            else:
                converted_value = other.change_to(self.unit).value
                return Currency(self.value + converted_value, self.unit)

    def __mul__(self, other):
        if other is int or float:
            new_value = self.value * other
            return Currency(new_value, self.unit)
        else:
            raise TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")

    def __gt__(self, other):
        if isinstance(other, Currency):
            if self.unit == other.unit:
                return self.value > other.value
            elif self.unit == "GEL" and other.unit == "USD":
                return self.value > other.value * self.shedareba[other.unit]
            elif self.unit == "GEL" and other.unit == "EUR":
                return self.value > other.value * self.shedareba[other.unit]
            elif self.unit == "USD" and other.unit == "EUR":
                return self.value > (other.value / self.shedareba[self.unit]) * self.shedareba[other.unit]
            elif self.unit == "EUR" and other.unit == "USD":
                return self.value > (other.value / self.shedareba[self.unit]) * self.shedareba[other.unit]

ob1 = Currency(10000)
ob2 = Currency(10, "USD")
print(f"თავდაპირველ ვალუთაში მყოფი თანხა შეადგენდა: \n {ob1}-ს")
print(f"თქვენს მიერ არჩეულ ვალუტაში გადაყვანილი თანხა ამჟამად არის: \n {ob1.change_to()}")
print(f"თავდაპირველ ვალუთაში მყოფი თანხა შეადგენდა: \n {ob2}-ს")
print(f"თქვენს მიერ არჩეულ ვალუტაში გადაყვანილი თანხა ამჟამად არის: \n {ob2.change_to()}")
print(ob1.__add__(ob2))
print(ob1.__mul__(2))
print(ob1.__gt__(ob2))

# მაგალითი_2


class Person:

    def __init__(self, name,  deposit=100, loan=0, owner=None):
        self.name = name
        self.deposit = deposit
        self.loan = loan
        owner_name = owner

    def __str__(self):
        return f"Name:{self.name} Deposit:{self.deposit} Loan:{self.loan}"


class House:

    def __init__(self, ID, price, owner_name, status='for sale', ):
        self.ID = ID
        self.price = price
        self.owner = owner_name
        self.status = status

    def sell_house(self, myidveli, loan=None):
        if loan is not None:
            self.owner.deposit += self.price
            self.owner = myidveli
            myidveli = self.owner
            self.status = 'sold on loan'
            myidveli.loan += loan
            return f"{self.ID} გაყიდულია {myidveli.name}-ზე {self.price}-ად სესხით: {loan}"
        else:
            self.owner.deposit += self.price
            myidveli.deposit -= self.price
            self.owner = myidveli
            myidveli = self.owner
            self.status = "sold"
            return f"აპარტამენტი ID-ით: {self.ID} არის გაყიდული {myidveli.name}-ზე "


ff = Person("data")
ss = Person("saba", 200)
cc = House("dadad", 400, ff)
print(ff)
print(ss)
print(cc.sell_house(ss, 5))
print(ff)
print(ss)

# მაგალითი_3


class Plane:

    def move(self):
        print("Plane can fly")

    def speed(self):
        print("Its speed is up to 900km/h")


class Bus:

    def move(self):
        print("Bus can move on roads")

    def speed(self):
        print("Its speed is up to 180km/h")


def move_speed(plane_bus):
    plane_bus.move()
    plane_bus.speed()


obj_1 = Plane()
obj_2 = Bus()
move_speed(obj_1)
move_speed(obj_2)
