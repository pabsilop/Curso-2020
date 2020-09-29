package com.salesianostriana.dam.springdata.modelo;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@Data @Builder
@NoArgsConstructor @AllArgsConstructor
public class Producto {

    @Id
    @GeneratedValue
    private long id;

    private String nombre;
    private double precio;
    private int unidadesEnStock;


}
