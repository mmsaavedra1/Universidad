#pragma once

typedef struct Cell
{
    int id;
    struct Cell* children[10];
} Cell;
