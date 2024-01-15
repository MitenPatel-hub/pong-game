# utils.py

def get_user_input(prompt, default, cast_type=str):
    """
    Gets user input with a prompt and a default value. Optionally casts the input to a specified type.

    Args:
        prompt (str): The input prompt to display to the user.
        default: The default value to use if no input is provided.
        cast_type (type): The type to cast the user input. Default is str.

    Returns:
        The user input cast to 'cast_type', or the default value if the input is invalid or empty.
    """
    while True:
        try:
            user_input = input(f"{prompt} (Press Enter to use default: '{default}'): ") or default
            return cast_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid value.")
