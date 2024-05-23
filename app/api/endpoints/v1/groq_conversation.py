from fastapi import APIRouter, HTTPException, Depends, Header, Response
from app.schemas import ChatRequest
from app.config import settings
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.chains import LLMChain
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from urllib.request import unquote

from app.permissions import verify_api_key

router = APIRouter()


conversational_memory_length = 10
memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True) 

@router.post("/conversation")
async def chat_with_model(
                          chat_request: ChatRequest,
                          api_key: str = Depends(verify_api_key),
                          x_api_key: str = Header(None, alias='x-api-key')
                          ):
    try:
        model = chat_request.llmModel
        if model is None or model == '':
            model = 'llama3-8b-8192'
        
        print(model)
        
        # Initialize Groq Langchain chat object and conversation
        groq_chat = ChatGroq(
                    groq_api_key=settings.GROQ_API_KEY, 
                    model_name= model
            )
        # .with_structured_output(method='json_mode').with_retry(stop_after_attempt=5)  
        
        user_question = unquote(chat_request.userPromptUrlEncoded)
        
        system_prompt = unquote(chat_request.systemPromptUrlEncoded)
        
        # Construct a chat prompt template using various components
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),  # This is the persistent system prompt that is always included at the start of the chat.

                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  # This template is where the user's current input will be injected into the prompt.
            ]
        )

        # Create a conversation chain using the LangChain LLM (Language Learning Model)
        conversation = LLMChain(
            llm=groq_chat,  # The Groq LangChain chat object initialized earlier.
            prompt=prompt,  # The constructed prompt template.
            verbose=True,   # Enables verbose output, which can be useful for debugging.
            memory=memory,  # The conversational memory object that stores and manages the conversation history.
        )
        
        # The chatbot's answer is generated by sending the full prompt to the Groq API.
        response = conversation.predict(human_input=user_question)
        message = {'human':user_question,'AI':response}
        print("chatbot's answer:"+message)
        memory.save_context(
                {'input':message['human']},
                {'output':message['AI']}
                )
        return Response(status_code=200, content=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
