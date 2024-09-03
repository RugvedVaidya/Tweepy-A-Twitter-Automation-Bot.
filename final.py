import tweepy
import openai
import news as n
import random
# to import apis from different (python) file 
from apii import key , bearer_token , api_key , api_secret , access_token , access_token_secret

# to 
client = tweepy.Client(bearer_token , api_key , api_secret , access_token , access_token_secret)
auth = tweepy.OAuth1UserHandler(bearer_token , api_key , api_secret , access_token , access_token_secret)
api = tweepy.API(auth)

# to store the chat log 
chat_log = []
c = random.randint(0,len(n.headlines)-1)
mes = n.headlines[c].text.strip()
user_mes = 'Generate proper hashtags for maximum engagement on the text. Maximum 8 hashtags on the text. generate only text and not numbers, '+mes
# to get the response
chat_log.append({"role": "user", "content": user_mes})
response =openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = chat_log
    )

#to just get actual mes than whole json / all the information
assistance_response = response['choices'][0]['message']['content']

print(mes, ' ' ,assistance_response,sep='')

# to tweet the response generated 

#client.create_tweet(text = assistance_response.strip("\n").strip())
#print("Tweeted Successfully")
#chat_log.append({"role": "assistance","content": assistance_response.strip("\n").strip()})
