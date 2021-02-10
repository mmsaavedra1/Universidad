#include "mould.h"
#include <stdlib.h>
#include <stdio.h>

Cell* add_cell (int* id) {
    // Se crea memoria dinamica para alojar lo esperado
    Cell* child = (Cell*) malloc(sizeof(Cell));
    // Se asigna su id
    child->id = *id;

     // Se da el paso del ID
    *id +=1;

    // Se dice que no posee hijas
    for (int i = 0; i < 10; i++){
        child->children[i] = NULL;
    }
    // Se asigna el valor a su mama
    return child;
}

Cell* copy_cell(Cell* cell_to_clone, int* id) {
    if (cell_to_clone != NULL) {
        // Creamos una nueva para su clon
        Cell* new = add_cell(id);

        // Se recorren todas las hijas y se clonan
        for (int i = 0; i < 10; i++) {
            new->children[i] = copy_cell(cell_to_clone->children[i], id);
        }
        // Cierra la recursion
        return new;
    }
    //Cierra la recursion cuando hay nada
    Cell* new = NULL;
    return new;
}

Cell* copy_absorb(Cell* cell_to_clone) {
    if (cell_to_clone != NULL) {
        // Creamos una nueva para su clon
        Cell* new = (Cell*) malloc(sizeof(Cell));
        new->id = cell_to_clone->id;
        printf("Creando el ID: %d\n", new->id);

        // Se recorren todas las hijas y se clonan
        for (int i = 0; i < 10; i++) {
            new->children[i] = copy_absorb(cell_to_clone->children[i]);
        }
        // Cierra la recursion
        return new;
    }
    //Cierra la recursion cuando hay anda
    Cell* new = NULL;
    return new;
}

void free_mould (Cell* cell) {
    // Funcion que libera la memoria del sistema
    for (int i = 0; i < 10; i++){
        if (cell->children[i] != NULL){
            free_mould(cell->children[i]);
        }
    }
    
    printf("Liberando memoria de data de ID: %d\n", cell->id);
    free(cell);
    return;
}
