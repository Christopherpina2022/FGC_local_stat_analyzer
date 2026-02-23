# WFGC Headcounter
This app is designed to send requests to the Start.gg API to look for attendees of *Crossover ICT* to create two main Queries:
* TODO: How many times each user has attended a Crossover ICT Tournament
* Every placement a user has gotten up to the Top 8 standings
* TODO: filter top 8 standings by game category

## Setup
1. Go to [This page and follow the instructions](https://developer.start.gg/docs/authentication) to get an API key from the start.gg Developer portal.
2. Setup your .env file to include the [Endpoint](https://developer.start.gg/docs/sending-requests) and the API Key you got from step 1. keys should be "API_KEY" and "ENDPOINT_URL"
2. setup Python Environment (python -m venv venv -> ./venv/scripts/activate) then run the requirements.txt to get dependencies. Python version used was *Python 3.13.11*.

## Execution
In your virtual environemnt run this:
`python main.py [COMMAND]`

### Available Commands
* top8 - gets a list of players that were in the Top 8 standings
* headcount - counts every user who attended the tournament and how many times

### Arguments
* --perpage [AMOUNT] - how many tournaments you want to pass per page to reduce complexity amount

## Handing API restrictions
The Start.gg API has two main restrictions:
* Maximum 80 Requests per minute
* Maximum 1000 complexity (objects that are returned including nested objects)

each query will return a smaller page of data that will then be concatenated into a larger data dictionary to help reduce the requests made, but if the number of participants are too high which caps the complexity amount, you will need to reduce the number of tournaments to query (for Crossover ICT, the sweet spot is 25 tournaments per page). sometimes a tournament has so many entries that it's not possible to meet this requirement in one run, so as a solution, the data you request will be cached into a CSV file of results.