from threading import Condition


class Foo:
    def __init__(self):
        self.condi_2 = Condition()
        self.condi_3 = Condition()

    def first(self, printFirst: 'Callable[[], None]') -> None:  # noqa
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.condi_2.acquire()
        self.condi_2.notify()
        self.condi_2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:  # noqa
        # printSecond() outputs "second". Do not change or remove this line.
        self.condi_2.acquire()
        self.condi_2.wait()
        printSecond()
        self.condi_3.notify()
        self.condi_3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:  # noqa
        # printThird() outputs "third". Do not change or remove this line.
        self.condi_3.acquire()
        self.condi_3.wait()
        printThird()
        self.condi_3.release()
