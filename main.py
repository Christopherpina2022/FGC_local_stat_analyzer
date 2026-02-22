import os
from dotenv import load_dotenv

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT
from parser import parse_top8
from analytics import computePlayerStats

load_dotenv()
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
if not ENDPOINT_URL:
    raise RuntimeError("GraphQL Endpoint is not set.")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API Key is not set.")

client = GraphQLClient(ENDPOINT_URL, API_KEY)

top8_nodes = client.fetch_tournament_info(TOP_8)
#headcount_nodes = client.fetch_tournament_info(HEADCOUNT)

results = parse_top8(top8_nodes)

stats = computePlayerStats(results)

for player_id, data in stats.items():
    print(data["gamerTag"])
    print("Attended:", data["attended"])
    print("Top 8:", data["top8"])
    print("Placements:", dict(data["placements"]))
    print()