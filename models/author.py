from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        self._id = None 
        self.name = name  

    def _create_author_in_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Cannot change the author's name after it is set")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def fetch_from_db(self, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author_data = cursor.fetchone()
        conn.close()
        if author_data:
            self._id = author_data[0]
            self._name = author_data[1]
        else:
            raise ValueError("Author with given ID does not exist in the database")

    def __repr__(self):
        return f'<Author {self.name}>'
