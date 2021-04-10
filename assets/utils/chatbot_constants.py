nltk_intents = [
           {"tag":"greeting",
            "patterns": ["hi", "hello", "good morning", "good evening"],
            "responses":["Hello, how are you ?", "Hi my friend, How can I help you ?"]},
           
           {"tag":"mood",
            "patterns":["I'm fine thank you", "I am fine", "I'm fine", "i am great", "I'm great"],
            "responses":["Oh Great, how can I help you ?", "Awesome!, I am at your service", "Cool, would you like some pizzas ?"]},
           
           {"tag":"goodbye",
            "patterns": ["Bye bye", "bye", "see you", "see ya later", "see you later"],
            "responses":["Good Bye", "See you later", "Take care and see you soon"]},
           
           {"tag": "options",
            "patterns": ["What pizzas do you propose ?", "Can I have the pizzas menu ?", "Menu ?", "What kind of pizzas do you have ?"],
            "responses": ["We have tuna, salmun, pepperoni, veggy and margarita pizzas"]},
           
           {"tag": "promotions",
            "patterns": ["Do you propose any promotion ?", "What kind of promotion do you have", "Are there any discount ?"],
            "responses": ["The second pizza is discounted by half price !"]},
           
           {"tag":"ordering",
            "patterns": ["I'd like to order a pizza", "I would like to order a pizza", "I would love a pizza", "one pizza please"],
            "responses":["Which pizza would you like we have tuna, salmun, pepperoni, veggy and margarita pizzas", "Nice call, which one do you like ?"]},
           
           {"tag":"thanking",
            "patterns":["Thank you", "thanks", "Awesome thanks", "thanks pal", "thanks mate"],
            "responses":["You're welcome", "No problem, enjoy!"]},
           
           {"tag":"no answer",
            "patterns": [""],
            "responses":["Sorry, I don't understand what you're saying"]}
]
nltk_regex_pairs = [
         ["my name is (.*)", ["Hi %1", "How are you doing %1 ?"]],
         ["^(?=.*pizza)(?!.*(veggy|pepperoni|margarita|tuna|salmun|don't|do not)).*", ["Nice call, which one do you like? We have tuna, salmun, pepperoni, veggy and margarita pizzas ?"]],
         ["(.*)(a|an|[1-9]?) (veggy|pepperoni|margarita|tuna|salmun)( pizza| pizzas)", ["%2 %3 %4 will be ready in 15 mins just for you :)  How do you set the order, by card or cash?"]],
         ["(?=.*card)(?!.*(don't|do not)).*", ["Ok for credit card ! Thank you "]],
         ["(.*) (cash)(.*)", ["Perfect, don't forget your wallet ;) "]]
]

def create_pairs_from_intents(intents:list) -> list:
  pairs=[]
  for intent in intents:
    for pattern in intent["patterns"]:
      pairs.append([pattern, intent["responses"]])
  return pairs
