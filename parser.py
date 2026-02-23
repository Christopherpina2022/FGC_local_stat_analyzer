from dataclasses import dataclass

@dataclass
class top8_Result:
    player_id: int
    gamerTag: str
    placement: int
    game: str

@dataclass
class headcount_Result:
    player_id: int
    gamerTag: str
    game: str

class Parser:
    @staticmethod
    def parse_top8(tournaments: list[dict]) -> list[top8_Result]:
        results = []

        for tournament in tournaments:
            for event in tournament.get("events") or []:
                gameName = event.get("name")
                standings = (event.get("standings") or {}).get("nodes") or []

                for standing in standings:
                    player = standing.get("player")
                    if not player:
                        continue

                    results.append(
                        top8_Result(
                            player_id = player["id"],
                            gamerTag = player["gamerTag"],
                            placement = standing["standing"],
                            game = gameName
                        )   
                    )
        return results
    
    def parse_headcount(tournaments: list[dict]) -> list[headcount_Result]:
        results = []

        for tournament in tournaments:
            for event in tournament.get("events") or []:
                gameName = event.get("name")

                entrants = (event.get("entrants") or {}).get("nodes") or []

                for entrant in entrants:
                    gamerTag = entrant.get("gamerTag")
                    if not gamerTag:
                        continue
                
                    results.append(
                        headcount_Result(
                            player_id = entrant["id"],
                            gamerTag = gamerTag,
                            game = gameName
                        )
                    )
                
