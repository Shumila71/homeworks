package org.task16.service;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.task16.entity.Team;
import org.task16.entity.Footballer;
import org.task16.repository.TeamRepository;
import org.task16.repository.FootballerRepository;

import java.util.List;

@Service
@AllArgsConstructor
public class FootballerService
{
    private FootballerRepository teamRepository;

    public void AddFootballer(Footballer level, Long teamId)
    {
        teamRepository.AddFootballer(level, teamId);
    }

    public void DeleteFootballer(Long id)
    {
        teamRepository.DeleteFootballer(id);
    }

    public List<Footballer> GetAllFootballer()
    {
        return teamRepository.GetAllFootballer();
    }

    public Footballer GetFootballerById(Long id)
    {
        return teamRepository.GetFootballerById(id);
    }
}