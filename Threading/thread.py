import threading
import logging
import time 
import concurrent.futures

# def thread_fun(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(1)
#     logging.info("Thread %s: finishing", name)


# def free_time(act):
#     print(f"I am {act}")


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_fun, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     free_time("playing chess")
#     logging.info("Main    : all done")

import logging
import threading
import time
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)


# class Database:
#     def __init__(self):
#         self.value = 0
    
#     def update(self, name):
#         print(f"Thread {name}: starting update")
#         local_copy = self.value
#         local_copy += 1 
#         time.sleep(0.2)
#         self.value = local_copy
#         print(f"Thread {name}: finishing update")


# if __name__ == "__main__":
#     database = Database()
#     print("Testing update. Starting value is {}.".format(database.value))
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.update, index)
#     print("Testing update. Ending value is {}".format(database.value))

class Database:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def update(self, name):
        print(f"Thread {name}: starting update")
        # self.lock.acquire()
        # local_copy = self.value
        # local_copy += 1 
        # time.sleep(0.2)
        # self.value = local_copy
        
        # print(f"Thread {name}: finishing update")
        # self.lock.release()
        # or can be done as 

        with self.lock:
            local_copy = self.value
            local_copy += 1 
            time.sleep(0.2)
            self.value = local_copy
        
        print(f"Thread {name}: finishing update")


if __name__ == "__main__":
    database = Database()
    print("Testing update. Starting value is {}.".format(database.value))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    print("Testing update. Ending value is {}".format(database.value))