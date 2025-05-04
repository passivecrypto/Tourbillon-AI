# Entry point script to run the Tourbillon Bot

# Import the main execution function from the bot script
# Ensure essential_requirements.txt are installed in your venv
# Configure your parameters in config.py before running

import Tourbillonbot392ST

if __name__ == "__main__":
    print("Starting Tourbillon Bot...")
    print("Loading parameters from config.py")
    # Call the main function located within the bot script
    Tourbillonbot392ST.main()
    print("Tourbillon Bot finished or stopped.")
