import webbrowser
import uuid

class Movie () :
    """ This class provides a way to store movie related information """
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        """ Initialies a new Movie Instance.
            
            Args:
                self: The object your are using this function on.
                movie_title: The title of the movie you'ld like to add.
                movie_storyline: A short summary of the movie's plot.
                poster_img_url: Url of the movie's poster image.
                trailer_youtube_url: Url of the movie's trailer on youtube.
                id: A unique id for every movie
            
            Returns:
                A new movie Instance with all the provided args.
            
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        # There is no current use for adding an Id.
        self.id = uuid.uuid4()
    
    def show_trailer(self):
        """ Plays the movie's trailer """
        # Using the webbrowser.open function provided by the webbrowser
        # library.
        webbrowser.open(self.trailer_youtube_url)
