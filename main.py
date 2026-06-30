import click
import os
from dotenv import load_dotenv
from datetime import datetime

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT, USERINFO
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
@click.option("--perpage", default = 25, help = "Number of tournaments to request at a time. [Defaults to 25]")
@click.option("--start", required=False, help="Start date (YYYY-MM-DD)")
@click.option("--end", required=False, help="End date (YYYY-MM-DD)")
@click.argument("tournament_name")
@click.argument("state_code")
def top8(perpage, tournament_name, state_code, start, end):
    print("Running Top 8 Analytics...")
    # Convert timestamps to Unix Timestamp (if applicable)
    start_unix = None
    end_unix = None
    if start:
        start_unix = int(datetime.strptime(start, "%Y-%m-%d").timestamp())
    if end:
        end_unix = int(datetime.strptime(end, "%Y-%m-%d").timestamp())
    
    # Run client
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    top8_nodes = client.fetch_tournament_info(TOP_8, perpage, tournament_name, state_code, start_unix, end_unix)

    # Stop running if the query failed
    if not top8_nodes:
        print("use the above error to determine if the perpage parameter is too high (see --help)")
        return None
    top8_results = Parser.parse_top8(top8_nodes)
    top8_stats = Analytics.compute_Top8(top8_results)
    Exporter.export_top8(top8_stats)
    print("Top 8 data has been exported.")

@cli.command()
@click.option("--perpage", default = 25, help="Number of tournaments to request at a time.")
@click.option("--start", required=False, help="Start date (YYYY-MM-DD)")
@click.option("--end", required=False, help="End date (YYYY-MM-DD)")
@click.argument("tournament_name")
@click.argument("state_code")
def headcount(perpage, tournament_name, state_code, start, end):
    print("Running Headcount Analytics...")
    # Convert timestamps to Unix Timestamp (if applicable)
    start_unix = None
    end_unix = None
    if start:
        start_unix = int(datetime.strptime(start, "%Y-%m-%d").timestamp())
    if end:
        end_unix = int(datetime.strptime(end, "%Y-%m-%d").timestamp())

    # Run client
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    headcount_nodes = client.fetch_tournament_info(HEADCOUNT, perpage, tournament_name, state_code, start_unix, end_unix)

    # Stop running if the query failed
    if not headcount_nodes:
        print("use the above error to determine if the perpage parameter is too high (see --help)")
        return None
    headcount_results = Parser.parse_headcount(headcount_nodes)
    headcount_stats = Analytics.compute_headcount(headcount_results)
    Exporter.export_headcount(headcount_stats)
    print("Headcount data has been exported.")

@cli.command()
@click.argument("tournament_name")
@click.argument("state_code")
def getattendees(tournament_name, state_code):
    print("Getting attendees for " + tournament_name + "...")
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    attendee_nodes = client.fetch_tournament_attendees(USERINFO, 1, tournament_name, state_code) 

    # Stop running if the query failed
    if not attendee_nodes:
        print("use the above error to determine if the perpage parameter is too high (see --help)")
        return None
    attendee_results = Parser.parse_attendees(attendee_nodes)
    attendee_stats = Analytics.compute_attendees(attendee_results)
    Exporter.export_attendees(attendee_stats)
    print("Attendee data has been exported.")

if __name__ == "__main__":
    cli()