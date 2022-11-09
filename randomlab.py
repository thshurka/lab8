import logging
import random

logging.basicConfig(level=logging.INFO, filename="py_log.log")

n = int(input("Kol-vo bochonkov: "))
logging.info(f"User input: {n}")
li = [0]*n

for i in range(n):
    li[i] = random.randint(1,1000)

logging.info(f"User list: {li}")

k = 1
while k != 0:
    k = int(input("Vvedite nuzhnuy bochonok, esli hotite zakonchit - vvedite '0': "))
    if k == 0:
        print("Thanks for using this")
        break
        logging.info("User executed the program")
    elif k > n:
        print("Takogo bochonka net, vvedite drugoy")
        logging.error("Out of bounds")
        continue

    print(li[k-1])
    li[k-1] = "Vy uzhe brali etot bochonok"
    logging.info(f"User get: {li[k-1]}")
