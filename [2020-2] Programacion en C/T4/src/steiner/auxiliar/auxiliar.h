#pragma once
#include <stdio.h>
#include <stdlib.h>



/* Estructura que almacena la informacion de cada nodo */
typedef struct {
    int first;
    int second;
    int weight;
} weighted_edge;

/* Representa un nodo/vertice */
typedef struct {
  int x;
  int y;
} Vertice;


/* Prototipado de funciones */
int distancia_rectilinea(Vertice u, Vertice v);
void imprimir_matriz_adyacencia(int N, int* arco[N]);
void escribir_en_archivo(FILE* file, int N, int* graph[N], Vertice vertices[N]);
int max(int num1, int num2);
int min(int num1, int num2);

