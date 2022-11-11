# IMPORT thread module
from threading import *
from time import sleep

# Extand thread class to make a saprate thread
class Hello(Thread):
    # override run method in thread class
    def run(self):
        for i in  range(8):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in  range(8):
            print("Hi")
            sleep(5)


t1=Hello()
t2=Hi()

# call start to execute run as a separate thread
t1.start()
# sleep to make threads start on different times so they reach the processor
sleep(1)
t2.start()

# calling join function to halt the main thread until the thread calling join() joins the main thread(completes its execution)
t1.join()
print("Bye")