# 👋 Hello there! This file contains ready-to-edit bot code.
# 🟢 Open "README.md" for instructions on how to get started!
# TL;DR Run ./connect (or .\connect.cmd on Windows) to begin.

class Bot:
    def __init__(self, config):
        print("Hello World!", config)
        self.config = config
        self.prev_xy = None

    def move(self, paddle, ball):
        # This prints the position of your paddle and the ball to the bot terminal.
        # Use these values to determine which direction your paddle should move so
        # you hit the ball!
        #print("paddle", paddle["x"], paddle["y"])
        #print("ball", ball["x"], ball["y"])

        # Return the direction you'd like to move here:
        # "north" "south" "east" "west" or "none"
        target_y = ball["y"]
        returning = False
        target_x = paddle["x"]
        if(self.prev_xy is not None):
            if(self.prev_xy[0] < ball["x"]): # traveling east
                returning = self.config["paddle"] == "east"
            else:
                returning = self.config["paddle"] != "east"

            if(returning):
                current_y = ball["y"]
                current_x = ball["x"]
                slope = (current_y - self.prev_xy[1]) / (current_x - self.prev_xy[0]) # only zero if the ball isn't moving - hopefully not true ;)
                intercept = slope*(-35 - current_x) + current_y
                target_y = intercept
                if( current_x - self.prev_xy[0] > -1): # moving slow
                    target_x = target_x + 1
            else:
                target_y = 0
                target_x = -35
                
        self.prev_xy = (ball["x"], ball["y"])


        ret = "none"
        if(paddle["y"] - target_y > 1):
            ret = "south"
        elif(paddle["y"] - target_y < -1):
            ret = "north"

        if ret == "none": # no need to move north/south
            ret = "west" if target_x > paddle["x"] else "east"
        return ret

    def end(self, paddle, ball):
        print("Good game!")
