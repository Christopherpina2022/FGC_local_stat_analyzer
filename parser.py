from dataclasses import dataclass

@dataclass
class top8_Result:
    gamerTag: str
    placement: int
    game: str

@dataclass
class headcount_Result:
    gamerTag: str
    game: str
    tournament_id: int

class Parser:
    @staticmethod
    def parse_top8(tournaments: list[dict]) -> list[top8_Result]:
        results = []

        for tournament in tournaments:
            for event in tournament.get("events") or []:
                gameName = (event.get("videogame")).get("name")
                standings = (event.get("standings") or {}).get("nodes") or []

                for standing in standings:
                    player = standing.get("player")
                    if not player:
                        continue

                    results.append(
                        top8_Result(
                            gamerTag = player["gamerTag"],
                            placement = standing["standing"],
                            game = gameName
                        )   
                    )
        return results
    
    @staticmethod
    def parse_headcount(tournaments: list[dict]) -> list[headcount_Result]:
        results = []

        for tournament in tournaments:
            tournament_id = tournament.get("name")
            for event in tournament.get("events") or []:
                gameName = event.get("videogame").get("name")
                entrants = (event.get("entrants") or {}).get("nodes") or []

                for entrant in entrants:
                    for participant in entrant["participants"]:
                        results.append(
                            headcount_Result(
                                gamerTag = participant.get("gamerTag"),
                                game = gameName,
                                tournament_id = tournament_id
                            )
                        )
        return results
                
