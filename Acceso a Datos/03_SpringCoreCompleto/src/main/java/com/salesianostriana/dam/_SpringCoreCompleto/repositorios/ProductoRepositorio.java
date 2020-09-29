package com.salesianostriana.dam._SpringCoreCompleto.repositorios;

import com.salesianostriana.dam._SpringCoreCompleto.modelos.Producto;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductoRepositorio extends JpaRepository<Producto, Long> {
}
