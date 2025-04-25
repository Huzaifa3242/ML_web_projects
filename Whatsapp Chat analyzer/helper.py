import urlextract
import matplotlib.pyplot as plt
from urlextract import URLExtract
from wordcloud import WordCloud
exreactor=URLExtract()
def show_stats(selected_user,df):
    if selected_user !="Overall":
        df=df[df["users"]==selected_user]
    num_messages=df.shape[0]
    words=[]
    for i in df['messages']:
            words.extend(i.split())
    media=df[df["messages"]=="<Media omitted>\n"].shape[0]

    # links
    links=[]
    for l in df["messages"]:
         links.extend(exreactor.find_urls(l))
         
    return num_messages,len(words),media,len(links)




def fetch_most_busy_users(df):
     x=df["users"].value_counts().head()
     df=round(df["users"].value_counts() / df.shape[0]*100,2).reset_index().rename(columns={"count":"percent","users":"Name"})
     return x,df


def create_wordcloud(selected_user,df):
    if selected_user !="Overall":
        df=df[df["users"]==selected_user]
    wc=WordCloud(height=500,width=500,min_font_size=10,background_color="white")
    df_wolrldcloud=wc.generate(df["messages"].str.cat(sep=" "))
    return df_wolrldcloud
