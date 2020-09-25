package com.salesianostriana.dam._EjemploSpringData;

import com.salesianostriana.dam._EjemploSpringData.model.Alumno;
import com.salesianostriana.dam._EjemploSpringData.model.AlumnoRepositorio;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);

	}

	@Bean
	public CommandLineRunner init(AlumnoRepositorio repo){
		return args -> {

			Alumno a = Alumno.builder()
					.nombre("Pablo")
					.apellidos("Silva López")
					.direccion("C/ Calatrava 26")
					.poblacion("Sevilla")
					.provincia("Sevilla")
				.build();

			repo.save(a);
		};

	}

}
