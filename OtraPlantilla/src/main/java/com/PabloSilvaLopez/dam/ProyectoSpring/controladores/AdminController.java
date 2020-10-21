package com.PabloSilvaLopez.dam.ProyectoSpring.controladores;

import com.PabloSilvaLopez.dam.ProyectoSpring.seguridad.modelo.Usuario;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/administrador/")
public class AdminController {

    @GetMapping("/")
    public String index() {
        return "administrador/index-tienda";
    }

    @GetMapping("/info")
    public String info(@AuthenticationPrincipal Usuario usuario, Model model) {
        model.addAttribute("nombre", usuario.getNombre() + " " + usuario.getApellidos());
        return "administrador/info";
    }

}