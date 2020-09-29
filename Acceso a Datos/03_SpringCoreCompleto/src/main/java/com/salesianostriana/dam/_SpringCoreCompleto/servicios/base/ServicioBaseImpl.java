package com.salesianostriana.dam._SpringCoreCompleto.servicios.base;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public abstract class ServicioBaseImpl<T, ID, R extends JpaRepository<T, ID>>
        implements ServicioBase<T, ID>{

    @Autowired
    R repositorio;

    @Override
    public T save(Object o) {
        return null;
    }

    @Override
    public Optional<T> findById(Object o) {
        return Optional.empty();
    }

    @Override
    public List<T> findAll() {
        return null;
    }

    @Override
    public T edit(Object o) {
        return null;
    }

    @Override
    public void delete(Object o) {

    }

    @Override
    public void deleteById(Object o) {

    }
}
