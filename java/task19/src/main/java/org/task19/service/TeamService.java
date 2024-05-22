package org.task19.service;

import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.task19.entity.Team;
import org.task19.repository.TeamRepository;

import java.util.List;

@Service
@AllArgsConstructor
@Slf4j
public class TeamService
{
    private TeamRepository teamRepository;

    public void AddTeam(Team team)
    {
        log.info("Команда сохранена");
        teamRepository.save(team);
    }

    public void DeleteTeam(Long id)
    {
        teamRepository.deleteById(id);
    }

    public List<Team> GetTeams()
    {
        log.info("Все команды получены");
        return teamRepository.findAll();
    }

    public Team GetTeamById(Long id)
    {
        return teamRepository.findById(id).get();
    }

    // Filter
    public List<Team> FilterTeamsByName(String pattern){
        return teamRepository.findAllByNameContains(pattern);
    }
    public List<Team> FilterTeamsByDate(String pattern){
        return teamRepository.findAllByCreationDateContains(pattern);
    }
}