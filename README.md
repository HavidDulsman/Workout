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
5. [Deployment](https://github.com/HavidDulsman/Workout/tree/developer#deployment)
    + [List of Technologies Used](https://github.com/HavidDulsman/Workout/tree/developer#list-of-used-technologies-and-languages)
6. [Project Retrospective](https://github.com/HavidDulsman/Workout/tree/developer#project-retrospective)
    + [Notable Achievements](https://github.com/HavidDulsman/Workout/tree/developer#notable-achievements)
    + [Future Improvements](https://github.com/HavidDulsman/Workout/tree/developer#future-improvements)
 


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

## Risk Assessment
A risk assessment was compiled to look and examine risk related to the project, its requirements and demands. Due to the complexity and detail of my risk assessment, i have opted to include it as it own file which can be accessed through the repository or by using [this link.](https://github.com/HavidDulsman/Workout/blob/developer/workout_Risk.xlsx)

## Deployment

![Deployment pipeline diagram of use softwares](https://i.imgur.com/rz4D02h.png)

### List of used technologies and languages
* **GitHub:** Version Control System
* **Jenkins:** Continuous Intergration Server
* **Google Cloud Services:** Live Environment + SQL Database Host
* **Visual Studio Code:** IDE for frontend and backend development. Used the following languages:
    - **Python 3:** Logic and Functionality
    - **HTML:** Front-end GUI design
    - **CSS:** Styling and design of front-end GUI
    - **Flask:** Connects front-end and back-end
    - **Jinja2:** Pass variables between Python and HTML
    - **MySQL:** Allows for access of SQL Databases, as well as query-based functions
* **Trello:** Kanban board and Project tracking

## Project Retrospective
### Notable Achievements
### Future Improvements

## Authors
David Hulsman

## Acknowledgements
The boys, past and present. You know who you are.
