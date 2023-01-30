import threading


class FizzBuzz:
    def __init__(self, n: int):
        '''
        Replace mutual lock with condition object in python to avoid busy polling.
        5% -> 96%.

        python doc ref: https://docs.python.org/3/library/threading.html#condition-objects
        '''
        self.n = n
        self.count = 0
        self.count_3 = 2
        self.count_5 = 4
        self.condition_3 = threading.Condition()
        self.condition_5 = threading.Condition()
        self.condition_15 = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:  # noqa
        self.condition_3.acquire()
        self.condition_3.wait()
        while True:
            if self.count <= self.n:
                printFizz()
            else:
                break
            self.condition_3.notify()
            self.condition_3.wait()

        self.condition_3.notify()
        self.condition_3.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:  # noqa
        self.condition_5.acquire()
        self.condition_5.wait()
        while True:
            if self.count <= self.n:
                printBuzz()
            else:
                break
            self.condition_5.notify()
            self.condition_5.wait()

        self.condition_5.notify()
        self.condition_5.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:  # noqa
        self.condition_15.acquire()
        self.condition_15.wait()
        while True:
            if self.count <= self.n:
                printFizzBuzz()
            else:
                break
            self.condition_15.notify()
            self.condition_15.wait()

        self.condition_15.notify()
        self.condition_15.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:  # noqa
        count_3 = 3
        count_5 = 5
        for i in range(self.n):
            self.count += 1
            count_3 -= 1
            count_5 -= 1

            if count_3 == 0:
                count_3 = 3
                if count_5 == 0:
                    self.condition_15.acquire()
                    self.condition_15.notify()
                    self.condition_15.wait()
                    self.condition_15.release()
                    count_5 = 5
                else:
                    self.condition_3.acquire()
                    self.condition_3.notify()
                    self.condition_3.wait()
                    self.condition_3.release()
            elif count_5 == 0:
                self.condition_5.acquire()
                self.condition_5.notify()
                self.condition_5.wait()
                self.condition_5.release()
                count_5 = 5
            else:
                printNumber(i+1)

        self.count = self.n + 1

        self.condition_3.acquire()
        self.condition_3.notify()
        self.condition_3.release()

        self.condition_5.acquire()
        self.condition_5.notify()
        self.condition_5.release()

        self.condition_15.acquire()
        self.condition_15.notify()
        self.condition_15.release()
