class IntegralMethods:

    def func(self, x):
        return 6*x**2 + 3*x - 5

    def parabola(self, a, b, n_iter=100):
        func = self.func
        h = (b - a) / n_iter
        i = a + h
        r1 = b - h
        r2 = b - 2 * h
        odd = 0
        even = 0
        while i <= r1:
            odd += func(i)
            i += 2 * h
        i = a + 2 * h
        while i <= r2:
            even += func(i)
            i += 2 * h
        res = h / 3 * (func(a) + func(b) + 4 * odd + 2 * even)
        return res

    def trapeze(self, a, b, n_iter=100):
        func = self.func
        result = 0
        h = 1 / n_iter
        while a <= b - h:
            result += (func(a) + func(a + h)) / 2 * h
            a += h
        return result


# i = IntegralMethods()
# 123

# print(round(i.parabola(-10, 10), 5), round(i.trapeze(-10, 10), 5), type(i.parabola(-10, 10)))