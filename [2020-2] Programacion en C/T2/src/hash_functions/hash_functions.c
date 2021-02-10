#include "hash_functions.h"


/* Funcion de incrementos. Rescatada de: http://www.cse.yorku.ca/~oz/hash.html*/
unsigned long int funcion_incremento(char string[])
{
    unsigned long int hash = 5381;  // Valor entregado por el paper
    int c;

    /* Depende si es el buffer o no */
    
    c = string[0];  // Valor ASCII "1" o "0"
     
    while (c)
    {
        hash = ((hash << 5) + hash) + c;
        c = *string++;
    }
    return hash;
}


/* Funcion de ajuste */
unsigned long int funcion_ajuste(unsigned long int k, unsigned int m)
{
    double entero;
    double phi = (1.0+sqrt(5.0))/2.0;                                                   // Se define phi para ser usado
    unsigned long int ajuste = (unsigned long int) floor( modf(k/phi, &entero)*m );     // Se realiza el ajuste apropiado

    return ajuste;
}