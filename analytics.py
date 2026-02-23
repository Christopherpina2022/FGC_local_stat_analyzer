from collections import defaultdict

class Analytics:

    @staticmethod
    def compute_Top8(results):
        stats = defaultdict(lambda: {
            "gamerTag": "",
            "top8": 0,
            "placements": defaultdict(int)
        })

        for result in results:
            game = result.game
            player_id = result.player_id

            player_stats = stats[game][player_id]

            player_stats["gamerTag"] = result.gamerTag
            player_stats["placements"][result.placement] += 1
            if result.placement <= 8:
                player_stats["top8"] += 1

        return stats
    
    @staticmethod
    def compute_headcount(results):
        temp = {
            "by_game": defaultdict(lambda: defaultdict(lambda: {
                "gamerTag": "",
                "attendance": 0
            })),
            "overall": defaultdict(lambda: {
                "gamerTag": "",
                "attendance": 0
            })
        }

        for result in results:
            game = result.game
            gamerTag = result.gamerTag

            # Count attendance per game
            temp["by_game"][game][gamerTag]["gamerTag"] = gamerTag
            temp["by_game"][game][gamerTag]["attendance"] += 1

            # Count overall attendance
            temp["overall"][gamerTag]["gamerTag"] = gamerTag
            temp["overall"][gamerTag]["attendance"] += 1

        # Convert to list for export
        stats = {
            "by_game": {game: list(players.values()) for game, players in temp["by_game"].items()},
            "overall": list(temp["overall"].values())
        }
        return stats
