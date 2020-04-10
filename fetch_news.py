from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="531b40e00dc142bfb2ad71704c08d40e") #this will allow us to access newsapi service. get key from https://newsapi.org/


#will fetch top-headlines

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
#to fetch everything

all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)


#to fetch the all news sources

sources = newsapi.get_sources()






