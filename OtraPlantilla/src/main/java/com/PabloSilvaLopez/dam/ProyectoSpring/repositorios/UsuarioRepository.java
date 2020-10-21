package com.PabloSilvaLopez.dam.ProyectoSpring.repositorios;

import java.util.Optional;

import com.PabloSilvaLopez.dam.ProyectoSpring.seguridad.modelo.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;


public interface UsuarioRepository extends JpaRepository<Usuario, Long>{

    Optional<Usuario> findFirstByEmail(String email);


}
