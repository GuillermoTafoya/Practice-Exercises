#pragma once
#include "Capitulo.h"

using string = std::string;
class Temporada {	
	int capitulosTotales, numeroDeTemporada;
	float duracionTemporada, ratingTemporada;
	string serieALaQuePertenece = "Ninguna";

	std::vector <Capitulo> CapitulosDeLaTemporada;

	friend class boost::serialization::access;
	template<class Archive>
	void serialize(Archive& ar, const unsigned int version)
	{
		
		ar& CapitulosDeLaTemporada;
		ar& capitulosTotales;
		ar& numeroDeTemporada;
		ar& duracionTemporada; 
		ar& ratingTemporada;
		ar& serieALaQuePertenece;
	}

public:
	Temporada() {};

	int exists(string);

	void setCapitulosTotales();
	void setNumeroDeTemporada(int);
	void setDuracionTemporada();
	void setRatingTemporada();
	void setSerieALaQuePertenece(string);
	

	int getCapitulosTotales();
	int getNumeroDeTemporada();
	int getDuracionTemporada();
	int getRatingTemporada();
	string getSerieALaQuePertenece();

	void playCapitulo(int);
	void playCapitulo(string);

	void describeCapitulo(int);
	void describeCapitulo(string);

	void aniadirCapitulo(Capitulo);
	void eliminarCapitulo(int);

	void update();

	void describe();
};


int Temporada::getCapitulosTotales() {
	return this->capitulosTotales;
}
int Temporada::getNumeroDeTemporada() {
	return this->numeroDeTemporada;
}
int Temporada::getDuracionTemporada() {
	return this->duracionTemporada;
}
int Temporada::getRatingTemporada() {
	return this->ratingTemporada;
}


void Temporada::setCapitulosTotales() {
	this->capitulosTotales = this->CapitulosDeLaTemporada.size();
}
void Temporada::setNumeroDeTemporada(int n) {
	this->numeroDeTemporada = n;
}
void Temporada::setDuracionTemporada() {
	float runningSum = 0;
	int size = this->CapitulosDeLaTemporada.size();
	for (int i = 0; i < size; i++) {
		runningSum += this->CapitulosDeLaTemporada[i].getDuracion();
	}

	this->duracionTemporada = runningSum;
}
void Temporada::setRatingTemporada() {
	float runningSum = 0;
	int size = this->CapitulosDeLaTemporada.size();
	for (int i = 0; i < size; i++) {
		runningSum += this->CapitulosDeLaTemporada[i].getRating();
	}

	this->ratingTemporada = runningSum/size;
}

int Temporada::exists(string name) {
	for (int i = 0; i < this->CapitulosDeLaTemporada.size(); i++) {
		if (this->CapitulosDeLaTemporada[i].getName() == name) {
			return i;
		}
	}
	return -1;
}

string Temporada::getSerieALaQuePertenece() {
	return this->serieALaQuePertenece;
}

void Temporada::setSerieALaQuePertenece(string n) {
	this->serieALaQuePertenece = n;
	
	
}

void Temporada::update() {
	this->setCapitulosTotales();
	this->setDuracionTemporada();
	this->setRatingTemporada();
}

void Temporada::playCapitulo(int i) {
	this->CapitulosDeLaTemporada[i].play();
}

void Temporada::playCapitulo(string str) {

	int i = exists(str);
	if (i >= 0) {
		this->CapitulosDeLaTemporada[i].play();
	}
	else {
		std::cout << "Capitulo no encontrado" << std::endl;
	}

}

void Temporada::describeCapitulo(int i) {
	this->CapitulosDeLaTemporada[i].describe();
}

void Temporada::describeCapitulo(string str) {
	int i = exists(str);
	if (i >= 0) {
		this->CapitulosDeLaTemporada[i].describe();
	}
	else {
		std::cout << "Capitulo no encontrado" << std::endl;
	}
	
}

void Temporada::aniadirCapitulo(Capitulo nuevo) {
	this->CapitulosDeLaTemporada.push_back(nuevo);
	this->update();
}

void Temporada::eliminarCapitulo(int n) {
	this->CapitulosDeLaTemporada.erase(this->CapitulosDeLaTemporada.begin()+n-1);
	this->update();
}

void Temporada::describe() {
	std::cout <<
		"Capitulos:\t" << this->capitulosTotales << '\n' <<
		"Temporada:\t" << this->numeroDeTemporada << '\n' <<
		"Serie:\t\t" << this->serieALaQuePertenece << '\n' <<
		"Rating:\t\t" << this->ratingTemporada << '\n' <<
		"Duracion:\t" << this->duracionTemporada << '\n';
}