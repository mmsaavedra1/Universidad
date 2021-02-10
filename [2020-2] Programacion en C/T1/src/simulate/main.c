#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "simulation.h"
#include "../visualizer/visualizer.h"

////////// INTEGRADO //////////
#include <math.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
////////// INTEGRADO //////////


////////// INTEGRADO //////////
typedef struct Nodo {
  struct Nodo* hijo_izquierdo;
  struct Nodo* hijo_derecho;
  int largo_segmentos;
  int profundidad;
  Segment* segmentos;
  BoundingBox caja;
  bool es_hoja;
} Nodo;

////////// INTEGRADO //////////



////////// INTEGRADO //////////
double max(double num1, double num2) {
   if (num1 > num2)
      return num1;
   else
      return num2;
}

double min(double num1, double num2) {
   if (num1 < num2)
      return num1;
   else
      return num2;
}


void max_min(double* min_x, double* max_x, double pi_x, double pf_x, double* min_y, double* max_y, double pi_y, double pf_y) {
  if (pi_x <= *min_x) {
    *min_x = pi_x;
  }
  else if (pf_x <= *min_x) {
    *min_x = pf_x;
  }
  if (pi_x >= *max_x) {
    *max_x = pi_x;
  }
  else if (pf_x >= *max_x) {
    *max_x = pf_x;
  }
  
  if (pi_y <= *min_y) {
    *min_y = pi_y;
  }
  else if (pf_y <= *min_y) {
    *min_y = pf_y;
  }
  if (pi_y >= *max_y) {
    *max_y = pi_y;
  }
  else if (pf_y >= *max_y) {
    *max_y = pf_y;
  }
}
////////// INTEGRADO //////////

////////// INTEGRADO //////////
void swap(Segment* a, Segment* b) 
{ 
    Segment t = *a; 
    *a = *b; 
    *b = t; 
} 

/* Codigo basado en la logica de GeeksForGeeks disponible en https://www.geeksforgeeks.org/quick-sort/  */
int particion (Segment segmentos[], int minimo, int maximo, bool es_x) 
{ 
  /* Analiza si el wachin de aca es busqueda de mediana X */
  if (es_x == true) {
    double pivote_x = (segmentos[maximo].pi.x + segmentos[maximo].pf.x)/2;
    int i = minimo - 1;
    
    for (int j = minimo; j < maximo; j++) { 
      double xi = segmentos[j].pi.x;
      double xf = segmentos[j].pf.x;
      double diferencia_x = (xi + xf)/2;

      if (diferencia_x < pivote_x) { 
        i++;
        swap(&segmentos[i], &segmentos[j]); 
      }
    } 
  
    swap(&segmentos[i + 1], &segmentos[maximo]); 
    i++;
    return i;
  }
  else{
    double pivote_y = (segmentos[maximo].pi.y + segmentos[maximo].pf.y)/2;
    int i = minimo - 1;

    for (int j = minimo; j < maximo; j++) { 
      double yi = segmentos[j].pi.y;
      double yf = segmentos[j].pf.y;
      double diferencia_y = (yi + yf)/2;

      if (diferencia_y < pivote_y) { 
        i++;
        swap(&segmentos[i], &segmentos[j]); 
      }
    } 
  
    swap(&segmentos[i + 1], &segmentos[maximo]); 
    i++;
    return i;
  }
}
////////// INTEGRADO //////////



////////// INTEGRADO //////////
/* Codigo basado en la logica de GeeksForGeeks para QuickSort disponible en: https://www.geeksforgeeks.org/quick-sort/ */
void quickSort(Segment segmentos[], int minimo, int maximo, bool es_x) 
{ 
  if (minimo < maximo) 
  { 
    int particion_i = particion(segmentos, minimo, maximo, es_x); 

    quickSort(segmentos, minimo, particion_i - 1, es_x); 
    quickSort(segmentos, particion_i + 1, maximo, es_x); 
  } 
} 
////////// INTEGRADO //////////



////////// INTEGRADO //////////
void printArray(Segment arr[], int size, int profundidad) 
{ 
  printf("Medianas en profundidad: %d\n", profundidad);
  for (int i = 0; i < size; i++){
    if (profundidad % 2 == 0) {
      printf("Diferencia X: %f\n", fabs(arr[i].pi.x + arr[i].pf.x)/2);
    }
    else{
      printf("Diferencia Y: %f\n", fabs(arr[i].pi.y + arr[i].pf.y)/2); 
    }
  }
}

void dimensionesCaja(BoundingBox caja) {
  printf("Minimo punto: (%f,%f)\n Maximo punto: (%f, %f)\n", caja.min_point.x, caja.min_point.y, caja.max_point.x, caja.max_point.y);
}

