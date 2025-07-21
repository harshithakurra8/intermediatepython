from threading import Thread
import time


database_value = 0

def increase():
    global database_value 

    # get a local copy (simulate data retrieving)
    local_copy = database_value

    local_copy += 1
    time.sleep(0.1)

    database_value = local_copy


if __name__ == "__main__":

    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')