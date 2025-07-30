from langchain_community.chat_models import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

memory = ConversationBufferMemory(memory_key="history", return_messages=True)

def get_llm(model_choice):
    if "GPT-4" in model_choice:
        return ChatOpenAI(model_name="gpt-4", temperature=0)
    elif "GPT-3.5" in model_choice:
        return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    else:
        return ChatGroq(model_name="llama3-70b-8192", temperature=0)

def get_tax_agent_response(user_input, model_choice):
    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
You are a multilingual, global AI Tax Agent.
You can answer tax-related questions for any country including Pakistan, India, UK, USA, Canada, etc.
Use only the user's question to infer the context.
If the country isn't clear, give a general answer and recommend checking with a local expert.

Question:
{input}
"""
    )
    llm = get_llm(model_choice)
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    return chain.run(user_input)
