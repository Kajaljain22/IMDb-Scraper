# Python App to fetch list of trending movies and give suggestions from them
import requests
from bs4 import BeautifulSoup
import random       #to randomly select a movie

URL = 'https://www.imdb.com/chart/top/'

def fetch_movie_list():
    response = requests.get(URL)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')    #html.parser is the default parser
    
    # Fetching Movie Years
    movies_list = soup.select('td.titleColumn')
    years = [get_year(movie_data) for movie_data in movies_list]

    # Fetching Movie Titles
    a_tag_list = soup.select('td.titleColumn a')
    titles = [tag.text for tag in a_tag_list]
    # Fetching Actors
    actors = [tag['title'] for tag in a_tag_list]
    # Fetching ratings
    ratings_list = soup.select('td.posterColumn span[name=ir]')
    ratings = [float(value['data-value']) for value in ratings_list]

    no_of_movies = len(titles)

    user_choice = "y"
    while(user_choice != "n"):
        index = random.randrange(0,no_of_movies)
        print(f'\n {titles[index]} {years[index]}\n Rating : {ratings[index]:.1f}\n Cast : {actors[index]}\n')

        user_choice = input("Do you want another suggestion (y/n) ??").lower()



def get_year(movie_data):
    movie_split = movie_data.text.split()
    year = movie_split[-1]
    return year


fetch_movie_list()
