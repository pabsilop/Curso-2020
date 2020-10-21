package com.PabloSilvaLopez.dam.ProyectoSpring.servicios;


import com.PabloSilvaLopez.dam.ProyectoSpring.repositorios.UsuarioRepository;
import com.PabloSilvaLopez.dam.ProyectoSpring.seguridad.modelo.Usuario;
import com.PabloSilvaLopez.dam.ProyectoSpring.servicios.base.BaseService;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UsuarioServicio extends BaseService<Usuario, Long, UsuarioRepository> {

    public UsuarioServicio(UsuarioRepository repo) {
        super(repo);
    }

    public Optional<Usuario> buscarPorEmail(String email) {
        return repositorio.findFirstByEmail(email);
    }

}
