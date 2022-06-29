class HW:
    def __init__(self, data):
        self.data = data

    def reckoning(self):
        vowels = 0  # глассные
        v = ''
        consonants = 0  # согласные
        c = ''
        suma = 0

        if self.data.isalpha():
            for i in self.data:
                if i in "aeoiuyауоеияюёэы":
                    vowels += 1
                    v += i
                else:
                    consonants += 1
                    c += i
            if vowels * consonants <= len(self.data):
                return v
            elif vowels * consonants > len(self.data):
                return c

        elif self.data.isdigit():
            for j in self.data:
                j = int(j)
                if j % 2 == 0:
                    j = str(j)
                    for k in j:
                        k = int(k)
                        suma += k
            return suma * len(self.data)


hw = HW(input('Введите строку или число: '))
print(hw.reckoning())


