# FGC Local Stat Analyzer
This app is designed to send requests to the Start.gg API to look for attendees of *Crossover ICT* to create two main Queries:
*  How many times each user has attended a Crossover ICT Tournament
* Every placement a user has gotten up to the Top 8 standings
* filters both results from both overall data and then by game

## Setup
1. Go to [This page and follow the instructions](https://developer.start.gg/docs/authentication) to get an API key from the start.gg Developer portal.
2. Setup your .env file to include the [Endpoint](https://developer.start.gg/docs/sending-requests) and the API Key you got from step 1. keys should be "API_KEY" and "ENDPOINT_URL"
3. setup Python Environment (python -m venv venv -> ./venv/scripts/activate) then run the requirements.txt to get dependencies. Python version used was *Python 3.13.11*. 

## Execution
In your virtual environemnt run this:
`python main.py [Tournament Name] [State Code] [Optional Arguments]`

### Commands
* top8 - gets a list of players that were in the Top 8 standings
* headcount - counts every user who attended the tournament and how many times

### Optional Arguments
* --perpage [AMOUNT] - how many tournaments you want to pass per page to reduce complexity amount

## Handing API restrictions
The Start.gg API has two main restrictions:
* Maximum 80 Requests per minute
* Maximum 1000 complexity (objects that are returned including nested objects)

each query will return a smaller page of data that will then be concatenated into a larger data dictionary to help reduce the requests made, but if the number of participants are too high which caps the complexity amount, you will need to reduce the number of tournaments to query (the default is at 25 per page)

## Other Information
The query I built for *headcount* caps at 50 users per tournament since this was a tool 
meant for a small local tournament; so big events or online tournaments with big numbers 
will be noticably lacking in data. to fix this, you can go into queries.py and raise the 
perPage amount on line 41. Do note that doing so will increase the complexity of the 
search (see handling API Restrictions)