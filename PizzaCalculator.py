# Piet besteld 6 pizza's, 2 small, 2 medium en 2 large bij de Domino's, hoeveel kost dit?

print("Piet besteld 6 pizza's: 2 small, 2 medium en 2 large bij de Domino's, wat zijn de kosten? reken uit:")
print("Hoeveel small pizza's wilt Piet?:")
pizzasmall = input("Aantal small pizza's: ")

print("Hoeveel medium pizza's wilt Piet?:")
pizzamedium = input("Aantal medium pizza's: ")

print("Hoeveel large pizza's wilt Piet?:")
pizzalarge = input("Aantal large pizza's: ")


pizzasmall = int(pizzasmall)
pizzamedium = int(pizzamedium)
pizzalarge = int(pizzalarge)

pizzasmall = pizzasmall * 8.99
pizzamedium = pizzamedium * 10.49
pizzalarge = pizzalarge * 12.99

price = pizzasmall + pizzamedium + pizzalarge
lunchTotal = price

lunchTotal = int(lunchTotal)

print("De 6 pizza's kost je bij de Domino's", lunchTotal, "euro, voor de small pizza", pizzasmall, "voor de medium pizza ", pizzamedium, "euro en voor de large pizza", pizzalarge, "euro")