void printSegment(Segment segmentos[], int largo) {
  for (int i = 0; i < largo; i++) {
    printf("Punto inicial: (%f,%f) - Punto final: (%f, %f)\n", segmentos[i].pi.x, segmentos[i].pi.y, segmentos[i].pf.x, segmentos[i].pf.y);
  }
}
////////// INTEGRADO //////////



////////// INTEGRADO //////////
bool punto_en_caja(Vector vector, BoundingBox caja) {
  double x = vector.x;
  double y = vector.y;

  double min_x = caja.min_point.x;
  double max_x = caja.max_point.x;
  double min_y = caja.min_point.y;
  double max_y = caja.max_point.y;

  /* Si esta dentro de la caja se retorna true */
  if ( ((min_x <= x) && (x <= max_x)) && ((min_y <= y) && (y <= max_y) )) {
    return true;
  }
  else{
    return false;
  }
}
////////// INTEGRADO //////////



////////// INTEGRADO //////////
Nodo* crear_hijo (Nodo* parent, bool es_izquierdo) {
  
  Nodo* hijo = (Nodo*) malloc(sizeof(Nodo));

  hijo->hijo_izquierdo = NULL;
  hijo->hijo_derecho = NULL;
  hijo->profundidad = parent->profundidad+1;

  parent->es_hoja = false;
  hijo->es_hoja = true;

  bool es_x;
  if (parent->profundidad % 2 == 0){
    es_x = true;
  }
  else{
    es_x = false;
  }

  /* Punto base la mediana */

  hijo->caja.min_point.x = parent->caja.min_point.x;
  hijo->caja.min_point.y = parent->caja.min_point.y;
  hijo->caja.max_point.x = parent->caja.max_point.x;
  hijo->caja.max_point.y = parent->caja.max_point.y;
  

  //double mediana = algoritmo_mediana(parent->segmentos, 0, parent->largo_segmentos -1, es_x, parent->largo_segmentos);

  /* Primer caso de mi pizarra -> corte vertical */
  if (es_x == true) {
    /* Se arregla la caja si es hijo izquierdo o derecho */
    if (es_izquierdo == true) {
      hijo->caja.max_point.x = (parent->caja.min_point.x + parent->caja.max_point.x) / 2;
    }
    else{
      hijo->caja.min_point.x = (parent->caja.min_point.x + parent->caja.max_point.x) / 2;
    }
  }
  else {
    /* Se arregla la caja si es hijo izquierdo o derecho */
    if (es_izquierdo == true) {
      hijo->caja.max_point.y = (parent->caja.min_point.y + parent->caja.max_point.y) / 2;
    }
    else{
      hijo->caja.min_point.y = ( parent->caja.min_point.y + parent->caja.max_point.y) / 2;
    }
  }

  /* Se agregan hijos si corresponde */
  int largo=0;
  for (int i = 0; i < parent->largo_segmentos; i++) {
    Segment segmento = parent->segmentos[i];
    
    
    if (es_x == true) {
      
    double min_x = min(segmento.pi.x, segmento.pf.x);
    double max_x = max(segmento.pi.x, segmento.pf.x);
    /* Se arregla la caja si es hijo izquierdo o derecho */
      if (es_izquierdo == true) {
        /* Maximo punto debe estar en la caja */
        if ( (max_x <= hijo->caja.max_point.x) || (min_x <= hijo->caja.max_point.x)) {
          largo++;
        }
      }
      else{
        if ( (min_x >= hijo->caja.min_point.x) ||  (max_x >= hijo->caja.min_point.x) ){
          largo++;
        }
      }
    }
    else {

    double min_y = min(segmento.pi.y, segmento.pf.y);
    double max_y = max(segmento.pi.y, segmento.pf.y);
      /* Se arregla la caja si es hijo izquierdo o derecho */
      if (es_izquierdo == true) {
        if ( (max_y <= hijo->caja.max_point.y) || (min_y<= hijo->caja.max_point.y)) {
          largo++;
        }
      }
      else{
         if ( (min_y >= hijo->caja.min_point.y) ||  (max_y >= hijo->caja.min_point.y) ){
          largo++;
        }
      }
    }    
  }

  hijo->segmentos = calloc(largo, sizeof(Segment));
  hijo->largo_segmentos = largo;

  int indice = 0;
  for (int i = 0; i < parent->largo_segmentos; i++) {
    Segment segmento = parent->segmentos[i];
    // Se comprueba que esta dentro de la caja
    
    if (es_x == true) {
    /* Se arregla la caja si es hijo izquierdo o derecho */
      if (es_izquierdo == true) {
        /* Maximo punto debe estar en la caja */
        if ( (max(segmento.pi.x, segmento.pf.x) <= hijo->caja.max_point.x) || (min(segmento.pi.x, segmento.pf.x) <= hijo->caja.max_point.x)) {
          hijo->segmentos[indice] = segmento;
          indice++;
        }
      }
      else{
        if ( (min(segmento.pi.x, segmento.pf.x) >= hijo->caja.min_point.x) ||  (max(segmento.pi.x, segmento.pf.x) >= hijo->caja.min_point.x) ){
          hijo->segmentos[indice] = segmento;
          indice++;
        }
      }
    }
    else {
      /* Se arregla la caja si es hijo izquierdo o derecho */
      if (es_izquierdo == true) {
        if ( (max(segmento.pi.y, segmento.pf.y) <= hijo->caja.max_point.y) || (min(segmento.pi.y, segmento.pf.y) <= hijo->caja.max_point.y)) {
          hijo->segmentos[indice] = segmento;
          indice++;
        }
      }
      else{
         if ( (min(segmento.pi.y, segmento.pf.y) >= hijo->caja.min_point.y) ||  (max(segmento.pi.y, segmento.pf.y) >= hijo->caja.min_point.y) ){
          hijo->segmentos[indice] = segmento;
          indice++;
        }
      }
    }
  }
  
  /*
  if (es_izquierdo){
    visualizer_set_color(255,0,0);
  }
  else{
    visualizer_set_color(0,0,255);
  }
  visualizer_draw_box(hijo->caja);
  */
 
  return hijo;
}


