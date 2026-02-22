from dataclasses import dataclass

@dataclass
class User:
    id: int
    gamerTag: str
    placement: int

def parse_tournament(data: dict) -> list[Result]:
    results = []

    tournament = data["tournament"]

    for event in tournament["events"]:
        standings = event["standings"]["nodes"]

        for standing in standings:
            placement = standing["placement"]
            participants = standing["entrant"]["participants"]

            for p in participants:
                player = p["player"]

                results.append(
                    User(
                        player_id=player["id"],
                        gamer_tag=player["gamerTag"],
                        placement=placement
                    )
                )

    return results