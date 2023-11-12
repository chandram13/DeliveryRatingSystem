# Marvish Chandra


def orderQuality(deliveryTime,speed):
    for d in deliveryTime:
        if d > 30: print("The driver is taking too long to arrive.")
        if d < 30: print("The driver is on time or even early for your order.")
        else: print("The driver is either on time or running late.")
    orderFormula = deliveryTime * speed
    print(orderFormula)


    orderQuality(30,65)
    orderQuality(60,80)
