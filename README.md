# pong-game

![](https://img.shields.io/badge/Release-v1.0-blueviolet)
![](https://img.shields.io/badge/Language-python-005255)
![](https://img.shields.io/badge/Libraries-pygame-00cfff)
![](https://img.shields.io/badge/Libraries-pygame__gui-00cfff)
![](https://img.shields.io/badge/Size-10.7Mo-f12222)
![](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

This repository is composed by a pong game source code.
The game is a beta version, many bugs are still present and the project needs a new conception for a cleaner code

![](https://github.com/FACON-Nicolas/FACON-Nicolas/raw/main/resources/pong.gif?raw=true)

# Summary

* **[Summary](#summary)**
* **[Credits](#credits)**
* **[Features](#features)**
* **[Pre-requisites](#prerequisites)**
* **[Install](#install)**
* **[Releases](#releases)**
* **[Inputs](#inputs)**
* **[Versions](#versions)**

# Credits

* **[Facon Nicolas](https://github.com/FACON-Nicolas)** : creator of the project

# Features

+ ## Scene maker 

The script called [Scene.py](src/Scene.py) could make a scene with a little json file, here this is the settings scene: 

![](https://i.ibb.co/TcpDdT3/json-file.png)

![](https://i.ibb.co/M6LbZYK/setting-scene.png)

+ ## Settings scene

The settings scene could controls the framerate and the game volume : 

![](https://i.ibb.co/M6LbZYK/setting-scene.png)

# Prerequisites

 + Windows
    - **[Python](https://www.python.org/downloads/)**
    - **[Git Bash](https://gitforwindows.org/)**
    - **pygame** (``py -3.8 -m pip install pygame`` in your terminal)
    - **pygame_gui** (``py -3.8 -m pip install pygame_gui`` in your terminal)

 + Linux:
 
    write this in terminal 
    ```sh
    #if python is not installed yet.
    sudo apt install python3.8
    #if pygame is not installed yet.
    pip install pygame
    #if pygame_gui is not installed yet.
    pip install pygame_gui
    ```

# Install

To install the game, write this in your terminal or git bash terminal 

```sh
git clone https://github.com/FACON-Nicolas/pong-game
cd pong-game/
#python3 or py on windows
python3 src/Main.py
```

# Inputs

The game contains many inputs to be playable, they are specified here: 

| inputs |    actions     |
| :----: | :------------: |
|  DOWN  |    move down   |
|   UP   |     move up    |
| ESCAPE | pause / resume |

# Versions

**1.0.0** : 2022-07-16






