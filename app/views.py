from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    description: str
    team_members: list


team_dictionary = {
    "procurement": Team(
        "Procurement",
        "Handling everything related to food for students",
        ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
    "documentation": Team(
        "Documentation",
        "Taking record and performing outreach for Base Camp.",
        ["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah"],
    ),
    "community": Team(
        "Community",
        "Taking care of and planning organization for events and public representation.",
        ["AJ", "Caleb", "Joby", "Jordan", "Micah"],
    ),
    "management": Team(
        "Management",
        "Handling everything related to the general management of Base Camp students.",
        ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
}


def show_teams(
    request,
    team_name,
):
    context = {
        "team_name": team_dictionary[team_name],
    }

    return render(request, "allTeams.html", context)


def home_teams(request):
    return render(request, "base.html")


def show_members(request, team_name):
    context = {"team_name": team_dictionary[team_name]}
    return render(request, "teamMembers.html", context)
