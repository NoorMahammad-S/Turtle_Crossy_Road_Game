from turtle import Turtle

# Define a font for the scoreboard
FONT = ("Courier", 24, "normal")

# Create a Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):

    # Constructor method to initialize the scoreboard
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)  # Set the initial position for the scoreboard
        self.update_scoreboard()  # Display the initial level

    # Method to update the scoreboard with the current level
    def update_scoreboard(self):
        self.clear()   # Clear the existing text on the scoreboard
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    # Method to increase the level
    def increase_level(self):
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the displayed level

    # Method to display "GAME OVER" message
    def game_over(self):
        self.goto(0, 0)  # Position the "GAME OVER" message at the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Display "GAME OVER" message