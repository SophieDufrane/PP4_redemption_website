# TITLE.

## Table of Contents

- [Introduction](#introduction)
- [User Story](#user-story)
- [Data Source](#data-source)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Feature 1](#feature-1)
    - [Feature 2](#features-2)
  - [Features left to implement](#features-left-to-implement)
- [Manual Testing](#manual-testing)
- [Refactoring Process](#refactoring-process-improving-efficiency-and-readability)
- [Deployment Steps](#deployment-steps)
- [Forking and Cloning the Project]()
- [External Libraries, Tools and Technology](#external-libraries-tools-and-technology)
- [Resources](#resources)

## Introduction

The [Title](https://satisfaction-survey-sd-a479e4d4f1cf.herokuapp.com/) project was inspired by...

## User Story

This project is...

## Data Source:

![Google Worksheet ScreenShot](media/google_worksheet.png)

## Features:

### Existing Features:

#### Feature 1

![Feature 1](media/main_menu.png)

#### Features 2

![Feature 2](media/survey.png)

### Features left to implement:

## Manual Testing:

***Key Tests, Bugs and fixs:***

## Refactoring Process: Improving Efficiency and Readability

### Deployment Steps

The site was deployed successfully to [site](https://www.heroku.com/github-students/signup) following the steps below:

1. 
2. 
3. 
4. 
5. 

### Forking and Cloning the Project

Forking the repository creates a copy of this project, allowing modifications without affecting the original code. Once the repository is forked, it can be cloned to a local machine for development. Follow these steps to fork, clone, and work on the project:

- **Fork the repository**
  - Go to the repository you want to fork on [GitHub](https://github.com/).
  - In the top-right corner of the page, click `Fork`.
  - Name the new forked repository, then click `Create Fork`.
  - This creates a copy of the repository under your own GitHub account.

Once the repository is forked, we need to clone it to our local machine before working on it. This is done by following the steps below:

- **Clone the forked repository**
  - In the forked repository on GitHub, above the list of files, click `Code`.
  - Copy the URL for the repository (either HTTPS or SSH).
  - Open a terminal (or Git Bash).
  - Type `git clone`, then paste the copied URL.
  - Press `Enter`
  - Navigate to the newly cloned repository directory: `cd` and the repository name.

### External Libraries, Tools and Technology

- `gspread`: A Python library used to interact with *Google Sheets*. This library was essential for retrieving and storing survey responses in real-time, allowing the application to dynamically update and analyse survey data directly from the Google Sheets document.
- `google.oauth2`: Another librairy used for authenticating access to *Google Sheets* via service account credentials. This library was crucial for secure and authorised access to the Google Sheets API. Credentials were managed securely through the creds.json file. 
- `Google Sheets`: Used to store and manage survey responses.
- `Python`: The main programming language used for building the survey and analysis tool.
- `Google Cloud Console`: Used to generate credentials and API accesses for Google Sheets integration.
- `Gitpod`: A cloud-based IDE used for developing the project.

### Resources
