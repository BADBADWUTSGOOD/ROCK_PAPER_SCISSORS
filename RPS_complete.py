import random

N_GAMES = 5

def main():
    print_welcome()
    player_score = 0
    for i in range (5):
        ai_choice = get_ai_choice() #function call for ai move
        player_choice = get_player_choice() #function call for players move 
        winner = winning_parameter(ai_choice, player_choice) #function to print the winner of the round
        player_score = round_feedback(ai_choice, player_choice, winner,player_score)
        print("")
    print ("You finished with a total score of: ", player_score)

def round_feedback(ai_choice, player_choice, winner,player_score): #Function that returns text feedback of the round and updates the players total score
    if winner == "Player wins!":
            player_score += 1
    elif winner == "AI wins":
            player_score -= 1
    else:
            player_score +=0
    print ("The computer chose", ai_choice, "against your choice of", player_choice.lower())
    print (winner)
    print ("")
    return player_score

def get_ai_choice(): #The AI RPS selection for the round
    ai_choice = random.randint(1,3)
    if ai_choice == 1:
     return "rock"
    if ai_choice == 2:
     return "paper"
    if ai_choice == 3:
     return "scissors"

def get_player_choice(): #Function to gather the input of the player's RPS choice

    while True:
        player_choice = input("Please enter your RPS choice: ")
        if player_choice.lower() == "rock":
            return player_choice
        if player_choice.lower() == "paper":
            return player_choice 
        if player_choice.lower() == "scissors":
            return player_choice
        print ("Invalid choice")
        print (" ")

def winning_parameter(ai_choice, player_choice): #Checks the players input against the AI's to decide upon the winner of the round
    if ai_choice == player_choice.lower():
        return "It is a tie!"
    if ai_choice == 'rock':
        if player_choice.lower() == "scissors":
            return "AI wins"
        return "Player wins!"
    if ai_choice.lower() == "paper":
        if player_choice == "rock":
            return "AI wins"
        return "Player wins!"
    if ai_choice.lower() == "scissors":
        if player_choice == "paper":
            return "AI wins"
        return "Player wins!"

def print_welcome(): #Prints a welcome statement
    print('Welcome to Rock Paper Scissors aka RPS')
    print('You will play '+str(N_GAMES)+' rounds against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('Try your best for a perfect score! :)')
    print('----------------------------------------------')
    print('')


if __name__ == '__main__':
    main()
