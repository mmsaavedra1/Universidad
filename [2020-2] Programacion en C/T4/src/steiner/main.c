#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "auxiliar/auxiliar.h"
#include "kruskalV2/kruskalv2.h"

/* Se ocupa parte del codigo de:

Kruskal:  https://www.thelearningpoint.net/computer-science/algorithms-minimum-spanning-trees-in-graphs---the-kruskal-algorithm--with-c-program-source-code

*/

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

  /* Lectura de input */
  int size;         // Alto y ancho de grilla
  int N;            // N° de puntos
  int MST_cost;     // Costo mínimo inicial
  
  fscanf(input_stream, "%d %d %d", &size, &N, &MST_cost);

  int row;
  int col;

  /////////// IMPLEMENTADO ///////////  
  /* Se crea la matriz de aristas */
  int* edges[N];
  for (int i = 0; i < N; i ++)
  {
    edges[i] = calloc(N, sizeof(int));
  }  
  /////////// IMPLEMENTADO ///////////


  /////////// IMPLEMENTADO ///////////
  /* Se crea la lista de vertices */
  Vertice vertices[N];

  /* Obtenemos cada uno de los puntos */
  for(int i = 0; i < N; i++)
  {
    fscanf(input_stream, "%d %d", &row, &col);

    /* Se crea el vertice y se guarda en el array */
    Vertice v;
    v.x = col;
    v.y = row;

    vertices[i] = v;
  }
  /////////// IMPLEMENTADO ///////////


  ////////// IMPLEMENTADO ///////////
  /* Se almacenan los valores de los arcos */
  Vertice v_i;
  Vertice v_f;
  int distancia;

  /* Se analizan todos los nodos */
  for (int i = 0; i < N; i++)
  {
    v_i = vertices[i];
    for (int f = 0; f < N; f++)
    {

      /* Se asume que no se puede volver al mismo nodo */
        v_f = vertices[f];

        /* Se calcula la distancia Manhatan */
        distancia = distancia_rectilinea(v_i, v_f);
        
        /* Se almacena el edge */
        edges[i][f] = distancia;
    }
  }
  /////////// IMPLEMENTADO ///////////


  /////////// KRUSKA v2 ///////////
  /* Se inicializan los objetos a trabajar */
  int* graph[N];
  for (int i = 0; i < N; i ++)
  {
    graph[i] = calloc(N, sizeof(int));
  }

  Edge* E = calloc(N*N, sizeof(Edge));

  /* Se crea el arreglo de edges */
  for (int i = 0; i < N; i++)
  {
      for (int j = 0; j < N; j++)
      {
          E[i*N + j].from = i; 
          E[i*N + j].to = j; 
          E[i*N + j].weight = edges[i][j];
      }
  }

  /* Ejecutamos Kruskal MST */
  //imprimir_matriz_adyacencia(N, edges);
  int MST = Kruskal(N, N*N, N, E, graph);
  printf("El MTS es: %i\n", MST);  
  /////////// KRUSKAL v2 ///////////





