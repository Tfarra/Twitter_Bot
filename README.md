# Twitter_Bot
Bot that tweets every x time. Using Tweepy api
0. Create a Twitter account

----------------------------

1. Create an application in https://developer.twitter.com/ to have access to the API;
2. Install all necessary libraries. pip install XXXX;
3. Create a config.py file and set the keys in variables: API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET;
4. Set the hashtags that will be used to search tweets;
5. Set how frequently tweets will be posted. (less than 15 minutes is unadvised);
6. Optional-> To post NY TIMES news instead of existing tweets, get the keys in https://developer.nytimes.com and set them up in the get_html.py file. Then change the 'is_news' variable to True.
7. Run bot.py and you will be posting tweets every X minutes.

ps: A file called existing.txt will be created and will keep track of duplicates, avoiding them.

