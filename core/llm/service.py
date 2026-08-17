from langchain_google_genai import ChatGoogleGenerativeAI

from core.config import settings


class LLMService:

    """Class that provides context to LLM and generates natural language response"""

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=settings.model_name,
            api_key=settings.gemini_api_key,
            temperature=0.2,
        )

    def generate(self,message: str,context: str = ""):

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question using the provided
document context.

If the answer cannot be found in the context,
say that you could not find the answer in the
uploaded documents.

Do not invent information.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{message}
"""

        response = self.model.invoke(prompt)

        return response.content