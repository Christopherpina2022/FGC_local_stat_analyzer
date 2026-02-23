import csv
from pathlib import Path
class Exporter:

    @staticmethod
    def export_top8(stats, filename="top8.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Overall header
            writer.writerow(["Overall Top 8 Stats"])
            writer.writerow([
                "gamerTag",
                "Top8 Achieved",
                "1st", "2nd", "3rd", "4th", "5th", "7th", "8th"
            ])

            # Overall players
            overall_sorted = sorted(
                stats["overall"],
                key=lambda p: p["top8"],
                reverse=True
            )
            for player in overall_sorted:
                placements = player["placements"]
                writer.writerow([
                    player["gamerTag"],
                    player["top8"],
                    placements.get(1, 0),
                    placements.get(2, 0),
                    placements.get(3, 0),
                    placements.get(4, 0),
                    placements.get(5, 0),
                    placements.get(7, 0),
                    placements.get(8, 0)
                ])

            # Per-game sections
            for game, players in stats["by_game"].items():
                writer.writerow([])  # blank row
                writer.writerow([f"{game} Top 8 Stats"])
                writer.writerow([
                    "gamerTag",
                    "Top8 Achieved",
                    "1st", "2nd", "3rd", "4th", "5th", "7th", "8th"
                ])
                
                game_sorted = sorted(
                    stats["by_game"][game],
                    key=lambda p: p["top8"],
                    reverse=True
                )
                for player in game_sorted:
                    placements = player["placements"]
                    writer.writerow([
                        player["gamerTag"],
                        player["top8"],
                        placements.get(1, 0),
                        placements.get(2, 0),
                        placements.get(3, 0),
                        placements.get(4, 0),
                        placements.get(5, 0),
                        placements.get(7, 0),
                        placements.get(8, 0)
                    ])
    
    @staticmethod
    def export_headcount(stats, filename="headcount.csv"):

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Overall
            writer.writerow(["Overall Attendance"])
            writer.writerow(["gamerTag", "attendance"])

            # Sort overall by attendance descending
            sorted_overall = sorted(
                stats["overall"], key=lambda x: x["attendance"], reverse=True
            )
            for player in sorted_overall:
                writer.writerow([player["gamerTag"], player["attendance"]])

            writer.writerow([])

            # Per Game
            for game, players in stats["by_game"].items():
                writer.writerow([f"Game: {game}"])
                writer.writerow(["gamerTag", "attendance"])

                # Sort players by attendance descending
                sorted_players = sorted(
                    players, key=lambda x: x["attendance"], reverse=True
                )
                for player in sorted_players:
                    writer.writerow([player["gamerTag"], player["attendance"]])

                writer.writerow([])