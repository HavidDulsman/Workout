# README

# Workout: Create and track your daily workouts!


This project was created in reference to the QA Learning Academy Training Based Project Specification: Fundamental Project Specification - DevOps Core. This Project meets all of the specifications of said documents and fully displays the ability of the creator.

This Project is due Week 5 of the QA Consultancy DevOps 17th February 2020 Intake.

## Table of Contents

1. [Brief](https://github.com/HavidDulsman/Workout/tree/developer#brief)
2. [Project Plan](https://github.com/HavidDulsman/Workout/tree/developer#brief)
    + [Trello Board](https://github.com/HavidDulsman/Workout/tree/developer#trello-board)
3. [Architechure](https://github.com/HavidDulsman/Workout/tree/developer#brief)
    + [Entity Relationship Diagram](https://github.com/HavidDulsman/Workout/tree/developer#entity-relationship-diagram)
    + [Use Case Diagram](https://github.com/HavidDulsman/Workout/tree/developer#use-case-diagram)
    + [Multi Tier Architecture Diagram](https://github.com/HavidDulsman/Workout/tree/developer#use-case-diagram)
4. [Risk Assessment](https://github.com/HavidDulsman/Workout/blob/developer/README.md#risk-assessment)

## Brief

## Project Plan
### Kanban Board
![Trello Board: In-Progress](https://i.imgur.com/8p3gPaO.png)

The contents of the task backlog are designed based of the **User Stories**, which are themselves based of the requirements of the users. The tasks will make their way back and forth until they are completed. Bugs are also recorded and put in the 'Done' column once ammended.

Some of the users stories have been tagged **Orange** to identify that they are additional user requirements that are not necessary to the minimum required product, and requests that may or may not be dealt with after all of the core tasks have been completed

## Architecture
### Entity Relationship Diagram
For my Entity Relationship Diagram, I opted to utilise the **MoSCow Prioritisation Method** in order to identify key areas of development. This will allow me to create a functional product **as early as possible**, and then increase the scale of my project once the minimum requirement is complete.

![Entity Relationship Diagram for QA SFIA Project: First Version](https://i.imgur.com/VCkA0So.png)

Firstly, I believe the minimal product would require workouts to be made and stored, containing actions suitable for a gym workout. One of the main requirements was to display a working **many-to-many relationship between two tables**. My 'workout' and 'action' tables share that relationship, and to work requires a **Bridging Table** in order to store each combination of data, as well as improve data structure.

Outside of these 3 tables, other desirable features such as **a user login system** and **categorised actions** require their own tables, however these will be implemented if their is minimal risk to the exisiting project after its completition.

### Use Case Diagram
This Use Case Diagram represents how a user interacts with the system. It is worth noting that the diagram only shows off the **Minimum-deliverable system**. 

![Use Case Diagram showcasing how users and functions work within the system](https://i.imgur.com/zM1Anws.png)

The diagram shows of the 2 users, **user** and **admin/developer** as well as their relations to system functions. The user has the majority of the interactions with the system, including creating, editing and deleting their workouts, as well as viewing what each action consists of. These interactions also extends into the system updating its records of workout. As for the developer, the developers only real interaction is via adding new actions for the user to use, but this will be via SQL queries.
### Multi Tier Architecture Diagram

## Risk Assessment

