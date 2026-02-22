from dataclasses import dataclass

@dataclass
class Result:
    player_id: int
    gamerTag: str
    placement: int

def parse_top8(tournaments: list[dict]) -> list[Result]:
    results = []

    for tournament in tournaments:
        for event in tournament["events"]:
            standings = event["standings"]["nodes"]

            for standing in standings:
                player = standing.get("player")
                if not player:
                    continue

                results.append(
                    Result(
                        player_id = player["id"],
                        gamerTag = player["gamerTag"],
                        placement = standing["standing"]
                    )   
                )
    return results