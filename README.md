# IMACS

**IMACS has been replaced with [IMACS 2.0](https://github.com/UWARG/IMACS-2)**.

This repository contains the code to create and run the graphical user interface that maps information from the drone.

To use the project locally on your machine:

- Clone the repository and open the project folder in the desired workspace.
- Open the desired workspace, and create a virtual environment using:
    - `python -m venv <environment name>`
- Activate the environment
    - `source <environment name>/bin/activate`
- Add submodule
    - `git submodule init`
    - `git submodule update`
- Install all required dependencies in the virtual environment
    - `pip install -r requirements.txt`
- Once all dependencies have been installed, run the `server.py` file
- Open a new terminal window, and run:
    - `python3 GroundStationGUI.py`


There you go! A new window should appear with the Ground Station GUI.
