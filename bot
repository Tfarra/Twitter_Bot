import config
import numpy as np
import tweepy as tw
import pandas as pd
import time
import random
import get_html as aux
import datetime as datetime

temas=['news','trump','covid', 'sports','breaking',
       'america','stocks', 'market'] # hashtags to search
random.shuffle(temas)
print(temas)

def get_tema():
    rand=len(temas)
    chosen=random.random()*rand
    chosen = int(np.floor(chosen))
    try:
        return temas[chosen]
    except:
        return 'random'

def get_tema1(lista : list,i: int): 
    try:
        return lista[i]
    except:
        return 'enw'
    
def get_temas():
    return temas

def get_tweets(hashtag: str):
    # Collect tweets
    tweets = tw.Cursor(api.search_tweets,
                           q=hashtag,
                           lang="en",tweet_mode='extended').items(10)
    
    #Get most liked tweets from the 5
    chosen_tweet=None
    tweet_mode='extened'
    soma_max=-1
    for twt in tweets:
        rtt=twt.retweet_count
        likes=twt.favorite_count
        if rtt+likes > soma_max:
            soma_max=rtt+likes
            chosen_tweet=twt      
    #Follow,like and return  
    favorited = chosen_tweet.favorited      
    if chosen_tweet:
        try:
            if not favorited:
                api.create_favorite(id=chosen_tweet.id)
            api.create_friendship(screen_name=chosen_tweet.user.screen_name,
                                  user_id=chosen_tweet.user.id,
                                  follow=False)
        except:
            try:
                api.create_friendship(screen_name=chosen_tweet.user.screen_name,
                                      user_id=chosen_tweet.user.id,
                                      follow=False)
            except:
                print(f'Cant follow {chosen_tweet.user.screen_name}')
        try:
            return chosen_tweet.retweeted_status
        except AttributeError:
            return chosen_tweet




if __name__ == '__main__':
    auth = tw.OAuthHandler(config.API_KEY,
                           config.API_KEY_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN,
                          config.ACCESS_TOKEN_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)
    i=0
    j=0
    listas=get_temas()
    news=aux.get_news()
    is_news=False # IF TRUE, IT TWEETS ARTICLES FROM THE NYTIMES. FALSE, IT TWEETS EXISTING TWEETS

    
    
    
    while True:
        if is_news:
        
        ######################## NY TIMES TWEETING ##########################
        
            for piece in news:
                new = piece[0] + '\n' + piece[1] + '\n' + piece[2]
                if len(new)>280:
                    new= piece[0] + '\n' + piece[1]
                    if len(new)>280:
                        new = piece[0]
                print(new)
                existing_tweets_write = open("existing.txt", "a",encoding='utf-8')
                existing_tweets_read = open("existing.txt", "r",encoding='utf-8')
                existing_tweets_read.seek(0)
                existing_tweets_write.seek(0)
                try:
                    if not (str(hash(new)) in existing_tweets_read.read()):
                        api.update_status(new)
                        existing_tweets_write.write(str(hash(new)))
                        time.sleep(3600)
                except:
                    print('cant publish the article:\n' + new)
            is_news=False
        else:
        
            ####################### TWEETING EXISTING TWEETS ##########################
        
        
            if len(listas)==0:
                listas=['news','trump','covid', 'sports','breaking',
                        'america','stocks', 'market']
            tema=get_tema1(listas, i)
            tweet=get_tweets(tema)
            
            existing_tweets_read = open("existing.txt", "r",encoding='utf-8')
            existing_tweets_write = open("existing.txt", "a",encoding='utf-8')
            existing_tweets_read.seek(0)
            existing_tweets_write.seek(0)
            if not (str(hash(tweet.full_text)) in existing_tweets_read.read()):
                try:
                    existing_tweets_write.write(str(hash(tweet.full_text)))
                except Exception as e:
                    print(e)
                existing_tweets_write.close()
                existing_tweets_read.close()
                user = api.get_user(user_id=tweet.user.id)
                
                final=('Via ' + tweet.user.screen_name + ' : ' + 
                       tweet.full_text + ' #' + tema)
                       
                print(final + '\n')
                print(tema +'\n')
                if len(final)<=280:
                    try:
                        api.update_status(final) # TWEETS final
                        try:
                            api.create_friendship(screen_name=tweet.user.screen_name,
                                                  user_id=tweet.user.id, 
                                                  follow=False) # Follow
                        except:
                            print(f'Cant follow {tweet.user.screen_name}.')
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        print(current_time)
                        time.sleep(3600) # Stop for 1hour
                        listas.remove(tema)
                        
                    except:
                        print('Cant post') # Update not working
                        time.sleep(10)
                        listas.remove(tema)
                else:
                    print('Tweet is too long') # longer than 280 chars
                    time.sleep(10)
                    listas.remove(tema) 
            else:
                print('Repeated tweet')
                time.sleep(10)
