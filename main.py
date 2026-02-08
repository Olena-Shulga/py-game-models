import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player in players.items():
        race = player["race"]
        race_obj, created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        if created:
            for skill in race["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )
        guild_obj = None
        if player["guild"] is not None:
            guild_obj, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
