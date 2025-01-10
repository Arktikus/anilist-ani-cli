# Copyright 2025 - Arktikus

import time
import rich
import requests
from rich.console import Console

tool_name = "AniList-Ani-CLI (aa-cli)"
url = "https://graphql.anilist.co"

console = Console()

def request_currently_viewing(user_name):
    query = '''
    query ($UserName: String) {
      MediaListCollection(userName: $UserName, type: ANIME, status: CURRENT) {
        lists {
          entries {
            media {
              id
              title {
                romaji
                english
                native
              }
              coverImage {
                large
              }
              episodes
              format
            }
          }
        }
      }
    } 
    '''

    variables = {
        'UserName': user_name
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    console.print(response.json())

def selection():
    while (True):
        console.print("[white]---[/white]What do you want to do?[white]---[/white]")
        console.print("[purple](1)[/purple] Get currently viewing Animes")
        i = input()

        match i:
            case '1':
                console.print("Type in your username:")
                u = input()
                request_currently_viewing(u)
            case _:
                console.print("[bright_red]Wrong input...[/bright_red]")

def print_greeting():
    console.print("[bold underline purple]%s[/bold underline purple]" % tool_name)

def init():
    console.log("Initializing...")
    time.sleep(1)
    console.log("Initialized!")

if __name__ == "__main__":
    init()
    print_greeting()
    selection()
