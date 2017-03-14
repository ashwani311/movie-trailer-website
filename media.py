class Movie():
    """
        The base movie class.
    """

    def __init__(self, title, poster, youtube_trailer):
        """
            Constructor Initializes all the Data Members of Class
        """
        image_base_url = "https://image.tmdb.org/t/p/w780"
        youtube_base_url = "https://www.youtube.com/watch?v="
        self.title = title
        self.poster_image_url = image_base_url + poster
        self.trailer_youtube_url = youtube_base_url + youtube_trailer
