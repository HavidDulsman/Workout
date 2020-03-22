# Workout: Create and track your daily workouts!


This project was created in reference to the QA Learning Academy Training Based Project Specification: Fundamental Project Specification - DevOps Core. This Project meets all of the specifications of said documents and fully displays the ability of the creator.

This Project is due Week 5 of the QA Consultancy DevOps 17th February 2020 Intake.

## Table of Contents

1. [Brief](https://github.com/HavidDulsman/Workout/tree/developer#brief)
    + [Requirements](https://github.com/HavidDulsman/Workout/blob/developer/README.md#requirements)
2. [Project Plan](https://github.com/HavidDulsman/Workout/tree/developer#brief)
    + [Trello Board](https://github.com/HavidDulsman/Workout/tree/developer#trello-board)
3. [Architechure](https://github.com/HavidDulsman/Workout/tree/developer#brief)
    + [Entity Relationship Diagram](https://github.com/HavidDulsman/Workout/tree/developer#entity-relationship-diagram)
    + [Use Case Diagram](https://github.com/HavidDulsman/Workout/tree/developer#use-case-diagram)
    + [Multi Tier Architecture Diagram](https://github.com/HavidDulsman/Workout/tree/developer#use-case-diagram)
4. [Risk Assessment](https://github.com/HavidDulsman/Workout/blob/developer/README.md#risk-assessment)
5. [Deployment](https://github.com/HavidDulsman/Workout/tree/developer#deployment)
    + [List of Technologies Used](https://github.com/HavidDulsman/Workout/tree/developer#list-of-used-technologies-and-languages)
6. [Testing](https://github.com/HavidDulsman/Workout#testing)
    + [Pytest Report](https://github.com/HavidDulsman/Workout#pytest-functionality)
    + [Coverage Report](https://github.com/HavidDulsman/Workout#coverage-report)
7. [Front-end Design](https://github.com/HavidDulsman/Workout#front-end-design)
8. [Project Retrospective](https://github.com/HavidDulsman/Workout/tree/developer#project-retrospective)
    + [Notable Achievements](https://github.com/HavidDulsman/Workout/tree/developer#notable-achievements)
    + [Project Shortcomings] (https://github.com/HavidDulsman/Workout#project-shortcomings)
    + [Future Improvements](https://github.com/HavidDulsman/Workout/tree/developer#future-improvements)
 


## Brief
As quoted from 'QAC - Fundamental Project Specification (DevOps Core)-revised':
    
    " Your overall objective with thisproject is the following:
    
    - To create a CRUD application with utilisation of supporting tools, methodologies and technologies 
      that encapsulate all core modules covered during training. "
### Requirements
Some of the requirements for a 'Minimal Viable Product' included:
* The use of two relational tables
* Complete utilization of CRUD Functionality in application
* Fully Designede test suits
* Intergration into a Version-Control System
    

## Project Plan
### Kanban Board
#### Sprint 1: 
The contents of the task backlog are designed based of the **User Stories**, which are themselves based of the requirements of the users. The tasks will make their way back and forth until they are completed. Bugs are also recorded and put in the 'Done' column once ammended.

Some of the users stories have been tagged **Orange** to identify that they are additional user requirements that are not necessary to the minimum required product, and requests that may or may not be dealt with after all of the core tasks have been completed

![Sprint 1](https://i.imgur.com/hmL0B6f.png)

#### Sprint 2:
The 2nd Sprint focuses heaviily on front end preparation as well as testing various parts of the backend, especially SQL and database related tasks. Moving forward, I opted to vigourly test an entire function during this stage, whilst also planning and developing another closelty associated with it.
![Sprint 2](https://i.imgur.com/3LyXYcU.png)

#### Sprint 3:
By the 3rd sprint, many of the front end features where either completed and tested, or nearing final stages of development. Some of the action features where also being started on, including the first **read** and **create** functions for CRUD.
![Sprint 3](https://i.imgur.com/EtvHDba.png)

#### Sprint 4: 
Sprint for took abit longer than previous stages, due to abit of confusion regarding routine functionality and styling. To counter this, the project was scaled back slightly to be more in line with my current ability set. Many of the action and routine functions are now being tested, with a couple bugs on the right side to sort out.
![Sprint 4](https://i.imgur.com/vDIDkrP.png)

#### Sprint 5:
At this stage of development, all of the CRUD feautures had now being developed, withn **delete** and **update** functions being tested. i would now focus on many of the CI/Jenkins requirements, as well as ironing out any bugs. It also became increasing unlikely at this stage the login feature would be completed, but i would try and get the category filters to work in time
![Sprint 5](https://i.imgur.com/l6GnjQg.png)

#### Completition
The Minimal required product was now achieved within a suitable time frame! Unfortunately the login and category filters where not completed in time and the remaining time was used to completed other tasks such as this readme.md file/
![Completiton](https://i.imgur.com/gyEe47o.jpg)

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
A risk assessment was compiled to look and examine risk related to the project, its requirements and demands. Due to the complexity and detail of my risk assessment, i have opted to include it as it own file which can be accessed through the repository or by using [this link.](https://github.com/HavidDulsman/Workout/blob/master/documentation/workout_Risk-2.xlsx)

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

## Testing
### Pytest Functionality
Testing the functionality of my finished product was very important during the end of development. Using the **Pytest** tool, I developed functions that would firstly test the 9 URLs of the page and if they would display a **HTTP 200** message, that means the page is ok with no errors.  Secondly, I though it was important to test the 4 main CRUD functions of my application, so i have also include 1 of each of the functions in my testing.

![Pytest Report](https://i.imgur.com/xeyy7tr.png)

### Coverage Report
This coverage report was made using a combination of the **Pytest** and **Coverage** tools for Python, and where displayed at the end of a Jenkins Pipeline build report. This was made possible thanks to various shell script files and clever cloning of the project files onto a new Jenkins Virtual Machine. Find a preview and overall coverage score below:

![Coverage Report TOP](https://i.imgur.com/SkvSTyX.png)
![Coverage Report BOTTOM](https://i.imgur.com/icQ7UC9.png)

## Front-end Design
### Homepage
![Homepage](https://i.imgur.com/vBuoaQw.png)

### My Routines
![My Routines](https://i.imgur.com/lhhJKsv.png)

### New Routine
![New Routine](https://i.imgur.com/7MEpcXx.png)

### Routine Details 
![Routine Details](https://i.imgur.com/poDoDiE.png)

### Actions
![Actions](https://i.imgur.com/Y3eVol5.png)

## Project Retrospective
This section of the report was completed either after the project was completed to its fullest or at the point of minimal delivery. The retrospective will reveal areas of success during the projects life, whilst also suggesting future improvements based on some of the shortcomings of the project.
### Notable Achievements
#### Good use of DevOps practices and Agile Methodologies
Many common DevOps practices where used in conjunction with this project. The vast majority of the work outside of this readme.md file was completed on a seperate **developer branch** and work was only pushed up to the master branch once in a stable state. More branches wouldve been made and pushed to the developer branch if more people where part of my team.

![Pushing from developer to master](https://i.imgur.com/i8Sm3yl.png)

![No conflicts with merge](https://i.imgur.com/NUO9k94.png)

#### Git Webhook to Jenkins
The Inclusion of a Webhook between my github and jenkins means that my Jenkins VM will always create and test every new build of my website, giving me new information on any new tests or coverage I have set up

![Webhook on Github linked to my Jenkins repository](https://i.imgur.com/qMv0YIj.png)

#### Website Aesthetics
The styles and aesthetics of my application go very well with the themes of a workout. Using both a minimalist design that also blends very well with the background make using the app a enjoyable experience. Most of the features made also use the same page, so there is little travel on the site and always tries to reveal all of the options for its users.

### Project Shortcomings
#### Lack of action search functionality
Whilst the category table was included in the final version, little was really done with the categories outside of back-end SQL testing. It would have been really good to include a feature that would have filtered out actions depending on their category, but mostly time constraints stopped this from being achieved.

#### Absense of User login
As explained during the design phase of the project, a log in feature would have been ideal as it would have allowed the system to only show the workouts made by that user. Unfortunately due to time constraints and overestimasting my ability, i opted to leave that function out of the end product. 

Its absense had little affect on the project, as i carefully followed my MoSCoW methodology and build functions to be independant of logins. Also the login feature would have had little affect on my overall mark, so it was the obvious that it would be the first feature to leave out.
### Future Improvements
#### Increased testing coverage
As shown previous in the [Coverage Report](https://github.com/HavidDulsman/Workout#coverage-report) section of the readme file, there was little coverage of the application, even though alot of its core features where tested. This is definately an area i would like to improve in later projects

#### Dynamic templates
Whilst something similar was implemented into the final product, i would have loved to incorporate dynamic pages and templates, especially on a routines individual page. This could have been achieved if i had used WhatTheForms during development, or used a different coding langauge.

#### Branch Management
Various time during the development did i have issues regarding the branches of development and which ones i was pushing and pulling from. Although i eventually got the hang of it, i would have prevented alot of early problems. I expect the next project to be much more smoother as i start to master basic git commands.

## Authors
David Hulsman

## Acknowledgements
My Family for supporting me during this training period, as well as Syed for his laidback, but also enjoyable and informative training sessions 
