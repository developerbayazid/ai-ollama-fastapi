from ollama import chat
from fastapi.responses import StreamingResponse


msg_context=[]

def generate_response(prompt: str):
    
    # msg context
    msg_context.append(
        {
            "role" : "user",
            "content" : prompt
        }
    )
    
    # generate response
    def generate():
        stream = chat(
            model="phi3",
            messages=msg_context,
            stream=True
        )
        
        full_response = ""
        
        for chunk in stream:
            content = chunk.message.content
            full_response+=content
            yield content
            
        # Ai response save to context
        msg_context.append(
            {
                "role" : "assistant",
                "content" : full_response
            }
        )
        
    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )
    