from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._save_to_db()

    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)',
                       (self._name, self._category))
       
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
        self._update_db('name', value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
        self._update_db('category', value)
    def __repr__(self):
        return f'<Magazine {self.name}>'
