from mblock import event
import random
rock_paper_scissor_choices = ["Rock","Paper","Scissors"]
@event.received('StartGame')
def on_received():   
    for i in range(3):
        sprite.say('Ready for another round? Choose again',2)
        sprite.say('Computer is Thinking',2)
        computer_choice=rock_paper_scissor_choices[random.randint(0,2)]
        sprite.say(computer_choice,2)
        player_choice=sprite.get_variable('result')
        if player_choice == "Rock" and computer_choice == "Rock":
            sprite.say("Draw",2)
        elif player_choice == "Paper" and computer_choice == "Rock":
            sprite.say("You win :) This round",2)    
        elif player_choice == "Scissors" and computer_choice == "Rock":
            sprite.say("You Lose this round :(",2) 
            
               
        elif player_choice == "Rock" and computer_choice == "Paper":
            sprite.say("You Lose this round :(",2)
        elif player_choice == "Paper" and computer_choice == "Paper":
            sprite.say("Draw",2)   
        elif player_choice == "Scissors" and computer_choice == "Paper":
            sprite.say("You win :) This round",2) 
        elif player_choice == "Rock" and computer_choice == "Scissors":
            sprite.say("You win :) This round",2) 
        elif player_choice == "Paper" and computer_choice == "Scissors":
            sprite.say("You Lose this round :(",2) 
        elif player_choice == "Scissors" and computer_choice == "Scissors":
            sprite.say("Draw",2)  
