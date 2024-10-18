# RetroStats Server

This is an open-source project aim to parse, save and share the scores of the most popular retro-games of all time. 

## Table of contents
- [How it works?](#how-it-works)
- [Installation](#installation)
- [Registration](#registration-inside-our-api)
- [Contributing](#contributing)
- [Roadmap](#roadmap)

## How it works?

It uses RetroPie as a base and it is mostly developed to work inside a Raspberry (Rasbperry + RetroPie = Arcade Machine Setup) but probably will work in other kind of setups since it uses Python. 

Right now it's currently being develop for the MAME (Multi Arcade Machime Emulator) framework but we will continue including new emulators and games whenever it is posible. How it actually works is parsing the binary scores saved by the MAME system into a human-readable file and store them wherever we like, local database or API. This has to be done for each game, since everyone of them saves the scores in different formats and there is no one-to-rule-them-all function that can convert the binary files into the format that we want.

## Installation

Well, you will need some things configured before actually use the system:
-   Pip 24.2
-   Python 3.9.6
-   RetroPie X.X.X
#
- Clone the project in your machine with Retropie and install the dependencies:
```
    $ git clone https://github.com/thewickest/retrostats-server.git
    $ cd retrostats-server
```
- Install depedencies and setup the local database:
```
    $ make setup
```
This will setup a local database in case you were not able to connect to and external API to save the scores and configure the environment variables that the project needs.

You are good to go! If the project supports the game you want to play, you will be able to store the scores outside the system.

## Registration inside our API

This project uses an custom API to store the scores for each game. It also stores the scores into a local database in case something wrong happened or you don't have an API at all. So the system connects to this API and stores the scores, simple isn't?

In order to be able to do that an use our API, first you have to being registed inside of it (your machine mostly). Right now we don't have a registration process as such, but we plan to include it. If you want to use our API just contact us and we will generate a username/password for you. This is only need to see who uses the API and block them in case they perform malicious attacks against it, so don't worry about the username since it's going to be random.

## Contributing

See our [contributing guidelines](CONTRIBUTING.md) to include new games inside the project.

## Roadmap
- [ ] <ins>**Games**</ins>: We plan to include every game posible so dont hesitate to contribute if you see that your favorite game is missing!
- [ ] <ins>**Cool logs**</ins>: Cool logs when you finish some game session. Pixelart or something like that. Right now they are pretty basic. 
- [ ] <ins>**RFID Identification**</ins>: Imagine the possibilities to use a RFID card to being identify into the system. You could be using the machine with more than one people and still save the scores for each person.