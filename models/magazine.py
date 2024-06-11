from database.connection import get_db_connection
from database.setup import create_tables

class Magazine:
    def __init__(self, name, category,id=None):
        self._id = id
        self._name = name
        self._category = category
        # self._save_to_db()

    @classmethod
    def create_table(cls):
        create_tables()
    
    
    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS magazines')
        conn.commit()
        conn.close()

    def _save_to_db(self):
        if not self._id:  
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)',
                           (self._name, self._category))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()


     
    @classmethod
    def create(cls, name, category):
      
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE name = ? AND category = ?', (name, category))
        existing_magazine = cursor.fetchone()
        if existing_magazine:
    
            return cls(existing_magazine[1], existing_magazine[2], existing_magazine[0])
        else:
            
            return cls(name, category)


    def delete(self):
        if self._id:  
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM magazines WHERE id = ?', (self._id,))
            conn.commit()
            conn.close()
            self._id = None  

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



    def _update_db(self, field, value):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f'UPDATE magazines SET {field} = ? WHERE id = ?', (value, self._id))
        conn.commit()
        conn.close()

          
    def __repr__(self):
        return f'<Magazine {self.name}>'
