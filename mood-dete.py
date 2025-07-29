from textblob import TextBlob

print("Welcome to AI mood detector")
name = input("Enter your name")
print(f"Welcome to AI Mood detector {name}")
print("\n Type exit to quit")

while True:
    sentence = input("Enter you sentence")
    if sentence.lower() == "quit":
        print("Good Bye !!")
        break
    
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        print("Positive Sentiment")
    elif sentiment < 0:
        print("Negative Sentiment")
    else:
        print("Neutral statement")
        
    

    