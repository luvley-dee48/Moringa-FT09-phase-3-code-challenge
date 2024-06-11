# from models.author import Author
from models.article import Article
from models.magazine import Magazine
from models.author import Author

Author.drop_table()
Magazine.drop_table()
Article.drop_table()

Author.create_table()
Magazine.create_table()
Article.create_table()

# Author.drop_table()
# Author.create_table()

# Magazine.drop_table()
# Magazine.create_table()


# Article.drop_table()
# Article.create_table()

author1=Author.create("Joana Neema")
magazine1=Magazine.create("Matembezi travellers","Travelling")
article1 = Article.create("Matembezi travellers club", "Day travel plan on a budget", author1, magazine1)

print("Author id:",author1.id)
print("Author name",author1.name)