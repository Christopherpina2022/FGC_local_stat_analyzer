import click
import os
from dotenv import load_dotenv
import csv
from pathlib import Path

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT
from parser import Parser
from analytics import Analytics
from exporter import Exporter

# Load environmental Variables
load_dotenv()
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
if not ENDPOINT_URL:
    raise RuntimeError("GraphQL Endpoint is not set.")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API Key is not set.")

@click.group()
def cli():
    pass

@cli.command()
@click.option("--perpage", default = 25, help="Number of tournaments to request at a time.")
def top8(perpage):
    print("Running Top 8 Analytics...")
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    top8_nodes = client.fetch_tournament_info(TOP_8, perpage)

    # Stop running if the query Failed
    if not top8_nodes:
        print("use the above error to determine if the perpage parameter is too high (see --help)")
        return None
    top8_results = Parser.parse_top8(top8_nodes)
    top8_stats = Analytics.compute_Top8(top8_results)
    Exporter.export_top8(top8_stats)
    print("Top 8 data has been exported.")

@cli.command()
@click.option("--perpage", default = 25, help="Number of tournaments to request at a time.")
def headcount(perpage):
    print("Running Headcount Analytics...")
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    headcount_nodes = client.fetch_tournament_info(HEADCOUNT, perpage)

    # Stop running if the query Failed
    if not headcount_nodes:
        print("use the above error to determine if the perpage parameter is too high (see --help)")
        return None
    headcount_results = Parser.parse_headcount(headcount_nodes)
    headcount_stats = Analytics.compute_headcount(headcount_results)
    Exporter.export_headcount(headcount_stats)
    print("Headcount data has been exported.")

if __name__ == "__main__":
    cli()