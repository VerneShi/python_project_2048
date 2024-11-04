import game_functions 

def main():
    while True:
        mat = game_functions.start_game()
        game_functions.print_matrix(mat)

        while True:
            x = input("Press the command (W/A/S/D), Q to exit, R to restart: ").strip().upper()
                
            if x == 'R':
                print("Restarting the game...")
                break
            
            if x == 'Q':
                print("Exiting the game. Goodbye!")
                return

            if x not in ['W', 'A', 'S', 'D']:
                print("Invalid Key Pressed. Please use only W, A, S, or D.")
                continue

            # Mapping input to corresponding move functions
            move_functions = {
                'W': game_functions.move_up,
                'A': game_functions.move_left,
                'S': game_functions.move_down,
                'D': game_functions.move_right
            }

            # Execute the appropriate move function based on user input
            mat, flag = move_functions[x](mat)

            # Check the state of the game after the move
            status = game_functions.get_current_state(mat)
            print(status)

            # Continue the game or end it based on the game state
            if status == 'GAME NOT OVER':
                game_functions.add_new_2(mat)
                game_functions.print_matrix(mat)
            else:
                print(status)
                break
            

if __name__ == '__main__':
    
    try:
        main()
    
    except KeyboardInterrupt:
        print('\nGame interrupted by user.')
    except Exception as general_error:
        print(f"A critical error occurred: {str(general_error)}")
