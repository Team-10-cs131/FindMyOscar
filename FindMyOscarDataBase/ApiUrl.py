class ApiUrl:
    def __init__(self, apikey, query):
        self.address = 'http://www.omdbapi.com/?apikey=' + apikey + '&t=' + query
