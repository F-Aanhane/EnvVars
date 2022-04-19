# EnvVars
An exercise to learn trainees how environment variables work. Used in Veneficus internal trainings

# Assignments
  1. Clone project and open in your IDE (Pycharm)
  2. Add an .env file in the main folder and add the THIS_USER and PASSWORD variables to it that have been given to you
  3. Read the beginning of the Getting Started section at https://pypi.org/project/python-dotenv/ (don't download the package, you should have it already)
  4. From the Getting started section, edit the main.py file to fetch environment variables
  5. Run main.py

# Questions
  a. What is the response from the data request?
  
  b. Take a look at mock_api.credential_store.py. The username/passwords are encoded, why would an API do that?
  
  c. Here is publicly available encoding method used (without a seed or cypher). Why would that in real-life situation be unwise?
  
  d. What encoding method is used? Look in mock_api.functions.py for hints...
  
  e. BONUS: Use the internet to decode the credential_store and find the order of names.
  
