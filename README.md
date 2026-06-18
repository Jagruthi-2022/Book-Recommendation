A Machine Learning-based Book Recommendation System that suggests similar books based on user rating patterns. The system uses K-Nearest Neighbors (KNN) with Cosine Similarity to find books that are most similar to a selected book.

Dataset
download the Book Recommendation Dataset from kaggle
Books.csv
Users.csv
Ratings.csv

Features
Recommends books based on user ratings
Uses Collaborative Filtering approach
KNN-based similarity search
Cosine similarity for accurate recommendations
Sparse matrix optimization for faster computation
Model and data persistence using Pickle

Technologies Used
Python
Pandas
NumPy
Scikit-learn
SciPy
Pickle


Project Workflow
Load and preprocess datasets
Filter active users and popular books
Create a Book-User Pivot Table
Convert pivot table into a sparse matrix
Train a KNN model using cosine similarity
Generate book recommendations
Save trained model and processed data using Pickle

Model
Algorithm: K-Nearest Neighbors (KNN)
Similarity Metric: Cosine Similarity
Search Algorithm: Brute Force
Saved Artifacts

The following files are generated after training:

artifacts/
├── model.pkl
├── books_name.pkl
├── final_ratings.pkl
└── book_pivot.pkl

How to Run
pip install -r requirements.txt
python main.py

Example Recommendation

Input:
Harry Potter and the Sorcerer's Stone

Output:
Harry Potter and the Chamber of Secrets
The Hobbit
Percy Jackson
The Chronicles of Narnia
Lord of the Rings
Future Improvements
Add content-based recommendations
Deploy as a Streamlit web application
Improve recommendation quality using hybrid models
Integrate user authentication and personalized profiles