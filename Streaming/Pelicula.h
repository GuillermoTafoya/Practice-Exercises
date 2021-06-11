#pragma once
#include "Video.h"


class Pelicula :
    public Video {

private:
    string reparto;
    friend class boost::serialization::access;
    template<class Archive>
    void serialize(Archive& ar, const unsigned int version)
    {
        ar& name;
        ar& genero;
        ar& duracion;
        ar& rating;
        ar& ratingAcumulado;
        ar& usuariosCalificados;
        ar& path;
        ar& reparto;
    }
public:
    Pelicula() {};
    Pelicula(string Nombre, string Path, string Genero, float Duracion, float Rating, string Reparto);
    string getReparto();
    void setReparto(string);
    void describe();

};


Pelicula::Pelicula(string Nombre, string Path, string Genero, float Duracion, float Rating, string Reparto) {
    this->name = Nombre;
    this->path = Path;
    this->duracion = Duracion;
    this->rating = Rating;
    this->genero = Genero;
    this->ratingAcumulado = Rating;
    this->usuariosCalificados = 1;
    this->reparto = Reparto;
}

string Pelicula::getReparto() {
    return  this->reparto;
}

void Pelicula::setReparto(string rep) {
    this->reparto = rep;
}

void Pelicula::describe() {
    Video::describe(); 
    std::cout <<
        "Reparto:\t" << this->reparto << '\n';
}