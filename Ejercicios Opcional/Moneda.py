def money_change(money):
    #money: the amount to change if different coins
    coins= [1.5,10]
    result = 0 #result : the minimun quantity of  conins needed to change the given money.

    for coins in coins: 
        while money >= coins: 
            money -= coins
            result = result + 1 
        return result
    
    Julian = int(input(""))

    resultado = money_change(Julian)
    print (f"{resultado}")