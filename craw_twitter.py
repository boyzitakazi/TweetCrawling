import tweepy
import pandas as pd
import time


# Autentikasi
consumer_key = "XXXXXXXXX"
consumer_secret = "XXXXXXXXX"
access_token = "XXXXXXXXX"
access_token_secret = "XXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# Query dengan text
tweets = []

def text_query_to_csv(text_query,count):
    try:	
    # mengambil tweet dengan query
        for tweet in api.search(q=text_query, count=count):

          # menambahkan daftar yang berisi tweet diatas ke tweets[]
          tweets.append((tweet.created_at,tweet.id,tweet.text))

          # Membuat data frame menggunakan pandas dari tweet
          tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])

          # Convert to csv
          tweetsdf.to_csv('{}-tweets.csv'.format(text_query)) 

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)


# masukan text_query untuk menscrape tweet dan beri nama file csv
# maksimal tweet yang diambil
text_query = 'COVID-19'
count = 150

# gunakan function untuk memanggil
text_query_to_csv(text_query, count)