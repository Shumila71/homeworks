package org.task23.repository;

import org.task23.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Integer>
{
    Optional<User> findUserByName(String username);
    User getUserByName(String username);
    boolean existsByName(String username);
}
