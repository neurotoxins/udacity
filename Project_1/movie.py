import movieClass
import fresh_tomatoes
import tmdbsimple as tmdb
import httplib
import simplejson

#replace this key
tmdb.API_KEY='Placeholder_API_KEY'
# getting youtube trailer url using tmdb api
def get_youtube_url(movie_id):
    conn = httplib.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    request = "/3/movie/" + str(movie_id) + \
            "/videos?language=en-US&api_key="+str(tmdb.API_KEY);
    conn.request("GET", request, payload)
    res = conn.getresponse()
    data = res.read()
    json_response = simplejson.loads(data)
    youtube_id = json_response['results'][0]['key']
    return "www.youtube.com/watch?v="+str(youtube_id)

# setting up the connection for movie details


# this line can be edited to get desired movie list
responses = tmdb.Discover().movie(year="2017",page="1")
results = responses['results']

movies =[] #declaring movies list to pass to fresh_tomatoes.py
#you can change the num of movies displayed by chaging the movie_count value
for movie_count in range(20):
    movie_details= results[movie_count]
    #getting stuff ready for calling fresh_tomatoes
    temp_url="https://image.tmdb.org/t/p/w370_and_h556_bestv2/"
    poster=temp_url+movie_details['poster_path']
    movie_id=movie_details['id']
    youtube_url = get_youtube_url(movie_id)
    summary = movie_details['overview']
    title= movie_details['title']
    movies.append(movieClass.Movies(title,summary,poster,youtube_url))



#calling fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
