#pragma once
#include "Video.h"

class Capitulo :
public Video {
private:
	int numeroDeCapitulo;
	int numeroDeTemporada;
	string serieALaQuePertenece;

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
		ar& numeroDeCapitulo;
		ar& numeroDeTemporada;
		ar& serieALaQuePertenece;
	}

public:
	Capitulo(){};
	Capitulo(string , string , string , float , float , int , int , string );
	void setNumeroDeCapitulo(int);
	int getNumeroDeCapitulo();
	void setNumeroDeTemporada(int);
	int getNumeroDeTemporada();
	void setSerieALaQuePertenece(string);
	string getSerieALaQuePertenece();
	void describe();
};

Capitulo::Capitulo(string Nombre, string Path, string Genero, float Duracion, float Rating, 
	int NumeroDeCapitulo, int NumeroDeTemporada, string SerieALaQuePertenece) :
	Video(Nombre, Path, Genero, Duracion, Rating) {

	this->numeroDeCapitulo = NumeroDeCapitulo;
	this->numeroDeTemporada = NumeroDeTemporada;
	this->serieALaQuePertenece = SerieALaQuePertenece;
}

void Capitulo::setNumeroDeCapitulo(int n) {
	this->numeroDeCapitulo = n;
}

int Capitulo::getNumeroDeCapitulo() {
	return this->numeroDeCapitulo;
}

void Capitulo::setNumeroDeTemporada(int n) {
	this->numeroDeTemporada = n;
}

int Capitulo::getNumeroDeTemporada() {
	return this->numeroDeTemporada;
}


void Capitulo::setSerieALaQuePertenece(string s) {
	this->serieALaQuePertenece = s;
}

string Capitulo::getSerieALaQuePertenece() {
	return this->serieALaQuePertenece;
}

void Capitulo::describe() {
	Video::describe();
	std::cout <<
		"Capitulo:\t" << this->numeroDeCapitulo << '\n' <<
		"Temporada:\t" << this->numeroDeTemporada << '\n' <<
		"Serie:\t\t" << this->serieALaQuePertenece << '\n';


}
