import urlextract
from urlextract import URLExtract
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