import os
import nltk
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse.corenlp import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser

STANFORD = "stanford-corenlp-full-2018-10-05"

jars = (
   os.path.join(STANFORD, "stanford-corenlp-3.9.2.jar"),
   os.path.join(STANFORD, "stanford-corenlp-3.9.2-models.jar"),    
)

text = "turn right and go up the stairs and stand at the top."
#text = "Walk out of the closet and into the hallway. Walk through the hallway entrance on the left. Stop just inside the entryway."
#text = "Turn, putting the exit of the building on your left. Walk to the end of the entrance way and turn left. Travel across the kitchen area with the counter and chairs on your right. Continue straight until you reach the dining room. Enter the room and stop and wait one meter from the closest end of the long dining table."
with CoreNLPServer(*jars):

    parser = CoreNLPParser()
    for i in parser.parse_text(text):
        print(i)

    parser = CoreNLPDependencyParser()
    for i in parser.raw_parse(text):
        print(i)
