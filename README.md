# Maki
**Powerful tool for managing complex Anki decks**

Maki is a build and development tool for managing Anki decks with custom note templates and styled cards. It does this by decoupling these from the Anki deck format and building to it using [GenAnki](https://github.com/kerrickstaley/genanki).

## Project Structure
### Basic

```
.
├── dist/
│   └── main_deck
├── decks/
│   └── main_deck/
│       └── notes.toml
├── models/
│   └── basic_note/
│       └── model.toml/
│           └── basic/
│               ├── front.html
│               ├── back.html
│               └── style.css
└── maki.config.json
```

This project structure defines a project with one root deck, one note type, and one card type for that note. 

### Advanced

```
.
├── dist/
│   ├── first_deck
│   └── second_deck
├── decks/
│   ├── first_deck/
│   │   └── notes.toml/
│   │       ├── subdeck1/
│   │       │   └── notes.toml
│   │       └── subdeck2/
│   │           └── notes.toml
│   └── second_deck/
│       └── notes.toml
├── models/
│   ├── vocab_note/
│   │   ├── model.toml
│   │   ├── front_back/
│   │   │   ├── front.html
│   │   │   ├── back.html
│   │   │   └── style.css
│   │   └── back_front/
│   │       ├── front.html
│   │       ├── back.html
│   │       └── style.css
│   └── basic_note/
│       └── model.toml/
│           └── basic/
│               ├── front.html
│               ├── back.html
│               └── style.css
└── maki.config.json
```

## Usage
### Create a project
```
maki new             create new project in current working directory
maki new my_deck     create new project in my_deck directory if it is empty or does not exist
```
### Live Preview

Maki offers a live web server with a UI for previewing your note designs and flashcards. To view this, run:

`maki server`

This command will host a preview interface on an available local port (`3453`, or a random available port if that port is busy).

### Build
To build your deck, run `maki build`. By default, this will build all top level folders in `decks` to the `build` directory.

## Configuration


      
maki.config.json
  
