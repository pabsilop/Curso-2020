package com.PabloSilvaLopez.dam.ProyectoSpring.seguridad.modelo;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Arrays;
import java.util.Collection;

@Data
@NoArgsConstructor
@Entity
public class Usuario implements UserDetails {


    /**
     *
     */
    private static final long serialVersionUID = 1409538586158223652L;

    @Id
    @GeneratedValue
    private Long id;

    private String nombre;
    private String apellidos;


    // Este será nuestro "username"
    @Column(unique = true)
    private String email;

    private String password;

    private boolean admin;

    public Usuario(String nombre, String apellidos, String email, String password, boolean admin) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.email = email;
        this.password = password;
        this.admin = admin;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        String role = "ROLE_";
        if (admin) {
            role += "ADMIN";
        } else {
            role += "USER";
        }
        return Arrays.asList(new SimpleGrantedAuthority(role));
    }

    @Override
    public String getUsername() {
        return email;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }



}
