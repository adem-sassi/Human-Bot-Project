

# HUMAN BOT - Digital Transformation Project

Welcome to the "HUMAN BOT" project repository! This project is aimed at transforming the operational management of HUMAN BOT, a family-owned company specializing in humanoid robots, from a paper-based system to a fully digital and unified database system. Below you will find all the details necessary to understand and contribute to this project.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Scope and Objectives](#scope-and-objectives)
3. [Requirements and Specifications](#requirements-and-specifications)
4. [Technical Stack](#technical-stack)
5. [Database Design](#database-design)
6. [User Interfaces and API](#user-interfaces-and-api)
7. [Deliverables and Evaluation](#deliverables-and-evaluation)
8. [Contributing](#contributing)


## Project Overview

### Context

HUMAN BOT is a family-owned business that specializes in manufacturing humanoid robots. The company is undergoing a digital transformation to replace its paper-based management system with a modern, integrated digital solution. This project is particularly important following the recent acquisition of a second factory that operates differently from the original.

### Objective

The primary goal is to create a unified digital system that accommodates the distinct operational workflows of both factories while providing a coherent management framework. This will involve developing custom solutions using open-source tools.

## Scope and Objectives

### Duration and Team

- **Timeframe**: 7 hours
- **Team Composition**: Groups of 5 :
    - Adem Sassi (Project Manager)
    - Mohamed Aziz Kabissa
    - Mohamed Madhzaoui
    - Ramla Argui
    - Neo Hayat

### Data Management

Each factory has its own data management systems for employees, suppliers, and inventory:

- **Home Factory**:
  - Employee Data: Name, age, start and end dates.
  - Supplier Data: Name and delivery details.
  - Inventory: Daily production of robots.
  
- **Acquired Factory**:
  - Employee Data: Name, start date, and current status.
  - Supplier Data: Name, delivery details, and receiver.
  - Inventory: Daily usage of robot parts.

### Integration Strategy

A unified data dictionary and conceptual data model will be developed to harmonize data from both factories while preserving their unique operational characteristics.

## Requirements and Specifications

### Technical Specifications

- **Database**: PostgreSQL
- **Web Framework**: Flask
- **ORM**: SQLAlchemy

### User Interfaces and API

- **HR Interface**: A web page displaying all employees across both factories.
- **Supplier Interface**: A web page showing deliveries over the past 10 days.
- **Stock API**: An API endpoint providing inventory levels per factory for supplier use.
- **Stock Interface**: A web page displaying the remaining parts inventory for each factory.

### Security

No security features are required at this stage. User authentication and authorization will be implemented in future phases.

## Technical Stack

### Backend

- **PostgreSQL**: Chosen for its robustness and support for complex queries.
- **Flask**: A lightweight and flexible web framework ideal for developing the required interfaces and API.
- **SQLAlchemy**: An ORM that simplifies database interactions and schema management.

### Frontend

- **HTML/CSS**: Basic styling and layout for web interfaces.
- **JavaScript**: Enhancing interactivity and dynamic content loading.

## Database Design

### Data Dictionary and Views

- **Data Dictionary**: Defines each data element with its code, description, type, constraints, and calculation rules.
- **Views**:
  - `ALL_WORKERS`: List of all current employees with details sorted by start date.
  - `ALL_WORKERS_ELAPSED`: Calculates the number of days since each employee's start date.
  - `BEST_SUPPLIERS`: Lists suppliers delivering more than 1000 parts, sorted by delivery volume.
  - `ROBOTS_FACTORIES`: Indicates which factory assembled each robot.

### Functions and Procedures

- **Functions**:
  - `GET_NB_WORKERS`: Returns the number of workers in a given factory.
  - `GET_NB_BIG_ROBOTS`: Counts robots assembled with more than 3 parts.
  - `GET_BEST_SUPPLIER`: Returns the name of the top supplier based on deliveries.
- **Procedures**:
  - `SEED_DATA_WORKERS`: Creates sample worker data for testing.
  - `ADD_NEW_ROBOT`: Adds a new robot model based on the `ROBOTS_FACTORIES` view.

### Triggers

- **View Insertions**: Handles insertions into the `ALL_WORKERS_ELAPSED` view.
- **New Robot Audit**: Logs the creation date of a new robot.
- **Factory Data Consistency**: Ensures factory tables align with the expected format.

## Deliverables and Evaluation

### Final Submission

The final submission should include a Git repository with the following components:

- **Data Dictionary** (`hb_dico.md`)
- **Conceptual Data Model** (`hb_mcd.png`)
- **Logical Data Model** (`hb_mld.md`)
- **SQL Scripts**:
  - Schema creation (`hb_schema.sql`)
  - Views (`hb_views.sql`)
  - Functions and procedures (`hb_funcs_procs.sql`)
  - Triggers (`hb_triggers.sql`)
- **Flask Projects**:
  - HR Service
  - Stock Service
  - Supplier Service
  - API Service

## Contributing

### How to Contribute

To contribute to this project, follow these steps:

1. **Fork the Repository**: Create a personal copy of the repository.
2. **Clone the Repository**: Clone the forked repository to your local machine.
3. **Create a Branch**: Make a new branch for your feature or bugfix.
4. **Commit Changes**: Commit your changes with clear and descriptive messages.
5. **Push Changes**: Push your changes to your forked repository.
6. **Submit a Pull Request**: Create a pull request to merge your changes into the main repository.


