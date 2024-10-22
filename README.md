README
Assignment Overview
: https://online-survey-ouvm.onrender.com

README

Overview

This project is divided into five main sections:

1. Web Development with Flask:
A simple webpage was created using Flask to collect user data through an online questionnaire named ‘Survey 2024’. The collected data includes Age, Gender, Total Income, and various Expenses. The expense categories are utilities, entertainment, school fees, shopping, and healthcare. Checkboxes were used for each expense category, with corresponding textboxes for users to input amounts spent. The questionnaire collected data from a sample size of 100 users.

2. Data Storage with MongoDB:
Initially, the data was stored locally using MongoDB. However, for cloud deployment, a free-tier MongoDB Atlas account was created to host the data.

3. Data Processing with Python:
A Python class named ‘User’ was created for data processing (see `data_processing.ipynb`). The class included a loop that collected and stored data in a CSV file. This CSV file was later loaded into a Jupyter notebook for data visualization.

 4. Data Visualization:
Data visualizations were performed in the Jupyter notebook (see `data_visualization.ipynb`). Two figures were generated:
Figure 1: Displays the ages with the highest total income.
Figure 2: Shows gender distribution across various spending categories.
Both figures were exported for use in a PowerPoint presentation for client review.

5. Deployment on Render Platform Using AWS Services:
The web application files were pushed to a GitHub repository using Git Bash. The cloud database was hosted on MongoDB Atlas, followed by deployment on the Render platform. 

Key points for deployment:
- Keep the `requirements.txt` file minimal, including only necessary dependencies for Flask.
- Render automatically downloads dependencies for deployment.
- Ensure that Render's IP addresses are whitelisted in MongoDB Atlas.
- Avoid exposing sensitive credentials (e.g., passwords) by using environment variables in your Flask app while keeping them secure on Render.

![image](https://github.com/user-attachments/assets/a054c7bf-508a-44b2-a896-bb0ebfcdd330)


The deployed web application can be accessed at:  
[https://online-survey-ouvm.onrender.com](https://online-survey-ouvm.onrender.com)

Upon visiting the link, users will first see a consent form. After consenting, they can access the survey. To ensure complete data collection, the questionnaire does not accept submissions if any fields are left blank. After submitting the form, a thank you message confirms successful data submission. When running the project on your end, the MongoDB database named ‘showcase’ will contain a collection called ‘Survey 2024’ that stores the submitted data in dictionary format.
