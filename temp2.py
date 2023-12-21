import random


ls = []

for j in range(100):

    amount = 10
    bid = 10
    wrong = 0

    max_wrong = 0
    for i in range(10000):
        amount -= bid
        a = random.randint(0, 99)

        # if wrong == 20:
        #     a = 40
        if a < 12:
            wrong = 0
            amount += 8.55 * bid
        else:
            wrong += 1

        # # bid on odd even
        # if a < 50:
        #     wrong = 0
        #     amount += 1.95 * bid
        # else:
        #     wrong += 1

        bid = (2 ** wrong) * 10
        bid = min(  bid, (2**20)*10 )
        # bid = 10

        max_wrong = max(max_wrong, wrong)
        # if i % 10000 == 0:
        #     print(amount, wrong)
        # print(amount, wrong)
    print(amount, max_wrong)
    ls.append(amount)
print(sum(ls)/len(ls))

