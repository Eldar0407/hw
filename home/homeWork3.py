class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f'name:{self._name}\nbalance:{self._balance}')

    def moneyX(self):
        self._balance += int(input('Внесите деньги:'))
        print(f'Текущий баланс:{self._balance}')

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance = self._balance * 10

    def _plus(self):
        self._balance += B._balance

B = Bank('ggg', 1000)


Eldar = Bank('FFF', 100)
Eldar.moneyX()
Eldar._Bank__jackpot()
Eldar._plus()
# Eldar._kill()
print(Eldar)
print(dir(Eldar))