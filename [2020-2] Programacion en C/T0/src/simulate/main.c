#include "mould.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>


/* Retorna true si ambos strings son iguales */
bool string_equals(char *string1, char *string2)
{
  return !strcmp(string1, string2);
}

/* Revisa que los parámetros del programa sean válidos */
bool check_arguments(int argc, char **argv)
{
  if (argc != 3)
  {
    printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
    printf("Donde:\n");
    printf("\tINPUT es la ruta del archivo de input\n");
    printf("\tOUTPUT es la ruta del archivo de output\n");
    return false;
  }

  return true;
}

// Funciones que serán ocupadas
  Cell* add_cell (int* id);
  Cell* copy_cell(Cell* cell_to_clone, int* id);
  Cell* copy_absorb (Cell* cell_to_clone);
  void observe (Cell* cell, int spacing, int idx, FILE* file);
  void free_mould(Cell* cell);

/* Programa principal */
int main(int argc, char **argv)
{
  
  /* Si los parámetros del programa son inválidos */
  if (!check_arguments(argc, argv))
  {
    /* Salimos del programa indicando que no terminó correctamente */
    return 1;
  }

  /* Para leer las instrucciones */
  char command[32];
 
  /* Para obtener la profundidad e índice de los comandos */
  int depth;
  int idx;

  /* [Por implementar] Inicalizamos el MOULD */
  int id = 0;
  Mould* mould = (Mould*) malloc(sizeof(Mould));
  mould->root = add_cell(&id);
  
  /* Abrimos el archivo de input */
  FILE *input_file = fopen(argv[1], "r");

  /* Abrimos el archivo de output */
  FILE *output_file = fopen(argv[2], "w");

  /* Número de líneas a leer */
  int n_lines;
  fscanf(input_file, "%d", &n_lines);
  
  /* Mientras existan líneas */
  while (n_lines > 0)
  {

    /* Disminuímos el número de líneas por leer en 1 */
    n_lines -= 1;

    /* Leemos la línea y lo guardamos en comando */
    fscanf(input_file, "%s", command);

    /* Caso 1: Comando GROW */
    if (string_equals(command, "GROW"))
    {
      /* [Por implementar ] Partimos desde la raíz */
      Cell* cur;
      cur = mould->root;

      /* Obtenemos la profundidad de la célula que crecerá */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta encontrar dicho nodo */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        cur = cur->children[idx];
      }

      /* Obtenemos en qué posición crear un nueva célula */
      fscanf(input_file, "%d", &idx);

      /* [Por implementar] La creamos */
      cur->children[idx] = add_cell(&id);
    }

    /* Caso 2: Comando CLONE */
    else if (string_equals(command, "CLONE"))
    {
      /* [Por implementar ] Partimos desde la raíz */
      Cell* cell_to_clone;
      cell_to_clone = mould->root;

      /* Obtenemos la profundidad de la célula a clonar */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta encontrar la célula */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        cell_to_clone = cell_to_clone->children[idx];
      }

      /* [Por implementar] Partimos desde la raíz */
      Cell* parent;
      parent = mould->root;

      /* Obtenemos la profundidad de la célula donde será clonada */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */ 
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        parent = parent->children[idx];
      }

      /* Obtenemos la posición donde será clonado */
      fscanf(input_file, "%d", &idx);

      /* [Por implementar] La clonamos */

      ///////////// TESTEO ///////////////
      parent->children[idx] = copy_cell(cell_to_clone, &id);
      ///////////// TESTEO ///////////////

    }

    /* Caso 3: Comando CROSSOVER */
    else if (string_equals(command, "CROSSOVER"))
    {
      int child_1_idx;
      int child_2_idx;

      /* [Por implementar] Partimos desde la raíz */
      Cell* parent_1;
      parent_1 = mould->root;

      /* Obtenemos la profundidad de la célula madre 1 */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] cambiamos la célula actual */
        parent_1 = parent_1->children[idx];
      }

      /* Obtenemos el índice de la primera hija */
      fscanf(input_file, "%d", &child_1_idx);

      /* [Por implementar] Obtenemos dicha hija */
      Cell* child_1;
      child_1 = parent_1->children[child_1_idx];
      /* [Por implementar] Partimos desde la raíz */
      Cell* parent_2;
      parent_2 = mould->root;

      /* Obtenemos la profundidad de la célula madre 2 */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        parent_2 = parent_2->children[idx];
      }

      /* Obtenemos el índice de la segunda hija */
      fscanf(input_file, "%d", &child_2_idx);
      
      /* [Por implementar] Obtenemos dicha hija */
      Cell* child_2;
      child_2 = parent_2->children[child_2_idx];

      /* [Por implementar] hacemos el intercambio */
      parent_1->children[child_1_idx] = child_2;
      parent_2->children[child_2_idx] = child_1;
    }

    /* Caso 4: Comando BUD */
    else if (string_equals(command, "BUD"))
    {
      /* [Por implementar] Partimos desde la raíz */
      Cell* cur;
      cur = mould->root;

      /* Obtenemos la profundidad de la célula */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha célula */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        cur = cur->children[idx];
      }

      /* Obtenemos el índice de la hija eliminar */
      fscanf(input_file, "%d", &idx);

      /* [Por implementar] La eliminamos */
      free_mould(cur->children[idx]);
      Cell* nuevo = NULL;
      cur->children[idx] = nuevo;
    }

    /* Caso 5: Comando ABSORB*/
    else if (string_equals(command, "ABSORB"))
    {

      /* [Por implementar] Partimos desde la raíz */
      Cell* parent_1;
      parent_1 = mould->root;

      /* Obtenemos la profundidad */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        parent_1 = parent_1->children[idx];
      }
      
      /* Obtenemos el índice de la hija que reemplazaremos */
      fscanf(input_file, "%d", &idx);
      
      /* [Por implementar] Obtenemos dicha hija */
      int new_idx = idx;
      Cell* parent_2;
      parent_2 = parent_1->children[new_idx];

      /* Obtenemos la profundidad del camino a continuar */
      fscanf(input_file, "%d", &depth);

      /* Iteramos por ese camino hasta la penúltima célula */
      for (int level = 0; level < depth - 1; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        parent_2 = parent_2->children[idx];

      }

      /* Obtenemos el índice de la célula que quedará */
      fscanf(input_file, "%d", &idx);

      /* [Por implementar] Obtenemos dicha célula */
      Cell* child;
      child = copy_absorb(parent_2->children[idx]);

      /* [Por implementar] Desvinculamos a la madre */
      free_mould(parent_1->children[new_idx]);
      Cell* nuevo = NULL;
      parent_1->children[new_idx] = nuevo;

      /* [Por implementar] Reemplazamos */
      parent_1->children[new_idx] = child;
    }

    /* Caso 7: Comando OBSERVE */
    else if (string_equals(command, "OBSERVE"))
    {
      /* Definimos el índice inicial */
      idx = -1;

      /* [Por implementar] Partimos desde la raíz */
      Cell* current;
      current = mould->root;

      /* Obtenemos la profundidad de la célula a observar */
      fscanf(input_file, "%d", &depth);
      
      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [Por implementar] Cambiamos la célula actual */
        current = current->children[idx];
      }

      /* Distinguimos el estado */
      fprintf(output_file, "STATE\n");

      /* [Por implementar] Obtenemos los datos de nuestra célula */
      observe(current, 0, idx, output_file);
    }
  }
  
  /* Cerramos archivo de lectura */
  fclose(input_file);

  /* Cerramos archivo de escritura */
  fclose(output_file);

  // Liberacion de memoria
  free_mould(mould->root);
  free(mould);

  return 0;
}
