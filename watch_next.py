#Compulsory Task 2

import spacy
nlp = spacy.load('en_core_web_md')

def watch_next(description):
#open movies.txt in read mode
    
    movies = open("movies.txt", "r")
#initialise movies_list
    movies_list = []

#split into title and description and store in list
    for i in movies:
        movies_list.append(i.split(':'))
    
#count number of movies in file
    count = len(movies_list)

#create list to store similarity
    similarity_list = []

    model_sentence = nlp(description)

#iterate through text file
#check similarity between the movie description and Planet Hulk description

    for i in range(0, count):
#I had help from a friend for this line        
        similarity_list.append(nlp(movies_list[i][1]).similarity(model_sentence))

#get the maximum similarity value and index
    max_sim = max(similarity_list)
    max_sim_index = similarity_list.index(max_sim)

#return the most similar movie
    return movies_list[max_sim_index][0]

#Planet Hulk description for comparison
planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar, where he is sold into slavery and trained as a gladiator."""


#call watch_next function
print("The next movie you should watch is: " + watch_next(planet_hulk))


