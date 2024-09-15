# Exercise 2 - Streamlit dashboard

In this exercise sheet, you will work with streamlit for creating frontend dashboard.

> [!NOTE]
> These exercises covers lecture 03-06.

## 0. Supahcoolsoft employee executive dashboard

Create a dashboard in streamlit displaying this employee data to the executives. Call it `Executive dashboard` for coolness sake. It should contain: 

- basic statistics on employees (total count, average age, average salary)
- show a table with employee details
- bar chart showing number of employees accross departments
- histogram of salary distribution
- box plot of salaries by department
- histogram of age distribution
- box plot of ages by department

Style the dashboard to make it more exclusive for executives.


## 1. Ice cream prediction app

Download this [ice cream data set](https://www.kaggle.com/datasets/vinicius150987/ice-cream-revenue) and create a simple app in streamlit that lets the user enter a temperature in celsius and it outputs the revenue prediction. You can for example use random forest regression to predict the revenue.  

## 2. PISA scores

PISA performance usually get a lot of media attention on how good it's going for the school in your country. It has gotten a lot of media attention at least in Sweden where I live. Use this [dataset of pisa performance](https://www.kaggle.com/datasets/thedevastator/pisa-performance-scores-by-country) and create a dashboard. It should contain a minimum of this: 

- basic statistics of the data (number of records, number of locations, subjects, and time periods)
- show a table with sample data
- bar chart showing average PISA scores by location
- plot trends that can be filtered for each country 
  
Bonus:
- more interactive filtering to drill down to specific locations, time period, subjects, ... 
- this filtering should be displayed on a side panel

## 3. Chatbot

Create a simple chatbot and customize it to your choice.

Here are some inspirations: 

- ChatGBG - always talk in göteborg dialect and likes making fun of people from Stocholm
- AnalystGPT - send in some data and it will give some KPIs, or even make graphs based on your data
- JokeTeller - turns everything into a good joke 
- Answer questions about your school or your programs 

Make sure that your chatbot has memory.

## 4 Chatbot assistants 

Now create a few chatbot assistants with various expertise, for example 

- a summarizer in simpler language
- an expert in resume building 
- an expert in resume summarizing
- a culinary expert that based on what ingredients you put in can give suggestions on recipes
- one data analyst which can take data and generate a plot

Create a filtering option so that you can choose which expert you want to talk to.