from bs4 import BeautifulSoup
import requests

#Using user agent to avoid error 403
user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

#prints movie name and ratings
def print_info(name, rating):
    print("Movie:", name,"| Rating:",rating,"\n")
    return

#extracts movie name and rating from trending page of imdb
def trending_movies():
    url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    text = requests.get(url, headers={'User-Agent': user_agent}).text
    soup = BeautifulSoup(text, 'lxml')
    movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent', )
    for movie in movies:
        name = movie.find('h3', class_='ipc-title__text').get_text()
        ratings = movie.find(class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
        if ratings==None:
            ratings = 'Not specified'
            print_info(name, ratings)

        else:
            ratings = ratings.get_text()
            print_info(name, ratings)

#extracts movie name and rating from top 250 movies page of imdb
def top_250_movies():
    url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    text=requests.get(url,headers={'User-Agent': user_agent}).text
    soup = BeautifulSoup(text,'lxml')
    movies =soup.find_all('li',class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent',)
    for movie in movies:
        name= movie.find('h3',class_='ipc-title__text').get_text()
        ratings=movie.find(class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
        if ratings==None:
            ratings = 'Not specified'
            print_info(name, ratings)

        else:
            ratings = ratings.get_text()
            print_info(name, ratings)

#extracts movie name and rating according to genre
def movie_genres():
    url="https://www.imdb.com/search/title/?title_type=feature&genres=changeit&sort=user_rating,desc&explore=genres"
    genre=select_genre()
    #modifying the url to make a url to open page of specific genre in imdb
    url=url.replace("changeit",genre)
    text = requests.get(url, headers={'User-Agent': user_agent}).text
    soup = BeautifulSoup(text, 'lxml')
    movies = soup.find_all( class_='lister-item mode-advanced')
    for movie in movies:
        name = movie.h3.a.get_text()
        ratings = movie.strong.get_text()
        print_info(name, ratings)

#to select the genre
def select_genre():
    genres = {1: "action", 2: "adventure", 3: "animation", 4: "biography", 5: "comedy", 6: "crime"
    , 7: "documentary", 8: "drama", 9: "family", 10: "fantasy", 11: "history", 12: "horror",
    13: "music", 14: "mystery", 15: "romance", 16: "sci-fi", 17: "sport", 18: "thriller", 19: "war"}

    for i in range(1, 20):
        print("Enter", i, "for", genres[i])

    choice = int(input("Enter your choice: "))
    return genres[choice]

def main():
    print("Enter 1 to display top 250 movies")
    print("Enter 2 to display top trending")
    print("Enter 3 to display movies by genre")

    try:

        choice=int(input("Enter choice:"))
        if choice==1:
            top_250_movies()

        elif choice==2:
            trending_movies()

        elif choice==3:
            movie_genres()

        else:
            print("Entered wrong input")
    except:
        print("An error occured")





if __name__ == "__main__":
    main()