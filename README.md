# Tune-Finder
A Song Recommendation Engine

## Introduction
This project aims to recommend songs similar to the input song to the user. The songs are recommended based on Artist(s), Album name, Genre and Popularity.

This project is a form of Content-based filtering. A Content-based recommendation system analyzes the characteristics or attributes of items (e.g., genre, tempo, instrumentation in music) to recommend items similar to those a user has liked before.

## Key Features
**Data**: This is a dataset of Spotify tracks with over a range of 125 different genres. Each track has some audio features associated with it. The data is in tabular CSV format and can be loaded quickly.
https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

**Algorithms**: I have used `PorterStemmer()` from `nltk` to tokenize the tags column. The integral parameter for finding the similarities is `cosine_similarity`.

## Libraries used
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* nltk
