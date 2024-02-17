# 👋 Hello there! This file contains ready-to-edit bot code.
# 🟢 Open "README.md" for instructions on how to get started!
# TL;DR Run ./connect (or .\connect.cmd on Windows) to begin.

class Bot:
    def __init__(self, config):
        print("Hello World!", config)
        self.config = config

    def move(self, paddle, ball):
        # This prints the position of your paddle and the ball to the bot terminal.
        # Use these values to determine which direction your paddle should move so
        # you hit the ball!
        print("paddle", paddle["x"], paddle["y"])
        print("ball", ball["x"], ball["y"])

        # Return the direction you'd like to move here:
        # "north" "south" "east" "west" or "none"
        return "none"

    def end(self, paddle, ball):
        print("Good game!")
