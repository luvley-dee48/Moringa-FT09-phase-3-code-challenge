from database.connection import get_db_connection
from database.setup import create_tables


class Article:
    def __init__(self, title, content, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.content = content  
        self.author_id = author_id
        self.magazine_id = magazine_id
    
    @classmethod
    def create_table(cls):
        create_tables()

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS articles')
        conn.commit()
        conn.close()
    
    def save(self):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',  
                (self.title, self.content, self.author_id, self.magazine_id)  
            )
            self._id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def create(cls, title, content, author, magazine):
        article = cls(title, content, author.id, magazine.id)
        article.save()
        return article

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def author(self):
        return self._get_author()

    @property
    def magazine(self):
        return self._get_magazine()

    def _get_author(self):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT authors.name FROM articles '
                'JOIN authors ON articles.author_id = authors.id '
                'WHERE articles.id = ?',
                (self._id,)
            )
            author_name = cursor.fetchone()
            if author_name:
                return author_name[0]
            else:
                raise ValueError("Author not found for the article")
        finally:
            conn.close()

    def _get_magazine(self):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT magazines.name FROM articles '
                'JOIN magazines ON articles.magazine_id = magazines.id '
                'WHERE articles.id = ?',
                (self._id,)
            )
            magazine_name = cursor.fetchone()
            if magazine_name:
                return magazine_name[0]
            else:
                raise ValueError("Magazine not found for the article")
        finally:
            conn.close()

    def __repr__(self):
        return f'<Article {self.title}>'
