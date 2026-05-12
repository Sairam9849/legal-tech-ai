from openai import OpenAI 
 
client = OpenAI() 
 
def get_embedding(text): 
   return client.embeddings.create( 
       model="text-embedding-3-small", 
       input=text 
   ).data[0].embedding 
