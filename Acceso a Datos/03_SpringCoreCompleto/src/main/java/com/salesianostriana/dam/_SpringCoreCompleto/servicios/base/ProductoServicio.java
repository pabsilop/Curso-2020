package com.salesianostriana.dam._SpringCoreCompleto.servicios.base;

import com.salesianostriana.dam._SpringCoreCompleto.modelos.Producto;
import com.salesianostriana.dam._SpringCoreCompleto.repositorios.ProductoRepositorio;
import org.springframework.stereotype.Service;

import java.util.stream.Collector;
import java.util.stream.Collectors;

@Service
public class ProductoServicio extends ServicioBaseImpl<Producto, Long, ProductoRepositorio> {


    public List<Producto> todosLosProductosConElNombreEnMayuscula(){
        return this.findAll().stream()
                                .map(p -> {
                                    return Producto.builder()
                                            .id(p.getId())
                                            .nombre(p.getNombre().toUpperCase())
                                            .precio(p.getPrecio())
                                            .build();
                                }).collect(Collectors.toList());
    }
}
