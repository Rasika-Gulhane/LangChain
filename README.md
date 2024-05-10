# LangChain
Complete understanding of Open AI LangChain LLM

#Document followed:
https://python.langchain.com/docs/get_started/introduction/

Chapters:
1. LangChain integaration and understanding prompt, chaining and history collecting with ConversationBufferMemory
2. Further understanding of prompts and FewShotPromptTemplate
3. PDF Query Using Langchain Q/A chain (Includes Text Embedding for classification, Search, recommendation, detection, etc)
4. LLM Model with Deployment using HuggingFace Spaces
5. RAG (Retrieval Augmentated Generation) basic wth custom retrieval
6. OLlama : Chatbot


## Working with langChain
Part: 1
- OPENAI_API KEY: Create your openAI API key 
- Generate HuggingFace access token (Read)
- Install all the requirements 
- Run the required chapter python file using streamlit run

Part: 2
- LANGCHAIN_API_KEY: Create ypur Langchain API key
- LANGCHAIN_PROJECT: ProjectName

## Streamlit Run

- run on local host: http://localhost:8501/

## Deploy to HuggingFace spaces

- Create new Space with SDK paramenter 'Streamlit':
https://huggingface.co/spaces/rasika-gulhane/LLM_Chatbot_Q-A

- Follow the steps to deploy git repo
- Spaces > Settings : Add the secrets for OpenAI access key
- Go to App in Home page
- Good to Run

