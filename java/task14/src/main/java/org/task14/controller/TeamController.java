package org.task14.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.task14.entity.Team;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("team")
public class TeamController {
    private List<Team> teams = new ArrayList<>();

    @PostMapping("/add")
    public ResponseEntity AddTeam(@RequestBody Team team)
    {
        teams.add(team);
        return ResponseEntity.ok(HttpStatus.OK);
    }
    // Delete
    @DeleteMapping("/delete/{id}")
    public ResponseEntity DeleteTeam(@PathVariable int id)
    {
        teams.remove(id);
        return ResponseEntity.ok(HttpStatus.OK);
    }
    // GetAll
    @GetMapping()
    public List<Team> GetAllTeam()
    {
        return teams;
    }
}
