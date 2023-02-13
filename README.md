# Breakfast Survey and Analysis

## Table of Contents
1. [User Experience](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colour Scheme](#colour-scheme)
    - [Data Model](#data-model)
    - [Flowchart](#flowchart)
2. [Features](#features)
    - [Take Survey or View Analysis](#take-survey-or-view-analysis)
    - [View Analysis by Gender or Age Group](#view-analysis-by-gender-or-age-group)
    - [Question Selection](#question-selection)
    - [Return to the Beginning](#return-to-beginning)
    - [Take Survey](#take-survey)
    - [Input Answers](#input-answers)
3. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
4. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Feature Testing](#feature-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
6. [Credit](#credit)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals
- Analyse survey results.
- Collect survey responses.
- Display results in a format that is easy for the user to read.
- Use input validation for user input.
- Store survey data in Google Sheets.

### User Stories
- As a user, I want to understand what the program is for and how to use it.
- As a user, I want to be able to choose whether to take the survey or view results.
- As a user, I want to be able to choose what questions I view the data for.
- As a user, I want to be able to take the survey.
- As a user, I want to be able to review my answers before submitting or take the survey again.
- As a user, I want to be able to exit or restart the program. 

### Colour Scheme
Colorama has been used to apply colour to the terminal to make it more readable. 
- Instructions are displayed in yellow.
- Inputs are displayed in green.
- Error messages are displayed in red.
- Tables are displayed in cyan.

### Data Model
The program uses Google Sheets to store data in columns. The worksheet has a column that applies a unique user ID for each user and a column for each survey question. 

The program uses a series of functions to display the survey results; results_selections asks the user if they want to view results by Gender or Age Group, then question_selection asks the user to choose which question they want view results for. This information is then passed into display_percentages which uses Pandas to analyse the data and calculate percentages which are presented in table format to the user. 

When taking the survey, the users answers are stored in a variable called user_answers which updates each time a question is answered. After the last question is answered the user is asked to review and submit their results or take the quiz again. If the user clicks the submit the data is pushed to the Google Sheets worksheet. 

If a user answers no to 'Do you eat breakfast?', the survey ends after they explain why. Furthermore, their data is not used when analysing the remaining questions, meaning that questions 5-9 are only analysed based on people who eat breafast. 

### Flowchart
[Lucid](https://lucid.app/documents#/dashboard) was used in the planning stage of the project to plan the logic and data flow. 

## Features

### Take Survey or View Analysis
### View Analysis by Gender or Age Group
### Question Selection
### Return to Beginning
### Take Survey 
### Input Answers


## Technologies Used
### Languages
- Python

### Frameworks, Libraries and Programmes
- [Lucid](https://lucid.app/documents#/dashboard): this was used to create a flowchart in the planning stage of the project.
- [Colorama](https://pypi.org/project/colorama/): this was used to add colour to the terminal to improve UX and readibility.
- [Tabulate](https://pypi.org/project/tabulate/): this was used to display data in tables. 
- [Pandas](https://pypi.org/project/pandas/): this was used to analyse survey data.
- [Numpy](https://pypi.org/project/numpy/): this was used to analyse survey data.
- [Gspread](https://docs.gspread.org/en/v5.7.0/): this is the API for the google which stores the survey data. 
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and to push the code to GitHub. 
- [GitHub](https://github.com/): this was used to store the project and for version control.
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.

## Testing
### Testing User Stories
### Code Validation
### Feature Testing
### Bugs

## Deployment

## Credit
### Content
### Media
### Code

## Acknowledgements