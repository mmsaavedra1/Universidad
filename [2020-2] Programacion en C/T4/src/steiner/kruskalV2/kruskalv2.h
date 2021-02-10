#pragma once

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define maxVertices 5096

/* Input graph must be undirected,weighted and connected*/
typedef struct Edge
{
        int from,to,weight;
}Edge;


/* Variables globales */
int parent[maxVertices];


void init(int vertices);
int compare(const void * x,const void * y);
int Find(int vertex);
int Union(int parent1,int parent2);
int Kruskal(int vertices, int edges, int N, Edge E[N*N], int* graph[N]);
void imprimir_kruskal(int N, int* graph[N]);
