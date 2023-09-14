# Computer Vision Rock-Paper-Scissors Game

![Rock-Paper-Scissors Game](game_screenshot.png)

## Overview

This project is a computer vision-based implementation of the classic rock-paper-scissors game against the computer. The game is written in Python and utilizes TensorFlow to build a neural network model for gesture recognition and OpenCV to access the computer's camera for user input.

### Features

- Play a best-of-three series of the classic rock-paper-scissors game against the computer.
- Computer makes random selections.
- Option to choose "Nothing," representing no gesture.
- Keep track of user and computer wins.
- Real-time camera feed for user input.

## How to Play

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   
2. Install the required packages:
   ```bash
   pip install tensorflow opencv-python
  
3. Follow the on-screen instructions to play the game. Use hand gestures for rock, paper, and scissors, or choose the "Nothing" option.

## Gameplay

The game uses computer vision to recognize your hand gestures as rock, paper, or scissors. Here's how it works:

- You'll see yourself on the screen through your computer's camera.
- Make a gesture for rock, paper, or scissors with your hand.
- The game will display your choice, and the computer will make a random selection.
- The round's winner is determined, and the game keeps track of user and computer wins.
- The game continues until either the user or the computer wins three rounds.

## Manual Mode (Optional)

If you prefer not to use your camera, you can play the game in manual mode by running manual_rps.py. Simply enter your choice (rock, paper, or scissors) when prompted.

## Customization

You can customize the game by modifying the labels.txt file to recognize additional gestures. Each line in labels.txt should contain an index and label separated by a space. For example:
    0 Rock
    1 Paper
    2 Scissor
    3 CustomGesture
You can train the model to recognize the corresponding gestures.

## Technologies Used

Python: The game is written in Python.
TensorFlow: Used to build the neural network model for gesture recognition.
OpenCV: Used to access the computer's camera and process live video feed.
Contributing

Contributions to this project are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or create a pull request.

## License

This project is licensed under the MIT License.

Enjoy playing Rock-Paper-Scissors with computer vision! If you have any questions or suggestions, feel free to contact me at manishsudhir8@gmail.com.









