class Bank:
    def __init__(self,name,balanse):
        self._name = name
        self._balanse = balanse


    def moneyX(self):
        dengi = float(input("Введите сумму для добавления на счет"))
        self._balanse += dengi
        print(F"деньги успешно длбавлены.Текущий баланс:  {self._balanse}")


    def _kill(self):
        self._balanse = 0
        print("Баланс обнулен.")


    def __jackpot(self):
        self._balanse *= 10
        print(F"Выигрыш в лотерею. Баланс увеличен в 10 раз. текущий баланс: {self._balanse}")


    def _merge_balance(self, other):
        self._balanse += other._balanse
        other._balance = self._balanse
        print(f"Балансы объединены. Ваш баланс: {self._balanse}, баланс второго клиента: {other._balance}")


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num2

    def __mul__(self, other):
        return self.num1 * other.num2

    def __truediv__(self, other):
        return self.num1 / other.num2


client1 = Bank("Клиент 1", 100)
client2 = Bank("Клиент 2", 100)

client1.moneyX()
client2.moneyX()

client1._merge_balance(client2)

client1._kill()

calc = Calculator(10, 5)
print(calc.__add__(calc))
print(calc.__sub__(calc))
print(calc.__mul__(calc))
print(calc.__truediv__(calc))



