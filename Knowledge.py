from logic import *


# from logic import Symbol, And, Or, Not, Implication, model_check

rain = Symbol("rain")                 # It is raining.
hagrid = Symbol("hagrid")             # Harry visited Hagrid.
dumbledore = Symbol("dumbledore")     # Harry visited Dumbledore.

sampleSentence = Implication(rain, hagrid)
print(sampleSentence.formula())       # Here, we can nicely see mathematical formula of "sampleSentence"

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())
# model_check takes two inputs, knowledge and query, and assuming knowledge is true checks if the query is true or not
print(model_check(knowledge, rain))