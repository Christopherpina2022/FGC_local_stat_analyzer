# WFGC Headcounter
This app is designed to send requests to the Start.gg API to look for attendees of *Crossover ICT* to create two main Queries:
* How many times each user has attended a Crossover ICT Tournament
* Every placement a user has gotten up to the Top 8 standings

## Setup
1. Go to [This page and follow the instructions](https://developer.start.gg/docs/authentication) to get an API key from the start.gg Developer portal.
2. Setup your .env file to include the [Endpoint](https://developer.start.gg/docs/sending-requests) and the API Key you got from step 1.
2. setup Python Environment (python -m venv venv -> ./venv/scripts/activate) then run the requirements.txt to get dependencies. Python version used was *Python 3.13.11*.

## Execution
In your Venv, run:
`python main.py`

## Handing API restrictions
The Start.gg API has two main restrictions:
* Maximum 80 Requests per hour
* Maximum 1000 complexity (results that are returned)

each query will return a smaller page of data that will then be concatenated into a larger data dictionary to help reduce the requests made, but if the number of participants are too high which caps the complexity amount, you will need to reduce the number of tournaments to query. sometimes a tournament has so many entries that it's not possible to meet this requirement in one run, so as a solution, the data you request will be cached into a CSV file of results.

### The Start/End Date parameter
Feature will be included later to explain how to use.