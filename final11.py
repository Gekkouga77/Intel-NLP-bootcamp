import os.path
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import numpy as np 
import random
import requests
import bs4 
import string 
import urllib.request
import warnings
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.feature_extraction.text import TfidfVectorizer 
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')

planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto','Comet','Asteroid','Meteroid']
before = 'https://en.wikipedia.org/wiki/'

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Greeting_Input = ["hello", "hi", "greetings", "sup", "what's up","hey", "hey there"]
Greeting_Responses = ["Hi", "Hello", "Sup","Namaste","Hey","Greetings"]
def greeting(sentence):
    for word in sentence.split(): 
        if word.lower() in Greeting_Input: 
               return random.choice(Greeting_Responses)

def response(user_response):
    robo_response='' 
    sent_tokens.append(user_response) 
    flat_list.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english') 
    tfidf = TfidfVec.fit_transform(flat_list) 
    vals = cosine_similarity(tfidf[-1], tfidf) 
    idx = vals.argsort()[0][-2] 
    flat = vals.flatten() 
    flat.sort() 
    req_tfidf = flat[-2] 
    
    if(req_tfidf == 0):
        robo_response = robo_response + ("I am sorry! I don't understand you" or "Uh...Sorry could you please repeat again..." or "I beg your pardon" )
        return robo_response
    else:
        robo_response = robo_response + flat_list[idx]
        return robo_response


all_sentences = []
for planet in planets:
    if planet == 'Mercury':
        url = before + planet + '_(planet)'
    else:
        url = before + planet
    storing_url = "D:/Desktop/Intel/" + planet + ".txt"
    html_url = "D:/Desktop/Intel/" + planet + "_html.txt"

    if not (os.path.isfile(html_url)):
        urllib.request.urlretrieve(url, storing_url)
        
        file = open(storing_url, "r", encoding="utf8")
        contents = file.read()
        soup = BeautifulSoup(contents, 'html.parser')
        
        f = open(html_url, "w", encoding="utf8")
        
        for data in soup.find_all("p"):
            sum = data.get_text()
            f.writelines(sum)
        f.close()
	
    corpus = open(html_url, 'r', errors = 'ignore')
    raw_data = corpus.read()
    raw_data = raw_data.lower()
    sent_tokens = nltk.sent_tokenize(raw_data)
    all_sentences.append(sent_tokens)
    word_tokens = nltk.word_tokenize(raw_data)

    sent_tokens[:2]
    word_tokens[:5]

    # stop_words = set(stopwords.words('english'))
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]

    # final_sentences = []
    # filtered_sentence = []
    # for w in word_tokens: 
    #     if w not in stop_words: 
    #         filtered_sentence.append(w)
    # 	final_sentences.append(' '.join(filtered_sentence))
    
    lemmer = nltk.stem.WordNetLemmatizer() 

flat_list = [item for sublist in all_sentences for item in sublist]

def chat(user_response):
    Name = 'Master678'
    robo_greeting = ("My name is " + Name + ". I will answer your queries about the solar system. If you want to leave, type Bye ")

    # flag = True
    # print( Name + ": My name is " + Name + ". I will answer your queries about the 9 planets. If you want to leave, type Bye ")
    # while(flag == True):
    #     #user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you' ):
            flag = False
            print(Name + ": You are welcome..")
            return "You are welcome.."
        else:
            if(greeting(user_response)!=None):
                print(Name + ": " + greeting(user_response))
                return greeting(user_response) + "   " +robo_greeting
            else:
                print(Name + ": " ,end ="")
                print(response(user_response))
                #sent_tokens.remove(user_response)
                flat_list.remove(user_response)
                return response(user_response)
    else:
        flag=False
        #print(Name + ": Bye  ")
        return "Bye"