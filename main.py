from anna_agent import AnnaAgent
from logger import ConversationLogger

def run_anna():
    anna = AnnaAgent(kb_path="kb/knowledge_base.txt")
    logger = ConversationLogger("logs/session_log.json")
    
    print("Hi, I’m Anna, your startup coach! Ask me anything about starting a business.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Anna: Talk soon, and keep building!")
            break
        
        response, reasoning = anna.respond(user_input)
        print(f"Anna: {response}")
        print(f"[Reasoning: {reasoning}]")
        
        logger.log_turn(user_input, response, reasoning)

if __name__ == "__main__":
    run_anna()
