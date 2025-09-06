import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for coloured output
colorama.init()

# Prolog: The start of the program
print(f"{Fore.CYAN}👋 Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Agent" # Fallback if user doesn’t provide a name

# Store conversation as a list of tuples (text, polarity, sentiment_type)
conversation_history = []

print(f"{Fore.CYAN}Hello, {user_name}!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}I will analyze your sentences with TextBlob and show you the sentiment. 🕵️")
print(f"{Fore.CYAN}Type {Fore.YELLOW}'exit'{Fore.CYAN} to quit, or {Fore.YELLOW}'reset'{Fore.CYAN} to clear conversation history.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}👉 Enter some text: {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}! 🕵️{Style.RESET_ALL}")
        break

    if user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🔄 All conversation history cleared!{Style.RESET_ALL}")
        continue

    if user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}⚠️ No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Color coding based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW

                print(f"{idx}. {color}[{sentiment_type}] {text} "
                      f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with sentiment, emoji, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity score: {polarity:.2f}){Style.RESET_ALL}")
