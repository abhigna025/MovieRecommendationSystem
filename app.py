import streamlit as st
import pickle
import pandas as pd
import requests
import webbrowser
st.set_page_config(layout="wide")
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b932b1d1e2ececff2526ed681d352714&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):
    index_of_the_movie = titles_list[titles_list['title'] == movie].index[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)[1:6]
    #print(sorted_similar_movies)
    recommended_movie=[]
    recommended_posters=[]
    for i in sorted_similar_movies:
        movie_id=titles_list.iloc[i[0]].id
        #print(movie_id)
        recommended_movie.append(titles_list.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_posters
titles=pickle.load(open('movies_dict.pkl','rb'))
titles_list=pd.DataFrame(titles)
popular=pickle.load(open('popular.pkl','rb'))
popular_list=pd.DataFrame(popular)
sort_popular=popular_list.sort_values(by=['popularity'],ascending=False)[1:6]
#popular_df=pd.DataFrame(sort_popular)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
title_selected = st.selectbox('What is your favourite movie?'
                      ,titles_list['title'].values)
df1=pd.read_csv("hotstar1.csv")
df2=pd.read_csv("netflix.csv")
if st.button('Recommend'):
    titles,posters=recommend(title_selected)
    print(titles)
    links=[]
    for i in range(len(titles)):
        #print(i)
        for j in range(len(df1)):
            # print(df1['Movie Name'][j],i)
            #print(len(i),len(df1['Movie Name'][j]),i,df1['Movie Name'][j])
            if titles[i]==df1['Movie Name'][j][:-1]:
                links.append(('c'+str(i+1),df1['Movie Link'][j],'hotstar'))
                break
        for j in range(len(df2)):
            if titles[i]==df2['MovieName'][j]:
                links.append(('c'+str(i+1),df2['Link'][j],'netflix'))
                break
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        z=0
        st.text(titles[0])
        st.image(posters[0])
        for i in links:
            if i[0]=='c1':
                k ='[Watch this on {}]({})'.format(i[2],i[1])
                st.markdown(k, unsafe_allow_html=True)
                z=1
        if z==0:
            st.markdown("not available on hotstar/netflix")
    with c2:
        z=0
        st.text(titles[1])
        st.image(posters[1])
        for i in links:
            if i[0]=='c2':
                z=1
                k = '[Watch this on {}]({})'.format(i[2],i[1])
                st.markdown(k, unsafe_allow_html=True)
        if z==0:
            st.markdown("not available on hotstar/netflix")
    with c3:
        z=0
        st.text(titles[2])
        st.image(posters[2])
        for i in links:
            if i[0]=='c3':
                z=1
                k = '[Watch this on {}]({})'.format(i[2],i[1])
                st.markdown(k, unsafe_allow_html=True)
        if z==0:
            st.markdown("not available on hotstar/netflix")
    with c4:
        z=0
        st.text(titles[3])
        st.image(posters[3])
        for i in links:
            if i[0]=='c4':
                k = '[Watch this on {}]({})'.format(i[2],i[1])
                st.markdown(k, unsafe_allow_html=True)
                z=1
        if z==0:
            st.markdown("not available on hotstar/netflix")
    with c5:
        z=0
        st.text(titles[4])
        st.image(posters[4])
        for i in links:
            if i[0]=='c5':
                k = '[Watch this on {}]({})'.format(i[2],i[1])
                st.markdown(k, unsafe_allow_html=True)
                z=1
        if z==0:
            st.markdown("not available on hotstar/netflix")

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Popular Movies:</p>', unsafe_allow_html=True)
popular_movie=[]
popular_posters=[]
popular_movie=sort_popular['id'].tolist()
popular_title=sort_popular['title'].tolist()
#print(popular_movie)
for i in popular_movie:
     #movieid=popular_df['id'][i]
     #print(movie_id)
     #popular_movie.append(popular_df['title'][i])
     popular_posters.append(fetch_poster(i))
#print(popular_posters)
links1=[]
#df1=pd.read_csv("hotstar1.csv")
#df2=pd.read_csv("netflix.csv")
for i in range(len(popular_title)):
    #print(i)
    for j in range(len(df1)):
        # print(df1['Movie Name'][j],i)
        #print(len(i),len(df1['Movie Name'][j]),i,df1['Movie Name'][j])
        if popular_title[i]==df1['Movie Name'][j][:-1]:
            links1.append(('c'+str(i+1),df1['Movie Link'][j],'hotstar'))
            break
    for j in range(len(df2)):
        if popular_title[i]==df2['MovieName'][j]:
            links1.append(('c'+str(i+1),df2['Link'][j],'netflix'))
            break
c1,c2,c3,c4,c5=st.columns(5)
with c1:
    st.text(popular_title[0])
    st.image(popular_posters[0])
    z=0
    for i in links1:
        if i[0] == 'c1':
            k = '[Watch this on {}]({})'.format(i[2], i[1])
            st.markdown(k, unsafe_allow_html=True)
            z = 1
    if z == 0:
        st.markdown("not available on hotstar/netflix")
    with c2:
        st.text(popular_title[1])
        st.image(popular_posters[1])
        z = 0
        for i in links1:
            if i[0] == 'c2':
                k = '[Watch this on {}]({})'.format(i[2], i[1])
                st.markdown(k, unsafe_allow_html=True)
                z = 1
        if z == 0:
            st.markdown("not available on hotstar/netflix")
    with c3:
        st.text(popular_title[2])
        st.image(popular_posters[2])
        z = 0
        for i in links1:
            if i[0] == 'c3':
                k = '[Watch this on {}]({})'.format(i[2], i[1])
                st.markdown(k, unsafe_allow_html=True)
                z = 1
        if z == 0:
            st.markdown("not available on hotstar/netflix")
    with c4:
        st.text(popular_title[3])
        st.image(popular_posters[3])
        z = 0
        for i in links1:
            if i[0] == 'c4':
                k = '[Watch this on {}]({})'.format(i[2], i[1])
                st.markdown(k, unsafe_allow_html=True)
                z = 1
        if z == 0:
            st.markdown("not available on hotstar/netflix")
    with c5:
        st.text(popular_title[4])
        st.image(popular_posters[4])
        z = 0
        for i in links1:
            if i[0] == 'c5':
                k = '[Watch this on {}]({})'.format(i[2], i[1])
                st.markdown(k, unsafe_allow_html=True)
                z = 1
        if z == 0:
            st.markdown("not available on hotstar/netflix")
print(popular_movie)
print(popular_title)
print(links1)