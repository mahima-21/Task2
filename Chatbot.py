import random
greetings=['hola','Hola','Hello!','hello','Hey','hey','hi','Hi','Hello','HELLO']

question1=['How are you?','how are you?','how you doing?','How are you doing?','Whats Up','whats up','How are you going?']
question2=['What is your name?','what is your name?','WHAT IS YOUR NAME?','Your good name please!',"And You?",'What should i call you?','what should i call you']
question3=['goodbye','Goodbye','I am leaving','Bye','See you later','see you later','bye']
question4=['What you do?','what you do?','What is your profession?','what is your profession']
question5=['What are you doing?','what are you doing?']
question6=['Do you believe in love?','Do you believe in god?','do you believe in love?','Do you love me?','do you love me?',]
question7=['Good Morning','good morning']
question8=['Good Night','good night']
question9=['good afternoon','Good Afternoon']
question10=['You are cute','You are beautiful','You are handsome','You are smart']
question11=['Are you Human?','Are you human?','Do you have a hobby?','Does god exist?','Does Santa exist?','Will you marry me?','Will You Marry Me?']
while True:
    userInput=input("User: ")
    if userInput in greetings:
        bot=['Hello!','hi','hey','hello','Hello','Hi','Hey','HELLO']
        print('Bot: ',random.choice(bot))
    elif userInput in question1:
        bot=['I am fine','Okay','okay','I am Good']
        print('Bot: ',random.choice(bot))
    elif userInput in question2:
        bot = ['My name is Zimmy','Zimmy here!','I am Zimmy','Zimmy','I am Zimmy.How can i help you?']
        print('Bot: ', random.choice(bot))
    elif userInput in question3:
        bot=['bye','Bye','Have a Good day','Have a nice day','Okay Bye','Okay talk to you later']
        print('Bot: ',random.choice(bot))
    elif userInput in question4:
        bot=['I am a bot','I am a Bot']
        print('Bot: ',random.choice(bot))
    elif userInput in question5:
        bot = ['Talking to You','Chatting','Replying you!']
        print('Bot: ', random.choice(bot))
    elif userInput in question6:
        bot = ["No i don't find it interesting"]
        print('Bot: ', random.choice(bot))
    elif userInput in question7:
        bot = ['Good Morning','good morning']
        print('Bot: ', random.choice(bot))
    elif userInput in question8:
        bot = ['Good Night','good night']
        print('Bot: ', random.choice(bot))
    elif userInput in question9:
        bot = ['good afternoon','Good Afternoon']
        print('Bot: ', random.choice(bot))
    elif userInput in question10:
        bot = ['Thank You']
        print('Bot: ', random.choice(bot))
    elif userInput in question10:
        bot = ['No','no','Try asking something else']
        print('Bot: ', random.choice(bot))





    else:
        print("I do not understand what you said")
