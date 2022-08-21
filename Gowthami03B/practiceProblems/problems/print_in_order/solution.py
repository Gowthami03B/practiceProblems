from threading import Lock
#the second job should depend on the completion of the first job and the third job should depend on the completion of the second job.
class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()#thread A releases the lock

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJobDone:#when second one wants to execute, it needs to obtain the lock on first to maintain order
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.secondJobDone.release()#with operation also releases the lock of firstJobDone


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondJobDone:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()