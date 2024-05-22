package org.task21.service;

import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.task21.EmailSender;
import org.task21.entity.Team;
import org.task21.repository.TeamRepository;

import java.util.List;

@Service
@AllArgsConstructor
@Slf4j
public class TeamService
{
    private TeamRepository teamRepository;
    private EmailSender customEmailSender;

    public void AddTeam(Team team)
    {
        log.info("Команда сохранена");
        customEmailSender.sendEmail(team);
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