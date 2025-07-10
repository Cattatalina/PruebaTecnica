// Pregunta 2: Estructuras de Datos (30 puntos)
// Debido a que en el documento no especifica lenguaje, usé C++.


#ifndef COLAMINIMO_H
#define COLAMINIMO_H

#include <queue>
#include <deque>
#include <iostream>


class ColaMinimo {
private:
    std::queue<int> cola;
    std::deque<int> colaMin;

public:
    void encolar(int valor);
    void desencolar();
    int minimo();
};

#endif