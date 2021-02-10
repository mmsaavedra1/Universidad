#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/////// IMPLEMENTADO ////////
#include "../hash_functions/hash_functions.h"
#include "../BST_tree/BST_tree.h"
/////// IMPLEMENTADO ////////



/////// IMPLEMENTADO ////////
/* Auxiliares para saber si existe o no el valor cosultado */
#define NO_EXISTE 0
#define EXISTE 1

/* Se crea una estructura que almacena las tuplas (key, value) */
typedef struct Tupla {
  unsigned long int key;
  unsigned long int value;
} Tupla;

/* Se crea una estructura que almacena la tabla de hash */
typedef struct HashTabla {
  /* Se define el largo y los punteros de los datos */
  int flag; // 1 si el valor esta poblado, 0 si no
  
  /* Se crean los posibles datos por almacenar */
  struct Tupla* datos;

} HashTabla;
/////// IMPLEMENTADO ////////



int main(int argc, char** argv)
{
  if(argc != 3)
  {
    printf("Modo de uso: %s input output\nDonde:\n", argv[0]);
    printf("\t\"input\" es la ruta al archivo de input\n");
    printf("\t\"output\" es la ruta al archivo de output\n");
    return 1;
  }

  // Abrimos el archivo de input
  FILE* input_stream = fopen(argv[1], "r");

  // Abrimos el archivo de output
  FILE* output_stream = fopen(argv[2], "w");

  // Si alguno de los dos archivos no se pudo abrir
  if(!input_stream)
  {
    printf("El archivo %s no existe o no se puede leer\n", argv[1]);
    return 2;
  }
  if(!output_stream)
  {
    printf("El archivo %s no se pudo crear o no se puede escribir\n", argv[2]);
    printf("Recuerda que \"fopen\" no puede crear carpetas\n");
    fclose(input_stream);
    return 3;
  }


  /////// IMPLEMENTADO ////////
  /* Se lee el BST */
  long int n_nodos;
  fscanf(input_stream, "%li", &n_nodos);

  char nodos[n_nodos+1];
  for (int i = 1; i < n_nodos+1; i++)
  {
    fscanf(input_stream, "%s", &nodos[i]);
  }
  /////// IMPLEMENTADO ////////


  /////// IMPLEMENTADO ////////
  /* Se crea la tabla de hash*/
  unsigned long int altura = log2(1+n_nodos);
  unsigned long int largo_tabla_hash = n_nodos - altura;

  HashTabla* tabla_hash;
  tabla_hash = (HashTabla*) malloc(largo_tabla_hash*sizeof(HashTabla));


  for (long int i = 0; i < largo_tabla_hash; i++)
  {
    tabla_hash[i].datos = NULL;
    tabla_hash[i].flag = 0;
  }

  /* Se crean los auxiliares de la creacion de subarboles*/
  unsigned long int count;
  unsigned long int n_subarboles;

  /* Se crema los auxiliares para hash */
  unsigned long int hash;
  unsigned long int ajuste;

  /* Se mapean todos los subarboles de cada altura dentro de la tabla */

  for (int h = 2; h < altura; h++)
  {
    /* Cantidad esperada de subarboles */
    count = 1;
    n_subarboles = (unsigned long int) pow(2, altura - h + 1)-1;
    unsigned long int n_nodos_subarbol = (unsigned long int) pow(2, h)-1;
    char buffer[n_nodos_subarbol];
 
    /* Se entrega cada indice para la creacion */
    for (unsigned long int nodo = 1; nodo <= n_nodos; nodo++)
    {
      /* Se crea el subarbol de strings */
      entregar_subarbol(h, nodo, nodos, buffer);

      /* Se realiza la operacion de hash */
      hash = funcion_incremento(buffer);
      /* Se realiza la operacion de ajuste */
      ajuste = funcion_ajuste(hash, largo_tabla_hash);


      /* Se pobla la tabla de hash */
      Tupla* tupla = (Tupla*) malloc(sizeof(Tupla*));
      
      /* Se crean las key y valur para cada celda de la tabla de hash */
      tupla->key = hash;
      tupla->value = nodo;

      unsigned long int indice = ajuste;
      while (tabla_hash[indice].flag == 1)
      {
        /* Caso en que las key son igaules */
        indice = (indice + 1) % largo_tabla_hash;
      }

      tabla_hash[indice].flag = 1;
      tabla_hash[indice].datos = tupla;
      //printf("[%s] Key (%li) ha sido insertada en (%li)\n", buffer, tupla->key, indice);

      /* Si ya se recorrieron todos los valores, se pasa a analizar el siguiente subarbol*/
      if (count == n_subarboles)
      {
        break;
      }
      else
      {
        count++;
      }
    }
  }

  /* Se analiza el arbol entero */
  char buffer[n_nodos];
  for (int i = 1; i < n_nodos+1; i++)
  {
    buffer[i-1] = nodos[i];
  }

  hash = funcion_incremento(buffer);
  /* Se realiza la operacion de ajuste */
  ajuste = funcion_ajuste(hash, largo_tabla_hash);

  /* Se pobla la tabla de hash */
  Tupla* tupla = (Tupla*) malloc(sizeof(Tupla*));
  
  /* Se crean las key y valur para cada celda de la tabla de hash */
  tupla->key = hash;
  tupla->value = 1;

  unsigned long int indice = ajuste;
  while (tabla_hash[indice].flag == 1)
  {
    /* Caso en que las key son igaules */
    indice = (indice + 1) % largo_tabla_hash;
  }

  tabla_hash[indice].flag = 1;
  tabla_hash[indice].datos = tupla;
  //printf("[%s] Key (%li) ha sido insertada en (%li)\n", buffer, tupla->key, indice);
  /////// IMPLEMENTADO ////////


  /////// IMPLEMENTADO ////////
  /* Se obtienen las cantidades de consultas */
  long int n_consultas;
  fscanf(input_stream, "%li", &n_consultas);

  unsigned long int sub_hash;
  unsigned long int sub_ajuste;

  int existe;
  unsigned long int maximo;
  unsigned long int contador;
  unsigned long int sub_indice;

  unsigned long int recorrido;
  int espacio;

  /* Se realiza cada consulta */
  for (int j = 0; j < n_consultas; j++)
  {
    /* Se obtiene la cantidad de nodos del subarbol */
    long int n_nodos_sub;
    fscanf(input_stream, "%li", &n_nodos_sub);
    //printf("Cantidad de nodos: %li\n", n_nodos_sub);

    /* Se lee el subarbol*/
    char sub_buffer[n_nodos_sub];
    for (int i = 0; i < n_nodos_sub; i++)
    {
      fscanf(input_stream, "%s", &sub_buffer[i]);
    }

    /* Se obtiene su hash */
    sub_hash = funcion_incremento(sub_buffer);
    /* Se realiza la operacion de ajuste */
    sub_ajuste = funcion_ajuste(sub_hash, largo_tabla_hash);

    /* Se analizan los indices -> Seteo de valores iniciales */
    existe = 0;
    contador = 0;
    maximo = (unsigned long int) pow(2, altura - log2(1+n_nodos_sub) + 1) - 1;
    sub_indice = sub_ajuste;
    
    recorrido = 0;

    //printf("KEY: %li\n", sub_hash);
    /* Se realiza la busqueda */
    espacio = 0;

    while((contador != maximo) && (recorrido != largo_tabla_hash))
    {
      /* Se analiza que los key sean iguales */
      if (tabla_hash[sub_indice].datos->key == sub_hash)
      {
        /* Solo si corresponde el espacio */
        if (espacio == 1)
        {
          fprintf(output_stream, " ");
        }
       
        //printf("**** Subarbol(%s) Hash(%li) Indice: %li    ", sub_buffer, sub_hash, tabla_hash[sub_indice].datos->value);
        
        /* Guarda en el output el valor */
        fprintf(output_stream, "%li", tabla_hash[sub_indice].datos->value);
        /* Actualiza el mundo */
        existe = 1;
        espacio = 1;
        contador++;
      }
      /* Se da el salto */
      sub_indice = (sub_indice + 1)%largo_tabla_hash;
      recorrido++;
    }
    espacio = 0;
    
    /* Se analiza si existe o no*/
    if (existe == 0)
    {
      fprintf(output_stream, "%i\n", -1);
      //printf("#### Subarbol(%s) Hash(%li) Indice: %i", sub_buffer, sub_hash, -1);
    }
    else
    {
      fprintf(output_stream, "\n");
    }
    //printf("\n");
    //printf("Consulta (%s) (%li) (%li)\n", sub_buffer, sub_hash, sub_ajuste);
  }
  /////// IMPLEMENTADO ////////



  /////// IMPLEMENTADO ////////
  /* Liberar memoria */
  for (int i = 0; i < largo_tabla_hash; i++)
  {
    free(tabla_hash[i].datos);
  }
  free(tabla_hash);
  /////// IMPLEMENTADO ////////


  // Cerrar archivo de input
  fclose(input_stream);

  // Cerrar archivo de output
  fclose(output_stream);

  return 0;
}
