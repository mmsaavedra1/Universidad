#include "../visualizer/visualizer.h"
#include <stdio.h>
#include <unistd.h>
#include <string.h>

bool check_arguments(int argc, char** argv)
{
  if(!(argc == 3 || argc == 4)) return false;
  if(argc == 4)
  {
    if(!strcmp(argv[3], "--novis"))
    {
      visualizer_disable();
    }
    else return false;
  }  
  return true;
}

int main(int argc, char** argv)
{
  if(!check_arguments(argc,argv))
  {
    printf("Modo de uso: %s input output [--novis]\nDonde:\n", argv[0]);
    printf("\t\"input\" es la ruta al archivo de input\n");
    printf("\t\"output\" es la ruta al archivo de output\n");
    printf("\t\"--novis\" es el flag opcional que desactiva el visualizador\n");
    return 1;
  }

  // Abrimos el archivo de input
  FILE* input_stream = fopen(argv[1], "r");

  // Abrimos el archivo de output
  FILE* output_stream = fopen(argv[2], "w");

  // Si alguno de los dos archivos no se pudo abrir
  if(!input_stream)
  {
    printf("El archivo %s no existe o no se puede leer\n", argv[1]);
    return 2;
  }
  if(!output_stream)
  {
    printf("El archivo %s no se pudo crear o no se puede escribir\n", argv[2]);
    printf("Recuerda que \"fopen\" no puede crear carpetas\n");
    fclose(input_stream);
    return 3;
  }


  // leemos el tamaño del tablero
  int N;
  fscanf(input_stream, "%d", &N);

  // inicializamos la interfaz
  visualizer_open(N,N);

  // leemos el numero en cada celda del tablero
  int cell;
  // leemos cada valor del tablero: cada fila
  for (int row = 0; row < N; row++)
  {
    // y cada columna dentro de esa fila
    for (int col = 0; col < N; col++)
    {
      fscanf(input_stream, "%d", &cell);
      if (cell == -1)
      {
        // indicamos que la celda (row,col) tiene color rojo
        visualizer_set_cell_color(row, col, RED);
      }
      else if (cell > 0)
      {
        // indicamos que la celda (row,col) tiene color azul
        visualizer_set_cell_color(row, col, BLUE);
        // asignamos el grado a la celda (row,col)
        visualizer_set_cell_degree(row, col, cell);
      }
      else
      {
        // indicamos que la celda (row,col) no tiene color (aun)
        visualizer_set_cell_color(row, col, NONE);
      }
      
    }
  }
  // actualizamos el contenido de la ventana
  visualizer_redraw();

  // [Aqui va tu tarea]

  // cerramos el archivo de input
  fclose(input_stream);

  // Hacemos sleep por 1 segundos para ver los cambios
  // (eliminar todos los sleeps al entregar tarea)
  sleep(1);

  // destacamos una celda especifica y luego lo borramos
  visualizer_set_cell_highlight(0,1, true);
  visualizer_redraw();

  // Hacemos sleep por 1 segundo para ver los cambios
  sleep(1);

  visualizer_set_cell_highlight(0,1, false);
  visualizer_redraw();

  // Hacemos sleep por 1 segundo para ver los cambios
  sleep(1);

  // [Aqui termina tu tarea]

  // cerramos la ventana
  visualizer_close();

  // acá escribes tu tarea en output
  // cerramos el archivo de output
  fclose(output_stream);

  return 0;
}