void insertar_nodo(Nodo* parent) {
  /* Si tiene solamente 2 o menos segmentos se corta*/
  if ( parent->largo_segmentos < 200 ) {
    return;
  }
  /* Si tiene mas de dos segmentos se crean hijos*/
  else{
  
    /* Creacion recurisva de los hijos */
    parent->hijo_izquierdo = crear_hijo(parent, true);
    parent->hijo_derecho = crear_hijo(parent, false);

    insertar_nodo(parent->hijo_izquierdo);
    insertar_nodo(parent->hijo_derecho);

    return;
  }
}
////////// INTEGRADO //////////



////////// INTEGRADO //////////
void search(Particle* particula, Nodo* nodo) {
  /* Si se llega al final de la base se analizan los nodos */
  if ( nodo->es_hoja ) {    
    for (int s = 0; s < nodo->largo_segmentos; s++) 
      {
        // Si la particula choca con el segmento
        if (particle_segment_collision(*particula, nodo->segmentos[s])) {
          // Si es que no ha chocado con nada, o si no desempatamos por ID
          if(!particula->intersected_segment || nodo->segmentos[s].ID < particula->intersected_segment->ID)
          {
            particula->intersected_segment = &nodo->segmentos[s];
          }
        }
      }
    return;
  }
  else{
   
    if ( particle_boundingbox_collision(*particula, nodo->hijo_izquierdo->caja) ) {
        search(particula, nodo->hijo_izquierdo); 
      }
    if (  particle_boundingbox_collision(*particula, nodo->hijo_derecho->caja)) {
        search(particula, nodo->hijo_derecho);
      }
  }
}
////////// INTEGRADO //////////


////////// INTEGRADO //////////
void liberar_memoria(Nodo* nodo) {
  if (nodo->es_hoja) {
    return;
  }
  else{
    /* Llamada recursiva para eliminar */
    liberar_memoria(nodo->hijo_izquierdo);
    liberar_memoria(nodo->hijo_derecho);

    free(nodo->hijo_izquierdo->segmentos);
    free(nodo->hijo_derecho->segmentos);

    free(nodo->hijo_izquierdo);
    free(nodo->hijo_derecho);
  }
}
////////// INTEGRADO //////////


////////// INTEGRADO //////////
void ver_final(Nodo* nodo) {
  if (nodo->es_hoja) {
    printSegment(nodo->segmentos, nodo->largo_segmentos);
    printf("Largo de segmentos: %d", nodo->largo_segmentos);
    exit(0);
  }
  else{
    ver_final(nodo->hijo_izquierdo);
    ver_final(nodo->hijo_derecho);
  }
}
////////// INTEGRADO //////////