// ################################# STEINER SHIT ######################################






  ////////// IMPLEMENTADO ///////////

  /* Matriz para saber si el punto ya existe o no*/
  int* existe_punto[size];
  for (int i = 0; i < size; i ++)
  {
    existe_punto[i] = calloc(size, sizeof(int));
  } 

  /* Se itera sobre los ya conocidos */
  Vertice aux;
  for (int i = 0; i < N; i++)
  {
    aux = vertices[i];
    
    existe_punto[aux.y][aux.x] = 1;
    
  } 


  /* Logica de los Steiner points */
  int M = 0;

  /* Se cuentan todos los puntos como proyecciones */
  int x;
  int y;
  for(int i = 0; i < N; i++)
  {
    for(int j = 0; j < N; j++)
    {
      if(graph[i][j] != -1)
      {
        /* Busca los valores que tienen una diagonal metida x ahi */
        if ( (vertices[i].y != vertices[j].y) && (vertices[i].x != vertices[j].x) )
       {
          /* Proyeccion */
          x = max(vertices[i].x, vertices[j].x);
          y = min(vertices[i].y, vertices[j].y);
          /* Si no existe se considera */
          if (existe_punto[y][x] == 0)
          {
            existe_punto[y][x] = 1;
            M++;
          }
          
        }
      }
    }
  }
  
  for (int i = 0; i < size; i ++)
  {
    for (int j = 0; j < size; j ++)
    {
      existe_punto[i][j] = 0;
    }
  } 

  /* Se itera sobre los ya conocidos */
  for (int i = 0; i < N; i++)
  {
    aux = vertices[i];
    
    existe_punto[aux.y][aux.x] = 1;
    
  } 
  
  /* Se agregan todos los puntos como proyecciones */
  Vertice s_vertices[M];
  Vertice ver;

  int contador = 0;

  for(int i = 0; i < N; i++)
  {
    for(int j = 0; j < N; j++)
    {
      if(graph[i][j] != -1)
      {
        /* Busca los valores que tienen una diagonal metida x ahi */
        if ( (vertices[i].y != vertices[j].y) && (vertices[i].x != vertices[j].x) )
        {
          /* Proyeccion */
          x = max(vertices[i].x, vertices[j].x);
          y = min(vertices[i].y, vertices[j].y);

         
          if (existe_punto[y][x] == 0)
          {
            existe_punto[y][x] = 1;
            /* Se crea el vertice y se guarda en el array */
            ver.x = x;
            ver.y = y;
          
            s_vertices[contador] = ver;
            contador++;
          }
  
        }
      }
    }
  }

  /*
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      printf("%i ", existe_punto[i][j]);
    }
    printf("\n");
  }
  */
  
  /* Se ejecuta toda la logica de nuevo */
  M = contador;
  printf("Antiguo N: %i\n", N);
  N = N + M;
  printf("DSPS N: %i\n", N);


  /* Se crea la matriz de aristas */
  int* new_edges[N];
  for (int i = 0; i < N; i ++)
  {
    new_edges[i] = calloc(N, sizeof(int));
  }  
  /////////// IMPLEMENTADO ///////////


  /////////// IMPLEMENTADO ///////////
  /* Se crea la lista de vertices */
  Vertice new_vertices[N];

  /* Obtenemos cada uno de los puntos */
  for(int i = 0; i < N-M; i++)
  {
    new_vertices[i] = vertices[i];
  }

  for (int i = 0; i < M; i++)
  {
    
    new_vertices[N-M+i] = s_vertices[i];
  }

  /////////// IMPLEMENTADO ///////////


  ////////// IMPLEMENTADO ///////////
  /* Se almacenan los valores de los arcos */

  /* Se analizan todos los nodos */
  Vertice new_v_i;
  Vertice new_v_f;
  int new_distancia;

  for (int i = 0; i < N; i++)
  {
    new_v_i = new_vertices[i];
    for (int f = 0; f < N; f++)
    {

      /* Se asume que no se puede volver al mismo nodo */
        new_v_f = new_vertices[f];

        /* Se calcula la distancia Manhatan */
        new_distancia = distancia_rectilinea(new_v_i, new_v_f);
        
        /* Se almacena el edge */
        new_edges[i][f] = new_distancia;
    }
  }
  /////////// IMPLEMENTADO ///////////


  /////////// KRUSKA v2 ///////////
  /* Se inicializan los objetos a trabajar */
  int* new_graph[N];
  for (int i = 0; i < N; i ++)
  {
    new_graph[i] = calloc(N, sizeof(int));
  }

  Edge* new_E = calloc(N*N, sizeof(Edge));

  /* Se crea el arreglo de edges */
  for (int i = 0; i < N; i++)
  {
      for (int j = 0; j < N; j++)
      {
          new_E[i*N + j].from = i; 
          new_E[i*N + j].to = j; 
          new_E[i*N + j].weight = new_edges[i][j];
      }
  }

  /* Ejecutamos Kruskal MST */
  MST = Kruskal(N, N*N, N, new_E, new_graph);
  printf("El nuevo MTS es: %i\n", MST);  
  /////////// KRUSKAL v2 ///////////



 ////////// IMPLEMENTADO ///////////
  /* Escritura del archivo */
  fprintf(output_stream, "%i\n", N);
  escribir_en_archivo(output_stream, N, new_graph, new_vertices); // Cambiar el -M
  ////////// IMPLEMENTADO ///////////



  /////// LIBERAR MEMORIA ///////
  /* Se libera el calloc asociado a cada fila */
  for (int i = 0; i < N; i++)
  {
    free(new_edges[i]);
  }

  /* Se libera el calloc asociado a cada fila */
  for (int i = 0; i < N; i++)
  {
    free(new_graph[i]);
  }

  /* Se libera el calloc del array */
  free(new_E);
  /////// LIBERAR MEMORIA ///////


  /////// LIBERAR MEMORIA ///////
  /* Se libera el calloc asociado a cada fila */
  for (int i = 0; i < N-M; i++)
  {
    free(edges[i]);
  }

  /* Se libera el calloc asociado a cada fila */
  for (int i = 0; i < N-M; i++)
  {
    free(graph[i]);
  }

  /* Se libera el calloc del array */
  free(E);


  for (int i = 0; i < size; i++)
  {
    free(existe_punto[i]);
  }
  /////// LIBERAR MEMORIA ///////


  // Cerrar archivo de input
  fclose(input_stream);

  // Cerrar archivo de output
  fclose(output_stream);

  return 0;
}