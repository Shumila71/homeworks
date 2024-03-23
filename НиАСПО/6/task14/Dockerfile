# build project
FROM gradle:8.6.0-jdk17 as build

COPY --chown=gradle:gradle . /project
WORKDIR /project
RUN gradle build --no-daemon


# build image
FROM openjdk:17

WORKDIR /app

#COPY ./build/libs/task14-0.0.1-SNAPSHOT.jar /app/task14.jar
COPY --from=build /project/build/libs/task14-0.0.1-SNAPSHOT.jar /app/task14.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","task14.jar"]