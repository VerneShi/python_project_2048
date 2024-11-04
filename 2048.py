import game_functions 

if __name__ == '__main__':
    
    try:
        # Initialize the matrix
        mat = game_functions.start_game()
        game_functions.print_matrix(mat)

        while True:
            try:
                x = input("Press the command (W/A/S/D), Q to exit: ").strip().upper()
                
                if x == 'Q':
                    print("Exiting the game. Goodbye!")
                    break

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
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Let's try that move again.")
    
    except KeyboardInterrupt:
        print('\nGame interrupted by user.')
    except Exception as general_error:
        print(f"A critical error occurred: {str(general_error)}")
