#include "kruskalv2.h"

void init(int vertices)
{
    int iter=0;
    for(iter=0;iter<vertices;iter++)
    {
        parent[iter]=-1;
    }

}

int compare(const void * x,const void * y)
{
        return (*(Edge *)x).weight - (*(Edge *)y).weight;
}


int Find(int vertex)
{
    if(parent[vertex]==-1)return vertex;
    return parent[vertex] = Find(parent[vertex]); /* Finding its parent as well as updating the parent 
                                                        of all vertices along this path */
}


int Union(int parent1, int parent2)
{
    /* This can be implemented in many other ways. This is one of them */
    parent[parent1] = parent2;
    return 0;
}


int Kruskal(int vertices, int edges, int N, Edge E[N*N], int* graph[N])
{
    /* Retorna el valor del MST*/
    int MST = 0;

    for (int i = 0; i < N; i++)
    {
        memset(graph[i],-1,sizeof(int)*N); /* -1 represents the absence of edge between them */
    }


    /* Sort the edges according to the weight */
    qsort(E, edges,sizeof(Edge),compare);

    /* Initialize parents of all vertices to be -1.*/
    init(vertices);
                        printf("oa\n");

    int totalEdges = 0,edgePos=0,from,to,weight;
    Edge now;

    while(totalEdges < vertices -1)
    {
            if(edgePos==edges)
            {
                    /* Input Graph is not connected*/
                    exit(0);
            }
            now = E[edgePos++];
            from = now.from;
            to = now.to;
            weight=now.weight;
            /* See If vetices from,to are connected. If they are connected do not add this edge. */
            int parent1 = Find(from);
            int parent2 = Find(to);
            if(parent1!=parent2)
            {
                    graph[from][to] = weight;
                    Union(parent1,parent2);
                    totalEdges++;
                    MST += weight;
            }
    }

    return MST;

}


/* Printing the MST */
void imprimir_kruskal(int N, int* graph[N])
{
    for(int iter = 0; iter < N; iter++)
    {
            for(int jter=0; jter < N; jter++)
            {
                    if(graph[iter][jter]!=-1)
                    {
                            printf("Vertex %d and %d, weight %d\n",iter,jter,graph[iter][jter]);
                    }
            }
    }
}







