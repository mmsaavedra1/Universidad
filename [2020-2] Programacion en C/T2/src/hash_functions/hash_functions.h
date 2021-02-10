#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Funcion de incrementos. Rescatada de: http://www.cse.yorku.ca/~oz/hash.html*/
unsigned long int funcion_incremento(char string[]);

/* Funcion de ajuste */
unsigned long int funcion_ajuste(unsigned long int k, unsigned int m);

