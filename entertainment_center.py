import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toy that come to"
                        " life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # N0QA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # N0QA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
the_prestige = media.Movie("The Prestige", "Two stage magicians engage in"
                           "competitive one-upmanship in an attempt to create"
                           " the ultimate stage illusion.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",  # N0QA
                           "https://www.youtube.com/watch?v=9n2B5WW4SKk")
law_abiding_citizen = media.Movie("Law Abiding Citizen", "A frustrated man"
                                  " decides to take justice into his own hands"
                                  " after a plea bargain sets one of his"
                                  " family's killers free. He targets not only"
                                  " the killer but also the district attorney"
                                  " and others involved in the deal",
                                  "https://upload.wikimedia.org/wikipedia/en/9/95/Law_abiding_citizen_ver5.jpg",  # N0QA
                                  "https://www.youtube.com/watch?v=p6hT_uY-jSM")
inside_man = media.Movie("Inside Man", "A police detective, a bank robber, and a"
                         "high-power broker enter high-stakes negotiations"
                         " after the criminal's brilliant heist spirals into a"
                         " hostage situation.",
                         "https://upload.wikimedia.org/wikipedia/en/a/a2/Inside_Man_%28film_poster%29.jpg",  # N0QA
                         "https://www.youtube.com/watch?v=44v8NhVEL5A")
les_miserables = media.Movie("Les Miserables", "In 19th-century France, Jean"
                             " Valjean, who for decades has been hunted by the"
                             " ruthless policeman Javert after breaking parole,"
                             " agrees to care for a factory worker's daughter."
                             " The decision changes their lives for ever.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b0/Les-miserables-movie-poster1.jpg",  # N0QA
                             "https://www.youtube.com/watch?v=YmvHzCLP6ug")
movies = [toy_story, avatar, the_prestige, law_abiding_citizen, inside_man,
          les_miserables]
fresh_tomatoes.open_movies_page(movies)
