# Movie Recommender System

A content-based movie recommender implemented in a Jupyter Notebook. The project uses the TMDB 5000 dataset (movies + credits) and builds recommendations by combining movie metadata (genres, keywords, cast, crew/director, and overview) into a single feature representation and computing pairwise similarities.

This repository contains an exploratory notebook (Untitled.ipynb) that walks through data loading, preprocessing, feature extraction, and generating recommendations.

---

## Table of contents

- [Project overview](#project-overview)
- [Dataset](#dataset)
- [What's included](#whats-included)
- [How it works](#how-it-works)

---

## Project overview

The notebook builds a content-based recommender system by:

- Parsing the TMDB CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`).
- Extracting and normalizing relevant fields (genres, keywords, top cast, director, overview).
- Combining these fields into a single text-like “metadata” field per movie.
- Vectorizing the metadata and computing similarity (e.g., cosine similarity).
- Providing lookups that return the most similar movies for a given title.

This approach is explainable, fast to compute at small-to-medium scale, and works well when metadata carries strong signals (cast, genre, keywords).

---

## Dataset

This notebook expects the following CSV files in the notebook working directory:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These are commonly available as the "TMDB 5000 Movie Dataset" (e.g., on Kaggle). The notebook reads these files, merges the credits into the movies dataframe, and then performs preprocessing.

---

## What's included

- Untitled.ipynb — Jupyter notebook containing:
  - Data loading and inspection
  - Parsing JSON-like columns (genres, keywords, cast, crew)
  - Cleaning, transforming and combining metadata
  - Building a content-based recommender
  - Example recommendations and demonstration cells

(If you add scripts, serialized models, or a simple Flask/Streamlit app, list them here.)

---

## How it works (high level)

1. Load CSVs and merge credits into the movies dataframe.
2. Select relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
3. Parse JSON strings in columns like `genres`, `keywords`, `cast`, `crew` into Python objects and extract the fields you need (e.g., genre names, top 3 cast, director).
4. Preprocess text data:
   - Tokenize overview, remove punctuation/stopwords if desired.
   - Flatten lists into single-space-separated strings where appropriate.
   - Lowercase tokens to normalize.
5. Combine the fields into one "metadata" string per movie (e.g., `"genres keywords cast director overview"`).
6. Vectorize the metadata using CountVectorizer or TfidfVectorizer.
7. Compute cosine similarity between movies.
8. For a given movie title, find its index and return the top-N most similar movies by similarity score.

---

