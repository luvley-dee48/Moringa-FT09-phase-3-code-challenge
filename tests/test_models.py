import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Author.drop_table()
        Magazine.drop_table()
        Article.drop_table()
        Author.create_table()
        Magazine.create_table()
        Article.create_table()
    
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    
    
    def test_article_creation(self):
        article = Article("Test Title", "Test Content", 1, 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_drop_table(self):
        Author.drop_table()
        with self.assertRaises(Exception):
            Author.create("Test Author")
    
    def test_article_save(self):
        article = Article("Test Article", "Test Content", 1, 1, 1)
        article.save()
        self.assertIsNotNone(article.id)
   
    def test_magazine_deletion(self):
      magazine = Magazine("Tech Weekly", "Technology")
      magazine.delete()
      self.assertIsNone(magazine.id)

if __name__ == "__main__":
    unittest.main()
