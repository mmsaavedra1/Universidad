#include "BST_tree.h"


void entregar_subarbol(int h, unsigned long int nodo, char nodos[], char buffer[])
{
    /* Se asigna una variable indice */
    unsigned long int indice = 3;

    /* Se asignan los valores indice del caso base */
    unsigned long int padre = nodo;
    unsigned long int hijo_izq = 2*padre;
    unsigned long int hijo_der = hijo_izq+1;

    /* Se lee el caso base */
    buffer[0] = nodos[padre];
    buffer[1] = nodos[hijo_izq];
    buffer[2] = nodos[hijo_der];

    unsigned long int inicio = 2*hijo_izq;
    /* Se analiza el caso general h >= 3 */
    for (int h_prima = 3; h_prima <= h; h_prima++)
    {
        for (unsigned long int i = 0; i < pow(2, h_prima-1); i++)
        {
            /* Se alamcenan los valores correspondientes en el buffer */
            buffer[indice] = nodos[inicio+i];
            indice++;
        }
        inicio = 2*inicio;
    }
}
