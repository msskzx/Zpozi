# Zpozi

### Installation

 - Clone the repo

 - Create a `.env` file
  - CLIENT_ID = 'app client id'
  - CLIENT_SECRET = 'app client secret'
  - REDIRECT_URI = 'http://localhost:8000'


 - So far, `username` at `app.py` could be changed manually to a different Spotify username

 - make sure `python` and `pip` are installed
 - In the project directory:
  - `mkvirtualenv zpozi`
  - `pip install dotenv`
  - `pip install spotipy`

- Run a `python` server `python -m http.server`
- Run the app `python app.py`

![Alt text](img/run.PNG?raw=true "Run")

- Copy the web address on the browser and paste it in the console

![Alt text](img/auth_code.PNG?raw=true "Auth")

- you will get the names of the playlists including private ones

![Alt text](img/playlists.PNG?raw=true "Playlists")
