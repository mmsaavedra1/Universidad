def selection_sort(lista):
	largo = len(lista)
	for i in range(largo):
		# Para saber que hace el algoritmo en c/ iteracion quitar el # de abajo
		print(lista)

		# Busqueda de elemento menor y su indice
		elemento_minimo = min(lista[i:])
		indice_minimo = lista.index(elemento_minimo)

		# Cambio de elemento minimo
		auxiliar = lista[indice_minimo]
		lista[indice_minimo] = lista[i]
		lista[i] = auxiliar

	print("\n--- Lista ordenada con Selection Sort ---")
	return lista


def insert_sort(lista):
	largo = len(lista)
	for i in range(1, largo):
		# Para saber que hace el algoritmo en c/ iteracion quitar el # de abajo.
		print(lista)

		# Se comprueba si el elemento de la izquierda es menor hasta llegar al final.
		j = i

		# Almaceno el elemento de la itereacion actual, ya que la lista se va 
		# actualizando y se pierde dicho indice en cada iteracion del while.
		elemento_actual = lista[i]

		while (elemento_actual < lista[j-1]) and (j > 0):
			# Muevo a la derecha los elementos
			lista[j] = lista[j-1]

			# Se recorre un indice mas a la izquierda
			j -= 1

		# Actualizo el elemento j ya que esta repetido
		lista[j] = elemento_actual

	print("\n--- Lista ordenada con Insert Sort ---")
	return lista


if __name__ == '__main__':
	lista = [4, 10, 25, 8, 49, 0, 32]
	print(selection_sort(lista))

	print("\n")
	print("-----*"*7)
	print("\n")
	
	print(insert_sort(lista))
