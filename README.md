# SECRET SANTA
    Video Demo:  https://youtu.be/SbpjOJHhKaI
  Description: The main idea of the project is to create a secret santa game. This game will consist in the user first entering the number of players and the name of each player. After this the game will ask for the name of the player that wants to know who he is gifting to until everyone knows who they are gifting so the game ends.
   I wil be defining the functions used one by one.
   The main function that kicks in when the game is started prints a welcome message using Figlet and also gives a disclaimer that the user can interrupt the game at any time by pressing Ctrl+C then the function game is called.

   Santa_asks and santa_says are two small function used for adding a santa claus emoji before the messages of the game and will be used through the game.

   The function game is called and this is where the magic happens, is the barebone of the whole game in it all the functions that make up the game are called and assigned to variables and dictionaries. On the first line of game qwe see a function called check_num_players is assigned to num.

   The function check_num_players when called enters a loop where the user is asked to input the number of player and until the number of player is nos tested as a valid number (>1) the function will not return back to game function. The function is designed to display error messages explaining why the user input is not valid if its less than 2 or not a number.

   After this, we go back to the game function storing the variable num, we assign a variable player with the return from a function called players_name in which we insert the variable num.

   The function players_name needs the variable num to work correctly as it will tell the number of players. With this information the function will enter a loop to ask one by one the name of the players and will only exit when the check_player function returns true. When all the players names have been submited and tested the function returns a dictionarie with all the players to the game function.

   check_player is a test function for the name of players provided from the user, fr the function to work as intended we need to pass to the function the name of the current player and also the players already stored. The function test if the name of the current player has been submited previously in wich case the function will print an error message telling the user the player has already been entered and return false so the user can input it again, and if this test is passed the function checks if the name of the player is alphanumerical if the test is not passed an error message is displayed and the function returns false so the user will input it again. When both this test are passed the function will return true to break out of the loop and continue inputing players or continue with the game.

   When the game function already has the players dictionary we proceed with the giveaway function, this function will assign each player another player for it to work we need to insert the players dictionary to this function.

   The giveaway function is called and opens a blank dictionary called assignated where it will store the players that have already been given to another player.
   A loop is initiated where each player from the dictionary players will receive a random number between 0 and the number of players then the variable gifted will save a random player of the players with the random position and the test check_gifted is initiated, if the test is not passed the giveaway will assign another player until the test is passed. When all the players have been assigned the last test check_giveaway kicks in and if the test is passed the function will return the assignated players dictionarie.

   Check_gifted test makes sure the player is not assigned itself and that the player that is assigned hasnt been asigned yet, if all is passed the test will return true and the giveaway will continue.

   Check_giveaway test makes sure again after the giveaway has finished that players hasn’t been assigned to themselves and that players appear only once in the assignated list. If the test is passed the giveaway function finishes but if it is not passed the giveaway is repeated and starts again the whole process.

   Back to the game function, tell_names function is called and the players and assigned list is passed.

   Tell_names is the final function in which the names are given the function asks the user to input their name for it to reveal who he is gifting. In case the player submits the name wrong all the players names are given. When the player knows who he is gifting the program asks the user to hit enter and the console clears so the next players dont see prior players assignation. When all the players have been revealed the game will end.
