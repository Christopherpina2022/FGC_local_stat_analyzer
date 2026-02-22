import requests

class GraphQLClient:
    def __init__(self, url: str, token: str | None = None):
        self.url = url
        self.headers = {
            "Content-Type": "application/json"
        }

        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    
    def execute(self, query: str, variables: dict | None = None) -> dict:
        response = requests.post(
            self.url,
            json={
                "query": query,
                "variables": variables or {}
            },
            headers=self.headers
        )

        response.raise_for_status()
        result = response.json()

        if "errors" in result:
            raise Exception(result["errors"])

        return result["data"]

    def fetch_tournament_info(client, query):
        page = 1
        all_nodes = []

        # First request
        data = client.execute(query, {"page": page})

        tournaments = data["tournaments"]
        total_pages = tournaments["pageInfo"]["totalPages"]

        all_nodes.extend(tournaments["nodes"])

        # Remaining pages
        for page in range(2, total_pages + 1):
            data = client.execute(query, {"page": page})
            all_nodes.extend(data["tournaments"]["nodes"])

        return all_nodes