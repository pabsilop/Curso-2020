package com.PabloSilvaLopez.dam.ProyectoSpring.controladores;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class InicioController {

    @GetMapping("/")
    public String index() {
        return "index-tienda";
    }

}
