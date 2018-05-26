import requests


alphabets = 'esiarngtomlcdupmhbyfvwzxqj' #etaoinsuhrdlugfcmfwypvbgkqjxz'   #'esiarntolcdupmghbyfvwzxqj'

def checkSame(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i] and str2[i] != '_':
            return False
    for i in range(len(str1)):
        if str1[i] != str2[i] and str1[i] in guessed:
            return False
    return True

    


URL = "http://upe.42069.fun/KzJBV"
URLRESET = "http://upe.42069.fun/KzJBV/reset"
path = 'words.txt'
f = open(path, 'r')
words = []


postData = {'email': "harshupatwari@gmail.com"}
p = requests.post(url=URLRESET, data = postData)
responseData = p.json()
print(responseData)

lists = f.readlines()
for i in range (len(lists)):
    words.append(lists[i].rstrip('\n'))

iterCount = 0

#print(words)
while(True):
    status = ""
    guessed = 'e'
    guessList = []
    r = requests.get(url=URL)

    data = r.json()

    state = data['state']
    status = data['status']
    remaining_guesses = data['remaining_guesses']

    print("State: %s\n"%(state))


    postData = {'guess': 'e'}
    p = requests.post(url=URL, data = postData)

    responseData = p.json()

    state = responseData['state']
    status = responseData['status']
    remaining_guesses = responseData['remaining_guesses']
    win_rate = responseData['win_rate']
    print(state)
    print(remaining_guesses)

    count = 1


    while (status != "FREE" and remaining_guesses != 1):
        postData = {'guess': alphabets[count]}
        guessed += alphabets[count]
        count += 1
        print(guessed)
        p = requests.post(url=URL, data = postData)
        responseData = p.json()

        state = responseData['state']
        status = responseData['status']
        remaining_guesses = responseData['remaining_guesses']
        win_rate = responseData['win_rate']

        print(state)
        print(remaining_guesses)
        print(win_rate)

    statewords = state.split()
    stateWords = []
    for word in statewords:
        word = word.replace(',', '')
        word = word.replace('(', '')
        word = word.replace(')', '')
        stateWords.append(word)

    if (remaining_guesses == 1 and status != "FREE"):
        for i in range(len(stateWords)): #for stateword in stateWords:
            if stateWords[i].isalpha() == False:
                for guessword in words:
                    if len(guessword) == len(stateWords[i]) and checkSame(guessword, stateWords[i]):
                        for ch in guessword:
                            if(status != "DEAD" and status != "FREE"):
                                print(guessword)
                                if(ch == '\''):
                                    continue
                                postData = {'guess': ch}
                                p = requests.post(url=URL, data = postData)
                                responseData = p.json()
                                state = responseData['state']
                                statewords = state.split()
                                stateWords = []
                                for word in statewords:
                                    word = word.replace(',', '')
                                    word = word.replace('(', '')
                                    word = word.replace(')', '')
                                    stateWords.append(word)
                                status = responseData['status']
                                remaining_guesses = responseData['remaining_guesses']
                                win_rate = responseData['win_rate']
                                print(state)
                                print(remaining_guesses)
                                print(win_rate)
                                print(status)
                        #guessList.append(guessword)
                        break

   # for guessword in guessList:
    #    for ch in guessword:
     #       if(status != "DEAD" and status != "FREE"):
      #          print(guessword)
       #         if(ch == '\''):
        #            continue
         #       postData = {'guess': ch}
          #      p = requests.post(url=URL, data = postData)
           #     responseData = p.json()
            #    state = responseData['state']
             #   status = responseData['status']
              #  remaining_guesses = responseData['remaining_guesses']
               # win_rate = responseData['win_rate']
                #print(state)
                #print(remaining_guesses)
                #print(win_rate)
                #print(status)
    
    while (status != "FREE" and status != "DEAD"):
        postData = {'guess': alphabets[count]}
        guessed += alphabets[count]
        count += 1
        p = requests.post(url=URL, data = postData)
        responseData = p.json()
        state = responseData['state']
        status = responseData['status']
        remaining_guesses = responseData['remaining_guesses']
        win_rate = responseData['win_rate']
        print(state)
        print(remaining_guesses)
        print(win_rate)

    print("Iter Count:")
    print(iterCount)
    iterCount += 1



    

                