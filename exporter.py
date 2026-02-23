import csv
from pathlib import Path
class Exporter:

    @staticmethod
    def export_top8(stats, filename="player_stats.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow([
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

            sorted_players = sorted(
                stats.items(),
                key=lambda item: item[1]["top8"],
                reverse=True
            )

            for player_id, data in sorted_players:
                placements = data["placements"]

                writer.writerow([
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
    
    @staticmethod
    def export_headcount(stats, filename="headcount.csv"):
        """
        Exports headcount stats to CSV.
        Layout:
        - Overall first with header
        - Then each game with its own header
        """

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

            writer.writerow([])  # blank line

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

                writer.writerow([])  # blank line after each game