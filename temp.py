import random


ls = []
for j in range(10000):
    mx_bid = 0
    amount = 10
    bid = 10
    wrong = 0
    for i in range(480):
        amount -= bid
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        # print(a, b)
        # bid on number
        if a == b:
            wrong = 0
            amount += 9 * bid
        else:
            wrong += 1

        bid = min(  (2**(wrong)) * 10, 20000000000000)
        mx_bid = max(mx_bid, bid)
        # # bid on odd even
        # if a%2 == b%2:
        #     wrong = 0
        #     amount += 1.98 * bid
        # else:
        #     wrong += 1
        #     bid = (2**wrong) * 10
            
        # if i % 10000 == 0:
        #     print(amount, wrong)

    # print("max bid: ", mx_bid)
    ls.append(amount)
    
print("avg amount: ", sum(ls)/len(ls))

