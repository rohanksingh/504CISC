DEFAULT_INITIAL_BASKET = ["orange", "apple"]

def create_picnic_basket(healthy, hungry, initial_basket=None):
    if initial_basket == None:
        basket = ["orange", "apple"]        # Initializing the intital basket condition to debug the code error for third print
    else:
        basket= initial_basket
    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Reproducer
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))
