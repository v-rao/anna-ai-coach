import json
from datetime import datetime

class ConversationLogger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
    
    def log_turn(self, user_input, anna_response, reasoning):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "anna": anna_response,
            "reasoning": reasoning
        }
        self.data.append(entry)
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=2)
