class Comment():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, content, created_on, post_id, author_id):
        self.id = id
        self.content = content
        self.created_on = created_on
        self.post_id = post_id
        self.author_id = author_id