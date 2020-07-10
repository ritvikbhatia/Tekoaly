import json
with open('C:\\Users\\Ritvik\\Desktop\\Tekoaly\\json file\\chatbot.json') as json_file:
    data = json.load(json_file)
y=data['intents']

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def chat():
    print(y[0]['Question'])
    print((y[1]['Question']))
    inp = input("You: ")
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    print(random.choice(responses))
    print((y[2]['Question']))
    age = input("You: ")

    print((y[3]['Question']))
    height = input("You: ")

    print((y[4]['Question']))
    weight = input("You: ")

    print((y[5]['Question']))
    famhist = input("You: ")

    if(famhist=='Yes'):
        print((y[6]['Question']))
        fambs = input("You: ")

        print((y[7]['Question']))
        fambp = input("You: ")

    print((y[8]['Question']))
    Hygine = input("You: ")

    print((y[9]['Question']))
    smoke = input("You: ")

    print((y[10]['Question']))
    alcohol = input("You: ")

    print((y[11]['Question']))
    fruits = input("You: ")

    print((y[12]['Question']))
    bp = input("You: ")

    print((y[13]['Question']))
    cholestrol = input("You: ")

    print((y[14]['Question']))
    fbs = input("You: ")

    print((y[715]['Question']))
    med = input("You: ")
    if(med=='yes'):
        print((y[16]['Question']))
        medicines = input("You: ")
    print("thank you for sharing the information! ")
    print("What can we help you with ?")
    while True:
        inp=input("you: ")
        if(inp=="bye"):
            break
        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))


chat()
