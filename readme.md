# WFGC Headcounter
This app is designed to send requests to the Start.gg API to look for attendees of *Crossover ICT* to create two main Queries:
* How many times each user has attended a Crossover ICT Tournament
* Every placement a user has gotten up to the Top 8 standings

## Setup
1. Go to [This page and follow the instructions](https://developer.start.gg/docs/authentication) to get an API key, the .env variable should be API_KEY.
2. setup Python Environment (python -m venv venv -> ./venv/scripts/activate) then run the requirements.txt to get dependencies. Python version used was *Python 3.13.11*.