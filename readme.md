# 3 Part Comparison Between My Codebase vs. Angela Yu's

## Learning Reflections

I completed this project independently without referencing the course's provided solution code. 
This approach allowed me to fully engage my problem-solving skills and rely on my understanding of Python and the principles of software development.
I intentionally over-engineered the project beyond the scope of the assignment guidelines to push my learning of OOP and other aspects of development. 
After completion, I compared my solution to the instructor's and noted several differences that are detailed in this file. 

The code comparisons in this file are not about judging which code was superior but about understanding different ways to approach a problem. 
The instructor, Angela Yu, assigned this as an intermediate level project and I assume her code choices were strategically designed to meet that level of learner.
In no way am I delusional enough to consider myself close to the level of programmer she is.

Simply put, my code was designed differently because I wanted to challenge myself beyond the intermediate level project requirements.
The code I implemented was written with the intent to dive deeper into Python's capabilities and to challenge myself to enhance my ability to better account for user experience considerations.
This caused many hours of frustrating debugging as I implemented many new concepts for the first time, but I am thankful for the valuable learning I gained from the experience.
It was also enlightening to see how the pong game, or any game, could be implemented in different ways based on a programmer's design wishes.

This practice of independently creating and then subsequently comparing has been very valuable in developing my analytical skills and will no doubt be a central theme I continue throughout my journey to improve as a developer. 
It's a reminder that in programming, as in all learning, there are many paths to a destination, and each one can provide a unique perspective that can broaden one's horizons and skill set.

I hope that sharing my journey and the insights gained from this comparison can inspire others to embrace the learning process, not be afraid of attacking problems on their own, and appreciate the value in reviewing and learning from the work of others after first engaging the challenge independently. 
To me, this practice has been a testament to the quality learning that can be gained from courses like Angela Yu's by pushing yourself beyond the baseline project requirements.
I hope that this project can serve as an inspiration for others to not only learn from educational courses like hers but also to expand upon them and create something unique.

Finally, the analysis below of how my code varied from Angela's provided a valuable opportunity for self-reflection on my coding practices and I hope it can do the same for you.

## Part 1 - Overall Structure and Code Organization

### Modularity and Use of Classes
- My solution exhibits a high degree of modularity with distinct classes for each component (`Paddle`, `Ball`, `Scoreboard`, `GameConfig`, and `DetectCollision`), enhancing readability and maintainability.
- My `GameConfig` and `DetectCollision` classes were designed to account for encapsulation by bundling related properties and methods together.

### User Customization
- The `GameConfig` class allows players to customize game parameters like screen size and colors, adding an interactive element to the game setup.
- Paddle and ball characteristics, including color, are customizable via user input to provide a more engaging user experience.
- Logic is built into my `GameConfig` class through the `validate_color_contrast` function to ensure the game text color contrasts with the screen's background color.
- In the future, I need to iterate on the codebase by building in logic that ensures paddle and ball colors are also handle to guarantee contrast with the screen's background color.

### Boundary Checking for Paddles
- Paddle movement is constrained within vertical wall boundaries, ensuring realistic and controlled gameplay.

### Error Handling
- My code accounted for proactive error handling with try-except blocks in the main game loop for exceptions like `TurtleGraphicsError`, `ValueError`, and other general exceptions.
- I do not believe try-except error handling has been taught in the course yet up to this point.

### Logging
- Logging is implemented throughout my game, specifically within the main game loop and important operations. 
- This was the first experience I have had with implementing logging. 
- I forced myself to learn some aspects of logging to push my development as a programmer who can better account for debugging and maintenance.
- Logging has not yet been addressed in the course.

### Comparison to Angela's Codebase Structure and Organization

