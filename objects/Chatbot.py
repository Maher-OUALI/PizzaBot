from assets.utils.chatbot_constants import *
from nltk.chat.util import Chat, reflections

class Chatbot():
    def __init__(self, lang="en"):
        self.lang=lang
        self._pairs=nltk_regex_pairs.copy()
        self._pairs.extend(create_pairs_from_intents(nltk_intents))
        self.isFitted=False
        self.nltk_bot=None

    def train(self):
        self.nltk_bot=Chat(self._pairs, reflections)
        self.isFitted=True

    def answer(self, text):
        if(not(self.isFitted)):
            self.train()
        if(self.nltk_bot.respond(text) != None):
            return self.nltk_bot.respond(text)
        return "I'm sorry, I didn't understand you"
    
