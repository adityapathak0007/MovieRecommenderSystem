# MovieRecommenderSystem
Overview
The Movie Recommender System is a web application built using Streamlit. It recommends movies based on user input using a similarity matrix derived from movie features. The app allows users to select a movie from a dropdown menu and displays a list of recommended movies along with their posters.

Features
Movie Recommendations: Provides a list of recommended movies based on the selected movie.
Movie Posters: Displays movie posters for recommended movies.
Dark Theme: The app uses a dark theme for a modern look and feel.
Technologies Used
Python: Programming language used for developing the app.
Streamlit: Framework used for building the interactive web application.
Pandas: Library used for data manipulation and analysis.
Requests: Library used for making HTTP requests to fetch movie posters.
Gdown: Library used for downloading files from Google Drive.
Pickle: Python library used for serializing and deserializing objects.
Installation
Prerequisites
Ensure you have Python 3.7 or higher installed on your system.

Install Dependencies
Clone the repository and install the required packages:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
Requirements File
Create a requirements.txt file with the following content:

makefile
Copy code
streamlit==1.19.0
pandas==2.1.0
requests==2.28.2
gdown==4.6.0
Usage
Download Required Files:

The app requires two files: similarity.pkl and movie_dict.pkl.
These files are used to load the similarity matrix and movie data.
Update the file_url variable in the script to the Google Drive link of similarity.pkl.
Run the App:

Use the following command to start the Streamlit app:
bash
Copy code
streamlit run app.py
The app will open in your default web browser.
How It Works
Data Loading:

The app downloads the similarity matrix and movie dictionary files from Google Drive.
It loads the similarity matrix and movie data into memory.
Movie Selection:

Users select a movie from a dropdown list populated with movie titles.
Recommendation Generation:

Upon clicking the "Show Recommendations" button, the app uses the similarity matrix to find and display similar movies.
Movie posters and titles of recommended movies are fetched and displayed.
Configuration
You can configure the app by updating the following variables in the script:

file_url: URL for downloading the similarity.pkl file.
Update the api_key in fetch_poster function with your own API key if needed.
Troubleshooting
ModuleNotFoundError: Ensure all dependencies are installed. Check the requirements.txt file.
File Download Issues: Verify the file_url and ensure you have internet access.
Contributing
Contributions are welcome! If you find a bug or want to add a feature, please open an issue or submit a pull request.

Fork the Repository
Create a New Branch
Make Your Changes
Commit and Push Your Changes
Submit a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, please contact Your Name.
