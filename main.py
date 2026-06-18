import numpy as np
import streamlit as st
import pickle

st.header("Book Recommendation System")
model= pickle.load(open("artifacts/model.pkl","rb"))
books_name = pickle.load(open("artifacts/books_name.pkl","rb"))
final_rating= pickle.load(open("artifacts/final_rating.pkl","rb"))
book_pivot= pickle.load(open("artifacts/book_pivot.pkl","rb"))

def fetch_poster(suggestion):
    book_name=[]
    ids_index=[]
    poster_url=[]

    for book_id in suggestion[0]:
        book_name.append(book_pivot.index[book_id])

    for name in book_name:
        ids= np.where(final_rating["title"]==name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]["img_url"]
        poster_url.append(url)

    return poster_url

def recommend_books(book_name):
    book_list=[]
    book_id= np.where(book_pivot.index ==book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1),n_neighbors=6)

    poster_url= fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
        return book_list, poster_url

selected_book = st.selectbox(
    "Type or Select a Book", books_name
)

if st.button("Show Recommendation"):
    recommendation_books, poster_url = recommend_books(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])

page_bg_img='''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1535905748047-14b2415c77d5?q=80&w=850&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
}
</style>
'''

st.markdown(page_bg_img,unsafe_allow_html=True)


