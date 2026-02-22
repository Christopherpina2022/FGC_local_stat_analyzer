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
                "variables": variables
            },
            headers=self.headers
        )

        response.raise_for_status()
        result = response.json()

        if "errors" in result:
            raise Exception(result["errors"])

        return result["data"]