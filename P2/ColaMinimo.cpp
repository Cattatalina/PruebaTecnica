// Pregunta 2: Estructuras de Datos (30 puntos)
// Debido a que en el documento no especifica lenguaje, usé C++.


#include "ColaMinimo.h"

void ColaMinimo::encolar(int valor) {
    cola.push(valor);

    while (!colaMin.empty() && colaMin.back() > valor) {
        colaMin.pop_back();
    }
    colaMin.push_back(valor);
}

void ColaMinimo::desencolar() {
    if (colaMin.empty()) {
        throw std::runtime_error("Error: La Cola está vacía.");
    }

    int valor = cola.front();
    cola.pop();

    if (!colaMin.empty() && colaMin.front() == valor) {
        colaMin.pop_front();
    }
}

int ColaMinimo::minimo() {
    if (colaMin.empty()) {
        throw std::runtime_error("Error: La Cola está vacía.");
    }
    return colaMin.front();
}