import time

class Timing:
    def __init__(self, function_to_run):
        self.num_runs = 100
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(
            "[Timing] Среднее время выполнения %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )
        return self.func_to_run(*args, **kwargs)


print("функция, которая будет тестироваться по умолчанию >>> Построение списка чисел фибоначи до 4 000 000 для числа 80")
print('''
def fibonachi(n):
    n = int(n)
    fib = [0,1]+[0]*(n-1)
    for i in range (2, n+1):
        if fib[i-1]+fib[i-2] <= 4000000:
            fib[i] = fib[i-1]+fib[i-2]
        else:
            return fib
    return fib  
fib = fibonachi(80)
''')
@Timing
def fibonachi(n):
    n = int(n)
    fib = [0,1]+[0]*(n-1)
    for i in range (2, n+1):
        if fib[i-1]+fib[i-2] <= 4000000:
            fib[i] = fib[i-1]+fib[i-2]
        else:
            return fib
    return fib  

fib = fibonachi(80)

input('Нажмите любую клавишу, чтобы завершить\n')
