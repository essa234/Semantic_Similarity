import spacy
nlp = spacy.load('en_core_web_md')

#test description to match with
planet_hulk = nlp('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator
''')

def watch_next(description):
    #list of descriptions, movies and the similarity score given
    description_list = []
    movie_list = []
    similarity_scores = []

    #open data file and read information initiating the lists
    with open("movies.txt", 'r') as movies:
        file = movies.readlines()
        for line in file:
            data = line.split(':')
            #add movie and description in line to list
            movie_list.append(data[0])
            description_list.append(data[1])

    #rank each description similarity to given description and store score given
    for desc in description_list:
        similarity_scores.append(description.similarity(nlp(desc)))
    #highest score is the best match
    best_match = similarity_scores.index(max(similarity_scores))
    #return associated movie with description with highest score
    print(f"The best movie matching based on what you watched is: {movie_list[best_match]}")

#call function
watch_next(planet_hulk)