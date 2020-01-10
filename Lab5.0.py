import hashlib

def main():
    ##Opening files
    wordsFile = 'wordslist.txt'
    userInfoFile = 'passwrd.txt'
    words = open(wordsFile, 'r').read().split('\n')
    userInfo = open(userInfoFile, 'r').read().split('\n')

    ##Initiating arrays
    wordList = []
    compare = []

    ##User info arrays
    username = []
    userId = []
    passwords = []

    ##Splitting and storing user info
    for data in userInfo:
        fileSplit = data.split(",")
        username.append(fileSplit[0])
        userId.append(fileSplit[1])
        passwords.append(fileSplit[2])

    ##Putting the hashed words into array
    for word in words:
        wordList.append(word)
        h = hashlib.sha1(word.encode()).hexdigest()
        compare.append(h)

    ##Comparing the two arrays and printing matches
    for match in passwords:
        if match in compare:
            passwordMatch = compare.index(match)
            print("Username:", username[passwords.index(match)],"\n"+
                  "Password:", wordList[passwordMatch], "\n")
            
      
    
main()
