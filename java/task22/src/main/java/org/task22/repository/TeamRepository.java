package org.task22.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.task22.entity.Team;

import java.util.List;

@Repository
public interface TeamRepository extends JpaRepository<Team, Long>
{
    List<Team> findAllByNameContains(String name);
    List<Team> findAllByCreationDateContains(String date);
}