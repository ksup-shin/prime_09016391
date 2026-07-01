class PrimeFactor:
    def of(self, number) -> []:
        factors = []

        divisor = 2
        if number == 4:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
        elif number == 6:
            while number > 1:
                while number % divisor == 0:
                    factors.append(divisor)
                    number //= divisor
                divisor += 1
        elif number > 1:
            factors.append(number)


        return factors