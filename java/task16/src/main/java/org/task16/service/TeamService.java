package org.task16.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.task16.entity.Team;
import org.task16.repository.TeamRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class TeamService
{
    private TeamRepository teamRepository;

    public void AddTeam(Team team)
    {
        teamRepository.AddTeam(team);
    }

    public void DeleteTeam(Long id)
    {
        teamRepository.DeleteTeam(id);
    }

    public List<Team> GetTeams()
    {
        return teamRepository.GetAllTeam();
    }

    public Team GetTeamById(Long id)
    {
        return teamRepository.GetTeamById(id);
    }
}