import random
import time
import cv2
from keras.models import load_model
import numpy as np

class RPS:
    def __init__(self):
        self.user_wins=0
        self.computer_wins=0

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.countdown(int(time.process_time()))
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            max_index = np.argmax(prediction[0])
            if max_index==0:
                print("You play: rock")
            elif max_index==1:
                print("You play: paper")
            elif max_index==2:
                print("You play: scissor")
            else:
                print("You play: Nothing")
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            return max_index

    def get_computer_choice(self):
        computer_choice = random.choice(["rock","paper","scissor"])
        return computer_choice
    
    # define the countdown func.
    def countdown(self,t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer)
            cv2.waitKey(1)
            t -= 1
        
        print('Play Now')

    def get_winner(self,computer_choice,user_choice):
        if(user_choice == 3):
            self.computer_wins+=1
            print("Invalid input from user")
        elif(computer_choice == user_choice):
            print("Draw")
        elif(computer_choice == "rock" and user_choice == 1) or \
        (computer_choice == "paper" and user_choice == 2) or \
            (computer_choice == "scissor" and user_choice == 0):
            print("User wins")
            self.user_wins+=1
        else:
            print("Computer wins")
            self.computer_wins+=1

    def play(self):
        while self.user_wins < 3 and self.computer_wins < 3:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()
            print("Computer plays:", computer_choice)
            self.get_winner(computer_choice,user_choice)
            print(f"Total Computer Wins: {self.computer_wins} and Total User Wins: {self.user_wins}")
        if self.user_wins == 3:
            print("User wins overall")
        if self.computer_wins == 3:
            print("Computer wins overall")

game=RPS()
game.play()