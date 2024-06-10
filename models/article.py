class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
   
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError("Title must be a string")
        if not 5 <= len(new_title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters long")
        self._title = new_title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def save_to_database(self):
        # Implement your database logic here
        # For example:
        # author_id = self._author.id
        # magazine_id = self._magazine.id
        # Execute SQL queries to save the article to the database
        pass

    def __repr__(self):
        return f'<Article {self.title}>'
