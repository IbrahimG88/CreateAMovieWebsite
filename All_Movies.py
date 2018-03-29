
import Mother_class

import fresh_tomatoes

"""This file uses fresh_tomatoes and Mother_class file through the function import"""

the_dark_knight = Mother_class.Movie("The Dark Knight", "Metascore: 82", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, \
                                        the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                                        "Stars: Christian Bale, Heath Ledger, Aaron Eckhart", "2h 32min", "release year: 2008",
                                        "http://www.batman-online.com/images/12327109537096.jpg",
                                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")


the_dark_knight_rises = Mother_class.Movie("The Dark Knight Rises", "Metascore: 78", "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, \
                                            is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
                                           "Stars:  Christian Bale, Tom Hardy, Anne Hathaway", "2h 44min", "release year: 2012",
                                           "http://www.android-hilfe.de/attachments/01-jpg.98655/",
                                           "https://www.youtube.com/watch?v=g8evyE9TuYk")







"""movies list conatains the movies in the movie website as list parameters, the movies list is executed in the open_movies_page procedure,
which is located in the fresh_tomatoes procedure."""



movies= [the_dark_knight, the_dark_knight_rises]
fresh_tomatoes.open_movies_page(movies)
