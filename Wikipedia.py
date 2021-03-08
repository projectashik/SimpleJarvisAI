import wikipedia


class Wikipedia:
    data = ""

    def __init__(self, query):
        query = query.replace('wikipedia', '')
        try:
            results = wikipedia.summary(query, sentences=2)
            self.data = "According to wikipedia" + results
        except:
            self.data = "4O4 not found."
