import numpy as np
import pandas as pd
import streamlit as st

st.title("CiniMagic")

page = st.sidebar.radio("Navigation",['Home','About me'],index=0)

if page == 'Home':
    st.subheader("Rate these movies")
    st.text("Rating these movies helps system learn about your behaviour")
    moviesWithGenres_df = pd.read_csv('gowdavidwan2003.csv')
    m1 = st.slider("Inception",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m2 = st.slider("The Dark Knight : Rises",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m3 = st.slider("The Avengers",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m4 = st.slider("Titanic",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m5 = st.slider("Pirates of the Caribbean: At World's End",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m6 = st.slider("Fifty Shades of Grey",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m7 = st.slider("The Wolf of Wall Street",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)   
    m8 = st.slider("The Fast and the Furious",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m9 = st.slider("Cars",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)
    m10 = st.slider("Annabelle",min_value=0.0,max_value= 5.0,value = 0.0,step =0.5)

    if st.button("Submit"):
        userInput = [
            {'title':'Inception', 'rating':m1},
            {'title':'The Dark Knight Rises', 'rating':m2},
            {'title':'The Avengers', 'rating':m3},
            {'title':"Titanic", 'rating':m4},
            {'title':'''Pirates of the Caribbean: At World's End''', 'rating':m5},
            {'title':'Fifty Shades of Grey', 'rating':m6},
            {'title':'The Wolf of Wall Street', 'rating':m7},
            {'title':'The Fast and the Furious', 'rating':m8},
            {'title':"Cars", 'rating':m9},
            {'title':'Annabelle', 'rating':m10}
            ]
        inputMovies = pd.DataFrame(userInput)
        inputId = moviesWithGenres_df [moviesWithGenres_df ['title'].isin(inputMovies['title'].tolist())]
        inputMovies = pd.merge(inputId, inputMovies)
        inputMovies = inputMovies
        userMovies = moviesWithGenres_df[moviesWithGenres_df['movieId'].isin(inputMovies['movieId'].tolist())]
        userMovies = userMovies.reset_index(drop=True)
        columns_to_drop = ['movieId', 'title', 'imdb_score']
        userGenreTable = userMovies.drop(columns=[col for col in columns_to_drop if col in userMovies.columns])
        #userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('imdb_score',1)
        userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
        genreTable = moviesWithGenres_df.set_index(moviesWithGenres_df['movieId'])
        #genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('imdb_score',1)
        genreTable = genreTable.drop(columns=[col for col in columns_to_drop if col in genreTable.columns])
        recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
        moviesWithGenres_df['match_score'] = recommendationTable_df
        final_recommend = moviesWithGenres_df.sort_values(by=['match_score', 'imdb_score'], ascending=[False, False])
        final = final_recommend.loc[:, ['title', 'match_score']].head(20)
        st.subheader("Recommended Movies to watch")
        st.dataframe(final,height= 741, width = 750)
        st.subheader("User Profile")
        st.dataframe(userProfile,height= 300, width = 750)

if page == "About me":
    st.image('abcd.jpeg')
    st.subheader('''I'M Vidwan Gowda H M
Data Science & Machine Learning
Enthusiast''')
    st.text('“Passionate Explorer, Innovative Learner, Collaborative Builder”')
    dataset = 'https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset'
    sourcecode = 'https://github.com/gowdavidwan2003/movie_recommendor'
    st.markdown(f'<a href={sourcecode}><button style="background-color:grey;display: block; width: 100%">Source - Code </button></a>', unsafe_allow_html=True)
    st.markdown(f'<a href={dataset}><button style="background-color:grey;display: block; width: 100%">Dataset used</button></a>', unsafe_allow_html=True)
    st.subheader("Contact me")
    first , last = st.columns(2)
    first1 , last1 = st.columns(2)
    first2 , last2 = st.columns(2)
    
    portfolio = 'https://gowdavidwan2003.github.io/portfolio'
    linkedin = 'www.linkedin.com/in/gowdavidwan2003'
    github = 'https://github.com/gowdavidwan2003'
    whatsapp = 'https://wa.me/917975045560'
    phone = 'tel:+917975045560'
    first.markdown(f'<a href={portfolio}><button style="background-color:grey;display: block; width: 100%">Portfolio website</button></a>', unsafe_allow_html=True)
    last.markdown(f'<a href={linkedin}><button style="background-color:grey;display: block; width: 100%">Linked In</button></a>', unsafe_allow_html=True)
    first1.markdown(f'<a href={github}><button style="background-color:grey;display: block; width: 100%">Github</button></a>', unsafe_allow_html=True)
    last1.markdown(f'<button style="background-color:grey;display: block; width: 100%">Email - gowdavidwan2003</button>', unsafe_allow_html=True)
    first2.markdown(f'<a href={whatsapp}><button style="background-color:grey;display: block; width: 100%">Whatsapp</button></a>', unsafe_allow_html=True)
    last2.markdown(f'<a href={phone}><button style="background-color:grey;display: block; width: 100%">Phone</button></a>', unsafe_allow_html=True)
