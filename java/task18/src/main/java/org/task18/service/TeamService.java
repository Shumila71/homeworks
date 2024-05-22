package org.task18.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.task18.entity.Team;
import org.task18.repository.TeamRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class TeamService
{
    private TeamRepository teamRepository;

    public void AddTeam(Team team)
    {
        teamRepository.save(team);
    }

    public void DeleteTeam(Long id)
    {
        teamRepository.deleteById(id);
    }

    public List<Team> GetTeams()
    {
        return teamRepository.findAll();
    }

    public Team GetTeamById(Long id)
    {
        return teamRepository.findById(id).get();
    }

    // Filter
    public List<Team> FilterTeamsByName(String pattern)
    {
        return teamRepository.findAllByNameContains(pattern);
    }
    public List<Team> FilterTeamsByDate(String pattern)
    {
        return teamRepository.findAllByCreationDateContains(pattern);
    }
}