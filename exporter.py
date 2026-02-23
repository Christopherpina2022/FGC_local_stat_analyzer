import csv
from pathlib import Path

def export_top8_stats(stats, filename="player_stats.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow([
            "player_id",
            "gamerTag",
            "top8's Achieved",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "7th",
            "8th"
        ])

        for player_id, data in stats.items():
            placements = data["placements"]

            writer.writerow([
                player_id,
                data["gamerTag"],
                data["top8"],
                placements.get(1, 0),
                placements.get(2, 0),
                placements.get(3, 0),
                placements.get(4, 0),
                placements.get(5, 0),
                placements.get(7, 0),
                placements.get(8, 0),
            ])

    print("CSV exported successfully.")