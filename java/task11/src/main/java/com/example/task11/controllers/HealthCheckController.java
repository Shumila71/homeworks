package com.example.task11.controllers;

import org.springframework.web.bind.annotation.GetMapping;

public class HealthCheckController {
    @GetMapping("/health")
    public String checkHealth() {
        return "Application is up and running!";
    }
}
