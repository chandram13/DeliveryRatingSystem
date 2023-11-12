# Marvish Chandra


def orderQuality(deliveryTime,speed):
    for d in deliveryTime:
        if d > 30: print("The driver is taking too long to arrive.")
        if d < 30: print("The driver is on time or even early for your order.")
        else: print("The driver is either on time or running late.")
    orderFormula = deliveryTime * speed
    print(orderFormula)

def ratingSystem(deliveryTime,speed,customerRank):
    if speed >= 65:
        print("The order is one star because the order didn't arrive on time.")
    if speed < 65:
        print("The order is five stars because the order delivery is fast.")
    findRate = deliveryTime * speed + customerRank
    print(findRate)

    orderQuality(30,65)
    orderQuality(60,80)
    ratingSystem((41,65,20))
