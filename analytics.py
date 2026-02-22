from collections import defaultdict

def computePlayerStats(results):
    stats = defaultdict(lambda: {
        "gamerTag": "",
        "attended": 0,
        "top8": 0,
        "placements": defaultdict(int)
    })

    for result in results:
        player = stats[result.player_id]

        player["gamerTag"] = result.gamerTag
        player["attended"] += 1
        player["placements"][result.placement] += 1

        if result.placement <= 8:
            player["top8"] += 1

    return stats