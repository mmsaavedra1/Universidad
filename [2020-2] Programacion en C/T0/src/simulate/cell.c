#include "cell.h"
#include <stdlib.h>
#include <stdio.h>

void observe (Cell* cell, int spacing, int idx, FILE* file) {
    // Se crea el espaciado
    for (int i = 0; i < spacing; i++){
        fprintf(file, "   ");
    }
    // Se guarda lo solicitado
    if (idx == -1) {
        fprintf(file, "r:0\n");
    }
    else{
        fprintf(file, "%d:%d\n", idx, cell->id);
    }
    // Se realiza para las hijas
    for (int i = 0; i < 10; i++) {
        if (cell->children[i] != NULL){
            observe(cell->children[i], spacing+1, i, file);
        }
    }
}