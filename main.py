import os
from dotenv import load_dotenv

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT

load_dotenv()
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
if not ENDPOINT_URL:
    raise RuntimeError("GraphQL Endpoint is not set.")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API Key is not set.")

pageCount = 1


