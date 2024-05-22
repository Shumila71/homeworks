package org.task19.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.task19.entity.Team;
import org.task19.service.TeamService;

import java.sql.SQLException;
import java.util.List;

@RestController
@RequestMapping("api/teams")
public class TeamController
{
    @Autowired
    private TeamService teamService;

    @PostMapping()
    public ResponseEntity AddTeam(@RequestBody org.task19.entity.Team team) throws SQLException
    {
        teamService.AddTeam(team);
        return ResponseEntity.ok(HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity DeleteTeam(@PathVariable Long id) throws SQLException
    {
        teamService.DeleteTeam(id);
        return ResponseEntity.ok(HttpStatus.OK);
    }

    @GetMapping()
    public List<org.task19.entity.Team> GetAllTeam() throws SQLException
    {
        return teamService.GetTeams();
    }

    @GetMapping("/{id}")
    public org.task19.entity.Team GetTeamById(@PathVariable Long id) throws SQLException
    {
        return teamService.GetTeamById(id);
    }
    // Filter by name
    @GetMapping("/name/{pattern}")
    public List<Team> FilterTeamsByName(@PathVariable String pattern){
        return teamService.FilterTeamsByName(pattern);
    }

    // Filter by creationDate
    @GetMapping("/date/{pattern}")
    public List<Team> FilterTeamsByDate(@PathVariable String pattern)
    {
        return teamService.FilterTeamsByDate(pattern);
    }
}
