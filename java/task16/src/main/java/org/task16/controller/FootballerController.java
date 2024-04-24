package org.task16.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.task16.entity.Footballer;
import org.task16.entity.Team;
import org.task16.entity.Footballer;
import org.task16.service.FootballerService;

import java.util.List;

@RestController
@RequestMapping("api/footballers")
public class FootballerController
{
    @Autowired
    private FootballerService footballerService;

    @PostMapping("/{teamId}")
    public ResponseEntity AddFootballer(@RequestBody Footballer level, @PathVariable Long teamId)
    {
        footballerService.AddFootballer(level, teamId);
        return ResponseEntity.ok(HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity DeleteFootballer(@PathVariable Long id)
    {
        footballerService.DeleteFootballer(id);
        return ResponseEntity.ok(HttpStatus.OK);
    }

    @GetMapping()
    public List<Footballer> GetAllFootballer()
    {
        return footballerService.GetAllFootballer();
    }

    @GetMapping("/{id}")
    public Footballer GetFootballerById(@PathVariable Long id)
    {
        return footballerService.GetFootballerById(id);
    }
}
