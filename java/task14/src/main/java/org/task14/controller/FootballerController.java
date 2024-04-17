package org.task14.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.task14.entity.Footballer;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("footballer")
public class FootballerController {
    private List<Footballer> footballers = new ArrayList<>();

    @PostMapping("/add")
    public ResponseEntity AddFb(@RequestBody Footballer footballer)
    {
        footballers.add(footballer);
        return ResponseEntity.ok(HttpStatus.OK);
    }
    // Delete
    @DeleteMapping("/delete/{id}")
    public ResponseEntity DeleteFb(@PathVariable int id)
    {
        footballers.remove(id);
        return ResponseEntity.ok(HttpStatus.OK);
    }
    // GetAll
    @GetMapping()
    public List<Footballer> GetAllFb()
    {
        return footballers;
    }
}
