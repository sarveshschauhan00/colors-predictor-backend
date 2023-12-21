import random


ls = []

amount = 10
bid = 10
wrong = 0

max_wrong = 0
for i in range(480):
    if i%40 == 0:
        print(i)
    amount -= bid
    a = random.randint(0, 99)

    if wrong == 30:
        wrong = 0
    # if a < 12:
    #     wrong = 0
    #     amount += 8.55 * bid
    # else:
    #     wrong += 1

    # bid on odd even
    if a < 50:
        wrong = 0
        amount += 2 * bid
    else:
        wrong += 1

    bid = (2 ** wrong) * 10
    # bid = min(  bid, (2**20)*10 )
    # bid = 10

    max_wrong = max(max_wrong, wrong)
print(amount, max_wrong)
