package com.salesianostriana.dam._Ejemplo.controlador;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.LocalDateTime;

@Controller
public class MainController {

    @GetMapping("/")
    public String welcome(Model model){
        model.addAttribute("mensaje","Los alumnos de 2º DAM de hoy están saludando");
        return "index";
    }

    @GetMapping("/now")
    public String now(Model model){
        model.addAttribute("ahora", LocalDateTime.now());
        return "lahora";
    }

}