int main(int argc, char** argv) 
{
  // Por defecto se abre la ventana
  bool visualize = true;
  if (argc == 4 && !strcmp(argv[3], "--novis"))
  {
    visualize = false;  
  }
  else if(argc < 3|| argc >= 4)
  {
    printf("Modo de uso: %s INPUT OUTPUT [--novis]\n", argv[0]);
    printf("Donde:\n");
    printf("\tINPUT es la ruta al archivo de input que describe la escena\n");
    printf("\tOUTPUT es la ruta al archivo en donde se reportarán las colisiones\n");
    printf("\tEl flag opcional --novis indica que no se debe abrir la visualización del programa\n");
    // Exit code 1: Programa llamado sin todos los argumentos
    return 1;
  }
  
  // Inicializa los elementos de la simulación, y abre la ventana si visualize es true
  Simulation* sim = simulation_init_from_file(argv[1], visualize);

  // El archivo donde iremos reportando las colisiones
  FILE* output_file = fopen(argv[2], "w");


  quickSort(sim->segments, 0, sim->segment_count-1, sim->segment_count);

  ////////// INTEGRADO //////////
  /* Creacion de las estructuras por utilizar */
  Nodo* raiz = (Nodo*) malloc(sizeof(Nodo));
  
  /* Seteo de los valores base de las estructuras */
  raiz->hijo_izquierdo = NULL;
  raiz->hijo_derecho = NULL;
  raiz->largo_segmentos = sim->segment_count;
  raiz->profundidad = 0;
  raiz->es_hoja = true;
  raiz->segmentos = calloc(sim->segment_count, sizeof(Segment));

  int largo = sim->segment_count;

  raiz->caja.min_point.x = min(sim->segments[largo-1].pi.x, sim->segments[largo-1].pf.x);
  raiz->caja.min_point.y = min(sim->segments[largo-1].pi.y, sim->segments[largo-1].pf.y);
  raiz->caja.max_point.x = max(sim->segments[0].pi.x, sim->segments[0].pf.x);
  raiz->caja.max_point.y = max(sim->segments[0].pi.y, sim->segments[0].pf.y);

  /* Se crea la raiz con todos los segmentos que existen hasta ahora */
  for (int i = 0; i < sim->segment_count; i++){
    raiz->segmentos[i] = sim->segments[i];
    max_min(&raiz->caja.min_point.x, &raiz->caja.max_point.x, raiz->segmentos[i].pi.x, raiz->segmentos[i].pf.x, &raiz->caja.min_point.y, &raiz->caja.max_point.y, raiz->segmentos[i].pi.y, raiz->segmentos[i].pf.y);
  }
 
  /* Se almacena la raiz dentro del arbol de estructura y se pobla la estructura */
  insertar_nodo(raiz);
  /*
  visualizer_draw_box(raiz->caja);
  visualizer_draw_box(raiz->hijo_izquierdo->caja);
  */


  //ver_final(raiz);

  /*
  Nodo* nodo = raiz->hijo_izquierdo->hijo_izquierdo->hijo_izquierdo;
  printArray(nodo->segmentos, nodo->largo_segmentos, nodo->profundidad);
  printSegment(nodo->segmentos, nodo->largo_segmentos);
  dimensionesCaja(nodo->caja);
  visualizer_set_color(255,0,0);
  visualizer_draw_box(nodo->caja);

  /////// INTEGRADO ////////
  liberar_memoria(raiz);
  free(raiz->segmentos);
  free(raiz);
 
  /////// INTEGRADO ////////
  
  exit(0);
  ////////// INTEGRADO //////////
  */
 
  // Para cada frame
  for (int f = 0; f < sim->frames; f++) 
  {
    // Para cada particula
    for (int p = 0; p < sim->particle_count; p++) 
    {
      // Inicialmente, esta particula no ha chocado con ningun segmento
      sim->particles[p].intersected_segment = NULL;
      // Por cada segmento
      // TODO: No revisar todos los segmentos, usar BVH para descartar los que estén muy lejos
      
      /*
      for (int s = 0; s < sim->segment_count; s++) 
      {
        // Si la particula choca con el segmento
        if (particle_segment_collision(sim->particles[p], sim->segments[s])) {
          // Si es que no ha chocado con nada, o si no desempatamos por ID
          if(!sim->particles[p].intersected_segment || sim->segments[s].ID < sim->particles[p].intersected_segment->ID)
          {
            sim->particles[p].intersected_segment = &sim->segments[s];
          }
        }
      }
      */
      
     
      /////////// IMPLEMENTACION V1 ///////////
      search(&sim->particles[p], raiz);
      /////////// IMPLEMENTACION V 1///////////
      

      // Si hubo intersección
      if(sim->particles[p].intersected_segment)
      {
        // Desviamos la partícula según el segmento con el que chocó
        particle_bounce_against_segment(&sim->particles[p], *sim->particles[p].intersected_segment);

        // Reportamos la colisión en el archivo de output
        fprintf(output_file, "%d %d %d\n", f, sim->particles[p].ID, sim->particles[p].intersected_segment->ID);
        // Finalmente, la particula avanza 
      }
     
      particle_move(&sim->particles[p]);
      
    }
    // Si la ventana está abierta, dibujar las particulas en sus nuevas posiciones
    visualizer_draw_particles(sim->particles, sim->particle_count);
  }
  // Hace free de todo lo que se creo en simulation_init. Cierra la ventana.
  simulation_destroy(sim);


  /////// INTEGRADO ////////
  liberar_memoria(raiz);
  free(raiz->segmentos);
  free(raiz);
  /////// INTEGRADO ////////


  fclose(output_file);

  return 0;
}
