from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def welcome_message():
    print("\nWelcome to AI-Powered Text Completion Application!\n")

def options() -> None:
    """
    Displays available options for the user.
    """
    print("Available Options:")
    print("1. Generate Text Completion")
    print("2. Configure Settings")
    print("3. Exit")

def generate_response(user_input, temperature=1, max_output_tokens=2048, top_p=1) -> str:
    """
    Generates a response from the AI model based on user input.
    Args:
        user_input (str): The input text from the user.
    Returns:
        str: The AI-generated response.
    """
    try:
        response = client.responses.create(
        model="gpt-4.1-nano",
        input=f'{user_input}',
        reasoning={},
        tools=[],
        temperature=1,
        max_output_tokens=2048,
        top_p=1,
        store=True
        )
        return response.output_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    


def main():
    """Main loop for the CLI application."""
    DEFAULT_TEMPERATURE = 1
    DEFAULT_MAX_OUTPUT_TOKENS = 2048
    DEFAULT_TOP_P = 1
    temperature = DEFAULT_TEMPERATURE
    max_output_tokens = DEFAULT_MAX_OUTPUT_TOKENS
    top_p = DEFAULT_TOP_P
    welcome_message()
    while True:
        options()
        choice = input("\nPlease select an option (1-3): ").strip()
        if choice == '1':
            user_input = input("Please enter your text: ")
            if not user_input.strip():
                print("Input cannot be empty. Please try again.\n")
                continue
            returned_response = generate_response(user_input, temperature, max_output_tokens, top_p)
            if returned_response:
                print(f"AI Response: {returned_response} \n")
        elif choice == '2':
            print(f"\nCurrent Settings: temperature={temperature}, max_output_tokens={max_output_tokens}, top_p={top_p}\n")
            try:
                temp_input = input('Please Enter your Temperature from 0 to 1 (Press "enter" to keep the current): ').strip()
                if temp_input:
                    try:
                        temp_val = float(temp_input)
                        if 0 < temp_val < 1:
                            temperature = temp_val
                        else:
                            print("Invalid value, keeping the current value.")
                    except ValueError:
                        print("Invalid input, keeping the current value.")
                tokens_input = input('Please Enter your Max_output_tokens (Press "enter" to keep the current): ').strip()
                if tokens_input:
                    try:
                        tokens_val = int(tokens_input)
                        max_output_tokens = tokens_val
                    except ValueError:
                        print("Invalid input, keeping the current value.")
                top_p_input = input('Please Enter your top_p from 0 to 1 (Press "enter" to keep the current): ').strip()
                if top_p_input:
                    try:
                        top_p_val = float(top_p_input)
                        if 0 < top_p_val < 1:
                            top_p = top_p_val
                        else:
                            print("Invalid value, keeping the current value.")
                    except ValueError:
                        print("Invalid input, keeping the current value.")
                print("Configuration updated.\n")
            except Exception as e:
                print(f"Error Occurred: {e}")
                continue
        elif choice == '3':
            print("Exiting the Application.")
            break
    
if __name__ == "__main__":
    main()

