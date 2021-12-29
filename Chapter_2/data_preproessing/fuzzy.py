from fuzzywuzzy import fuzz
# research interests of a pair of authors
author1_research = "applied machine learning, computational sustainability, " \
                   "artificial intelligence"
author2_research = "artificial intelligence, computational epidemiology, " \
                    "recommender systems, applied machine learning, " \
                    "visual analytics"
# fuzzy compare the pair of research interests
ratio = fuzz.ratio(author1_research, author2_research)
# prints 45
print(ratio)