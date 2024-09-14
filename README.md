# Movie Recommender System 🎬

## Overview

The Movie Recommender System is a web application built using Streamlit. It recommends movies based on user input using a similarity matrix derived from movie features. The app allows users to select a movie from a dropdown menu and displays a list of recommended movies along with their posters.

## Features

- **Movie Recommendations:** Provides a list of recommended movies based on the selected movie.
- **Movie Posters:** Displays movie posters for recommended movies.

## Technologies Used

- **Python:** Programming language used for developing the app.
- **Streamlit:** Framework used for building the interactive web application.
- **Pandas:** Library used for data manipulation and analysis.
- **Requests:** Library used for making HTTP requests to fetch movie posters.
- **Gdown:** Library used for downloading files from Google Drive.
- **Pickle:** Python library used for serializing and deserializing objects.
- **Scikit-learn:** Library used for machine learning, specifically for feature extraction and similarity computation.
- **NLTK:** Library used for natural language processing, specifically for stemming.

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

## Download Required Files

The app requires two files to function correctly:

1. **`similarity.pkl`**: Contains the similarity matrix used to find similar movies.
2. **`movie_dict.pkl`**: Contains the movie data needed for recommendations.

To ensure that the app works properly:

1. **Update the `file_url` Variable:**

   - In the `app.py` script, update the `file_url` variable with the Google Drive link to the `similarity.pkl` file.
   - The `file_url` should look something like this: `https://drive.google.com/uc?id=<your-file-id>`.

   Example:
   ```python
   file_url = "https://drive.google.com/uc?id=1nRxFIkLs-lfRtUVozJCUAEssNkiigzd8"


## View the App

You can view the live Movie Recommender System app by clicking on the link below:

[View Movie Recommender System](https://movierecommendersystem-3mwpnnrwcxlph9wavxwhob.streamlit.app/)


### Install Dependencies

Clone the repository and install the required packages:

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt



