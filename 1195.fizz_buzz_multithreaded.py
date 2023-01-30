import threading


class FizzBuzz:
    def __init__(self, n: int):
        '''

        Implement the waiting flag.
        '''
        self.n = n
        self.count = 1
        self.count_3 = 2
        self.count_5 = 4
        self.lock = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:  # noqa
        while True:
            self.lock.acquire()
            if self.count < self.n:
                self.lock.release()
                break
            if self.count_3 == 0 and self.count_5 != 0:
                self.count_3 = 2
                self.count_5 -= 1
                printFizz()
                self.count += 1
            self.lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:  # noqa
        while True:
            self.lock.acquire()
            if self.count < self.n:
                self.lock.release()
                break
            if self.count_3 != 0 and self.count_5 == 0:
                self.count_3 -= 1
                self.count_5 = 4
                printBuzz()
                self.count += 1
            self.lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:  # noqa
        while True:
            self.lock.acquire()
            if self.count < self.n:
                self.lock.release()
                break
            if self.count_3 == 0 and self.count_5 == 0:
                self.count_3 = 2
                self.count_5 = 4
                printFizzBuzz()
                self.count += 1
            self.lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:  # noqa
        while True:
            self.lock.acquire()
            if self.count < self.n:
                self.lock.release()
                break
            if self.count_3 != 0 and self.count_5 != 0:
                self.count_3 -= 1
                self.count_5 -= 1
                printNumber(self.count)
                self.count += 1
            self.lock.release()
