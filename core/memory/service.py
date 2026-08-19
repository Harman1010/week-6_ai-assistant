class MemoryService:

    """This class provides conversation history management"""

    def __init__(self):

        self.conversations = {}

    def get_history(self,session_id:str):

        if session_id not in self.conversations:

            self.conversations[session_id] = []

        return self.conversations[session_id][-10:]

    def add_message(self,session_id:str,role:str,content:str):

        if session_id not in self.conversations:

            self.conversations[session_id] = []

        self.conversations[session_id].append({
            "role" : role,
            "content" : content
        })

    #def format_history(self,session_id:str) ->str:

        #history = self.get_history(session_id)

        #if not history:

            #return "No previous conversations"

        #return "\n".join(
            #f"{message['role'].capitalize()} : {message['content']}"
            #for message in history
        #)

