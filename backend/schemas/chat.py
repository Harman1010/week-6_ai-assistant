from pydantic import BaseModel,Field

class ChatRequest(BaseModel):

    """Defines the schema for the query"""

    question : str = Field(min_length=1,max_length=1000)

    session_id : str = Field(min_length=1,max_length=100)

class Source(BaseModel):

    document : str

    page_number : int | None = None

    score : float | None = None

class ChatResponse(BaseModel):

    """Defines the schema for response"""

    answer : str

    sources : list[Source] = Field(default_factory = list)