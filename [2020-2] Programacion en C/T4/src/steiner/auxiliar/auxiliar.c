#include "auxiliar.h"

/////////// IMPLEMENTADO ///////////
/* Funcion para calcula la distancia */
int distancia_rectilinea(Vertice u, Vertice v)
{
  int valor = abs(u.x - v.x) + abs(u.y - v.y);
  return valor;
}
/////////// IMPLEMENTADO ///////////


/////////// IMPLEMENTADO ///////////
void imprimir_matriz_adyacencia(int N, int* arco[N])
{
  for (int i = 0; i < N; i++)
  {
    for (int f = 0; f < N; f++)
    {
      printf("%i ", arco[i][f]);
    }
    printf("\n");
  }
}
/////////// IMPLEMENTADO ///////////

/////////// IMPLEMENTADO ///////////
/* Funcion que escribe en el documentos las aristas conectadas */
void escribir_en_archivo(FILE* file, int N, int* graph[N], Vertice vertices[N])
{
  for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < N; j++)
      {
        if(graph[i][j] != -1)
        {
          fprintf(file, "%i %i %i %i\n", vertices[i].y, vertices[i].x, vertices[j].y, vertices[j].x);
        }
      }
    }
}
/////////// IMPLEMENTADO ///////////



/////////// IMPLEMENTADO ///////////
int max(int num1, int num2) {
   if (num1 > num2)
      return num1;
   else
      return num2;
}

int min(int num1, int num2) {
   if (num1 < num2)
      return num1;
   else
      return num2;
}
/////////// IMPLEMENTADO ///////////

