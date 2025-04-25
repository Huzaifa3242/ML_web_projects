import streamlit as st
import preprocessing
import helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")
file=st.sidebar.file_uploader("Choose a file")
if file is not None:
    data=file.getvalue()
    data=data.decode("utf-8")
    df=preprocessing.preprocess(data)
    st.dataframe(df)

    users_list= df["users"].unique().tolist()
    users_list.remove("group_notification")
    users_list.sort()
    users_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show Analysis wrt",users_list)



    if st.sidebar.button("Show Analysis"):
        num_messages,words,media,links=helper.show_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        col1, col2, col3,col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Total Media")
            st.title(media)
        with col4:
            st.header("Total Links")
            st.title(links)
        

        # finding the busiest users for group level
        if selected_user=="Overall":
            st.title("Most Busy Users")
            x,new_df= helper.fetch_most_busy_users(df)
            fig,ax= plt.subplots()
            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index,x.values,color="green")
                plt.xticks(rotation=50)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df, width=800)
        

        # Wordcloud
        st.title("Word Cloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        





