import os
from dotenv import load_dotenv
import csv
from pathlib import Path

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT
from parser import parse_top8
from analytics import computeTop8Stats
from exporter import export_top8_stats

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

top8Results = parse_top8(top8_nodes)

top8Stats = computeTop8Stats(top8Results)

export_top8_stats(top8Stats)