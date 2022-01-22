num = int(input("Insert the number: "))


class Summa:
    def __init__(self, numbers: list, disared_sum: int):
        self.numbers = numbers
        self.disared_sum = disared_sum

    def index(self):
        for i in range(len(self.numbers)):
            for n in range(i + 1, len(self.numbers)):
                if (self.numbers[i] + self.numbers[n]) == self.desired_sum:
                    return (i, n)


num_1 = Summa(numbers=[2, 7, 11, 15], disared_sum=num)
print(num_1)
print(num_1.index())
