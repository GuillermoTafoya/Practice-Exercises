#pragma once
#include "Temporada.h"

class Serie{

	int duracionDeLaSerie, temporadasTotales;

	float ratingDeLaSerie;

	std::vector <Temporada> TemporadasDeLaSerie;

	string generoDeLaSerie;

	friend class boost::serialization::access;
	template<class Archive>
	void serialize(Archive& ar, const unsigned int version)
	{

		ar& TemporadasDeLaSerie;
		ar& ratingDeLaSerie;
		ar& duracionDeLaSerie;
		ar& temporadasTotales;
		ar& generoDeLaSerie;

	}
public:
	Serie() {};

	Temporada getTemporada(int);

};



Temporada Serie::getTemporada(int n) {
	return this->TemporadasDeLaSerie[n];
}
