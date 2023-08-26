class NewsArticle(dict):

    def __init__(self, *k, **kwargs):
        """ Object Constructor """

        self.__dict__ = self
        super().__init__(*k, **kwargs)
