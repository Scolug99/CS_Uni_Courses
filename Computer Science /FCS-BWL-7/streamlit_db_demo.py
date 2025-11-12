"""
This is a short demo of how to use a local 
SQLite database in a streamlit web application
"""

# import the relevant libraries
import streamlit as st
import pandas as pd
import sqlite3

# setup the basic page config
st.set_page_config(
    page_title="A short database demo",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# title of the page
st.title("A short database demo")

# connect to the database
DB = sqlite3.connect('chinook.db')

# query the database for all artists 
artists = pd.read_sql("""
            SELECT DISTINCT * 
            FROM artists
            ORDER BY Name
            """
            , DB, index_col=['ArtistId']) 

# output the artists just that we get an idea
st.header('This is how the artists table looks like')
st.dataframe(artists)

# use the list of artists for a multiselect box
st.header('Who are your favorite artists?')
artist_options = st.multiselect('Select your favorite artists', artists)

# see what has been selected
st.write('You selected:', artist_options)

# now let's find all the albums of the selected artists
# we first construct our search string 
search_string = ""

for artist in artist_options:
    if len(search_string) > 0:
        search_string += ', '
    search_string += f'"{artist}"'

albums = pd.read_sql(f"""
            SELECT Name, Title 
            FROM albums
            INNER JOIN artists
                ON artists.ArtistID = albums.ArtistID
            WHERE Name IN ({search_string})
            ORDER BY Name
            """, DB) 

st.header('Here are all the albums of your favorite artists')
st.dataframe(albums)


st.header("What's next?")
st.write('''
    ### Album or Track Ratings?
    You could introduce album ratings or track ratings. And you could
    automatically generate playlists based on those ratings.
    Maybe you want to generate playlists based on your mood?

    ### Additional data
    You could add all kind of additional metadata such as album covers, etc.
    via via APIs such as the **[Discogs API](https://www.discogs.com/developers/)**.
    And there are [python libraries](https://github.com/joalla/discogs_client) 
    that make it fairly easy.

    Or directly try to play a song involving streaming services such as __Spotify__
    via the **[Spotify API](https://developer.spotify.com/documentation/web-api)**. 
    Also here some lightweight python libraries such as 
    **[Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)** are available.

    ### Other things to consider using databases in streamlit
    You may use your database in streamlit as is, or you may also use some even 
    simplers ways to interact with a database with `streamlit` means. The latter 
    me be helpful if you want to deploy your app to the streamlit cloud 
    (maybe difficult with SQLite, maybe see the rather advanced MS Azure SQL Server
    examples).

    Please find the sreamlit _connecting to data_ documentation 
    [here](https://docs.streamlit.io/library/advanced-features/connecting-to-data)

    When deploying your app with user input and dynamically created SQL queries 
    to the internet, be aware of the threat of **sql injections**. 
    [Here](https://realpython.com/prevent-python-sql-injection/) and in many 
    other places you can read what an sql injection is and how to prevent them. 
    This is an important but advanced topic.

    In the context of using databases in `streamlit` but also for other approaches 
    of **making data persistent beyond a run of a `streamlit` program or even 
    beyond a `streamlit` session**, have a look at the advanced concepts of 
    **[statefulness](https://docs.streamlit.io/library/advanced-features/session-state)** 
    and **[caching](https://docs.streamlit.io/library/advanced-features/caching)**.
    ''')




# close the database connection
DB.close()