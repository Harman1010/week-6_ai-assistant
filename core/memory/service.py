class MemoryService:

    """This class provides conversation history management"""

    def __init__(self,coversations:str):

        self.conversations = {}

    def get_history(self,session_id:int):

        return self.conversations.get(session_id,[])

    def add_message(self,session_id:int,role:str,content:str):

        if session_id not in self.conversations:

            self.conversations[session_id] = []

        self.conversations.append(
            "role" : role,
            "content" : content
        )