- **Modularity**: Angela's codebase, while structured, lacks the same level of encapsulation and modularity. Essential functionalities like game settings and collision detection are not separated into distinct classes in her solution.
- **Customization**: Angela's codebase does not provide options for user input customization as seen in my code.
- **Boundary Checking**: Angela's code does not include boundary checks for paddles and I included this to increase the realism of the gameplay.
- **Error Handling and Logging**: Angela's code lacks comprehensive error handling and logging, which is crucial for robustness and maintainability.
- **Collision Detection**: My code demonstrates more advanced collision detection between the paddle and ball to increase the accuracy of the gameplay experience.

## Part 2 - Gameplay Mechanics and User Interaction

### Collision Detection
- My `DetectCollision` class was designed to account for the principles of single responsibility and separation of concerns.
- My code includes detailed methods for collision detection to improve the accuracy and feel of the game for the user.

### Score Management
- The `Scoreboard` class handles game scoring and includes methods for updating and displaying scores, as well as a game over message, to enhance the game's user interface and gameplay.
- Both mine and Angela's code contained score handling, but mine differs in the inclusion of a game over message.

### Keyboard Bindings and Event Handling
- I implemented keyboard bindings for paddle movement. My code does not differ from Angela's in this respect, but I mention it because this experience introduced me to the concept of event-driven programming for the first time.
- My program uses screen click events to provide an additional method for ending the game. I implemented this to provide the user with more interactivity with and control over the game.

### Game Conclusion Mechanism
- My code includes a mechanism to end the game when a player reaches a predetermined winning score, enhancing the structure and competitive nature of the game.
- A function is called to conclude the game, displaying a game over message and ensuring a definitive end to gameplay.
- There is potential for me to improve the code by implementing a user input feature to provide the user with the choice to set the winning score value according to their desire.

### Comparison to Angela's Codebase

- **Collision Detection**: Angela's code employs a simpler approach to collision detection, which may not account for all edge cases.
- **Score Management**: Both codebases manage scoring effectively. However, my code further enhances the user experience with a developed game over display.
- **Event Handling**: While Angela's codebase handles key events for gameplay, it lacks the feature of using click events to end the game.
- **Game Conclusion Mechanism**: Angela's code lacks a mechanism to end the game based on players reaching a specific score. This omission means her game lacks a defined endpoint, which could arguably impact player engagement and the sense of competition.

## Part 3: Code Quality and Best Practices

### Documentation
- I was intentional about including comprehensive docstrings and comments throughout the codebase to increase understanding and maintaining the code. 
- Each class and method of my program is described with their purpose and functionality to facilitate ease of use and future modification.

### Game End Mechanics
- My ame end mechanics include the use of a timer to delay automatic closing of the game window to make sure that the game over message and end-game information are properly displayed to users.

### Adherence to Python Standards
- I believe that my code adheres well to Pythonic principles and standards. I am learning the importance of this consideration as it relates to readability and maintainability.
- My belief around this comes from consciously trying to follow PEP 8 guidelines for code formatting, use clear and meaningful variable names, and effectively leverage Python's built-in functions.

### Error Handling and Logging
- I challenged myself to implement logging to manage error handling in the game loop. My motivation to do this is from a desire to become a programmer that can proactively handle debugging and maintenance through the actual code.
- The logging in my code records game events and errors.

### Comparison to Angela's Codebase

- **Documentation**: Angela's code, while clear, does not contain the same level of detailed documentation as found in my code. This does not mean anything negative about her code documentation, and it is possible I went overboard in this area.
- **Game End Mechanics**: Angela's codebase does not include a mechanism to delay the game window closure. This omission can impact the user experience by not allowing sufficient time to view the game over message.
- **Python Standards**: Both of our codebases adhere to Python standards. I personally believe that my code shows more in this respect around error handling and class structure. Again, I intentionally exceeded the difficulty level requirement.
- **Error Handling and Logging**: Angela's codebase does not contain any error handling designed to catch specific exceptions. Likewise, her code does not contain any logging features.

## Other Areas for Improvement Going Forward
- **Unit Testing**