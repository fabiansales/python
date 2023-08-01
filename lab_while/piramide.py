blocks = int(input("Numbers of Blocks: "))
height = 0 # altura
cant_in_one_line = 1 # cantidad de bloques en una linea

while height < blocks:
    height += 1 # sumo uno a la altura
    blocks -= cant_in_one_line # le resto a la cantidad de bloques la cantidad de bloques que hay en una linea
    cant_in_one_line += 1 #

print(f"The height of the Pyramid is {height},and there are left over: {blocks}")
