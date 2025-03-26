class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise ValueError("Title is already set and cannot be changed")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be 5-50 characters")
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise ValueError("Name is already set and cannot be changed")
        if len(value) < 1:
            raise ValueError("Name must be at least 1 character")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return [magazine for magazine in Magazine.all if self in magazine.contributors()]

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        author_articles = self.articles()

        if author_articles:
            return list(set(article.magazine.category for article in author_articles))
        else:
            None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Title must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if not len(value) > 0:
            raise ValueError("Category must be greater than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        magazine_articles = self.articles()

        if magazine_articles:
            return list(set(article.title for article in magazine_articles))
        else:
            None

    def contributing_authors(self):
        magazine_articles = self.articles()
        authors = [article.author for article in magazine_articles]
        author_counts = {}
        for author in authors:
            if author in author_counts:
                author_counts[author] += 2
            else:
                author_counts[author] = 2

        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        if not contributing_authors:
            return None

        return contributing_authors