from retriever import KnowledgeRetriever
from some_llm_wrapper import call_llm

class AnnaAgent:
    def __init__(self, kb_path):
        self.retriever = KnowledgeRetriever(kb_path)
    
    def respond(self, user_input):
        context = self.retriever.search(user_input)
        
        if "idea" in user_input.lower():
            reasoning = "I want to understand who you’re building for before suggesting validation steps."
        elif "mvp" in user_input.lower():
            reasoning = "I’m asking questions to make sure your MVP stays focused."
        else:
            reasoning = "I’m clarifying so I can give more targeted advice."
        
        prompt = f"""
        Context from knowledge base:
        {context}

        User question:
        {user_input}

        Give a helpful, actionable answer.
        If needed, ask a single follow-up question to guide the next step.
        """
        response = call_llm(prompt)
        return response, reasoning
