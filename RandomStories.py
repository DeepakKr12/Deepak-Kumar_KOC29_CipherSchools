import random
print("Hello Reader")
readername=input("What is your name?:")
print("Hello"+" "+readername)

adjective_t=["LAZY","CARELESS","LETHARGIC","INATTENTIVE"]
who_t=["BOY","YOUNG MAN","CHILD","KID"]
print("TITLE OF THE STORY:-  "+random.choice(adjective_t)+" "+random.choice(who_t))

# Defining list of phrases which will help to build a story

Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Sam.',
			' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by ',' he was going for a picnic to ']
place = [' the mountains ', ' the garden ', 'the forest ']
second_character = ['he saw a old man', 'he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' singing a song on the roadside', ' searching something.', ' digging a well on roadside.']

print(random.choice(Sentence_starter)+random.choice(character),
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))
