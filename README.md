# RetroStats Server

This is an open-source project aimed at parsing, saving, and sharing the scores of the most popular retro-games of all time.

## Table of Contents
- [How it Works?](#how-it-works)
- [Installation](#installation)
- [Registration](#registration-inside-our-api)
- [Contributing](#contributing)
- [Roadmap](#roadmap)

## How it Works?

It uses RetroPie as a base and is mostly developed to work inside a Raspberry Pi (Raspberry + RetroPie = Arcade Machine Setup) but will likely work in other kinds of setups since it uses Python.

Right now, it is currently being developed for the MAME (Multi Arcade Machine Emulator) framework, but we plan to include new emulators and games whenever possible. How it actually works is by parsing the binary scores saved by the MAME system into a human-readable file and storing them wherever we like, either in a local database or an API. This has to be done for each game, as each one saves scores in different formats, and there is no one-to-rule-them-all function to convert the binary files into the desired format.

## Installation

You will need some things configured before actually using the system:
- Pip 24.2
- Python 3.9.6
- RetroPie X.X.X

1. Clone the project onto your machine with RetroPie and install the dependencies:
```
    $ git clone https://github.com/thewickest/retrostats-server.git
    $ cd retrostats-server
```
- 2. Install dependencies and set up the local database:
```
    $ make setup
```
This will set up a local database in case you are unable to connect to an external API to save the scores and configure the environment variables that the project needs.

You are good to go! If the project supports the game you want to play, you will be able to store the scores outside the system.

## Registration Inside Our API

This project uses a custom API to store the scores for each game. It also stores the scores in a local database in case something goes wrong or you don't have an API at all. So, the system connects to this API and stores the scores, simple isn't it?

To be able to use our API, you first need to be registered (mostly for your machine). Right now, we don't have a registration process as such, but we plan to include it. If you want to use our API, just contact us, and we will generate a username/password for you. This is only needed to see who uses the API and block them in case of malicious attacks, so don't worry about the username since it's going to be random.

## Contributing

See our [contributing guidelines](CONTRIBUTING.md) to include new games in the project.

## Roadmap
- [ ] <ins>**Games**</ins>: We plan to include every game possible, so don’t hesitate to contribute if you see that your favorite game is missing!
- [ ] <ins>**Cool Logs**</ins>: Cool logs when you finish some game session. Pixel-art or something like that. Right now, they are pretty basic.
- [ ] <ins>**RFID Identification**</ins>: Imagine the possibilities of using an RFID card to be identified inside the system. You could be using the machine with more than one person and still save the scores for each individual.