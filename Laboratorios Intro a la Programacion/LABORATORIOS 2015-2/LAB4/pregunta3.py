from random import randint as r

def refrigerador(people, pizzas, cans):
    needed_c = 4 * people
    needed_p = int((1/3) * people) + 1
    if cans >= needed_c and pizzas > needed_p:
        return True, 0, 0
    else:
        return False, (needed_c - cans), (needed_p - pizzas)
    return False

while True:
    break
    people = int(input("Personas: "))
    pizzas = int(input("Pizzas: "))
    cans = int(input("Latas: "))
    success, m_cans, m_pizza = refrigerador(people, pizzas, cans)
    print("Exito:", success, "; Faltan tantas latas:", m_cans, "; Faltan tantas pizzas:", m_pizza)

p_success, p_cans, p_pizzas = refrigerador(100, 0, 0)
r_cans = r_pizzas = 0

for i in range(101):
    r_cans += r(2, 6)
    r_pizzas += r(0, 5)

r_pizzas /= 6
r_pizzas = int(r_pizzas) + 1

f_success = (refrigerador(100, r_pizzas, r_cans))
print(f_success)

print("Las pizzas estimadas fueron:", p_pizzas)
print("Las pizzas finales fueron:", r_pizzas)
print("Las latas estimadas fueron:", p_cans)
print("Las latas finales fueron:", r_cans)
print("La fiesta fue un " + ("exito." if f_success[0] else "fracaso."))