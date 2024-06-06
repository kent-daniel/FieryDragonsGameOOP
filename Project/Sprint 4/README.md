# Fiery dragons game
## Features implemented
- StartGameMenu
- Timer
- Player Lives
- Card effects Game Controller
- Special effects Controller
- Saving and Loading from external file
- Changing Number of players

## Preview
![img.png](preview1.png)
![img.png](preview2.png)
![Alt text](<Screen Recording 2024-05-18 at 1.57.26 pm.gif>)

## Key Files
- **config.JSON** and **config.default.JSON**: Configuration file for game settings. (However currently configuration is hardcoded in `GameDataController.py`)
- **main.py**: Entry point of the game.


## Known Issues 🐞
- Volcano cards overlapping in smaller screen dimensions

## How to run
### Steps
1. Unzip FieryDragonExe.zip
2. Look for main unix executable file

![img.png](stepstorun.png)

3. Click on the file and let it run (it might take a while to load the game)

![img_1.png](stepstorun2.png)

4. It should create a pygame window and display the game ( Game UI might be cropped if the screen dimensions are too small)