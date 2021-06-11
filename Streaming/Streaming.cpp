// Streaming.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

// std
#include <vector>
#include <fstream>
#include <string>

// include headers from boost
#include <boost/archive/binary_oarchive.hpp>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/serialization/vector.hpp>
#include "boost/filesystem.hpp"  

//Headers
#include "Video.h"
#include "Pelicula.h"
#include "Capitulo.h"
#include "Temporada.h"
#include "Serie.h"


#include <stdlib.h>
using string = std::string;



std::string pathString = "assets";
boost::filesystem::path p = boost::filesystem::current_path(); // Construct the path from a string.
//string boost::filesystem::absolute(p)

int main()
{

    string src = "E:\\Dev\\Streaming\\Streaming\\assets\\";
    Capitulo video1 = Capitulo("Paradoja del abuelo", src + "Solution to the Grandfather Paradox.mp4", "Fisica" ,2.45, 4, 1,1,"Fisica en un minuto");
    Capitulo video2 = Capitulo("Privacidad", src + "When It's OK to Violate Privacy.mp4", "Fisica", 2.45, 4, 1, 1, "Fisica en un minuto");
    
    video1.calificar(4.7);
    video1.calificar(2.5);

    Temporada prueba = Temporada();
    prueba.setNumeroDeTemporada(1);

    prueba.setSerieALaQuePertenece("Fisica: la serie");

    prueba.aniadirCapitulo(video1);
    prueba.aniadirCapitulo(video2);
    
    std::cout << "write data" << '\n';
    {
        std::ofstream ofs("data.dat");
        boost::archive::binary_oarchive out_arch(ofs);
        out_arch << prueba;
    }

    std::cout << "read data" << '\n';
    {
        std::ifstream ifs("data.dat");
        if (!ifs) {
            std::cout << "read error!" << '\n';
            return 1;
        }
        Temporada prueba2;
        boost::archive::binary_iarchive in_arch(ifs);

        in_arch >> prueba2;

        std::cout << std::endl << "Descripcion de capitulo:" << std::endl;
        prueba2.playCapitulo("Privacidad");
        prueba2.describeCapitulo("Privacidad");

        std::cout << std::endl << "Descripcion de capitulo:" << std::endl;

        //prueba2.playCapitulo(0); // solo se muestra el ultimo video en ser reproducido
        prueba2.describeCapitulo(0);

        std::cout << std::endl << "Descripcion de la serie:" << std::endl;

        prueba2.describe();
    }

    


    return 0;
}