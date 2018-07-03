from firebase import firebase

firebase = firebase.FirebaseApplication('link to your firebase database')



# writing to firebase
def writeToFirebase(key, value):
    user_input = {key: value}
    send_input = firebase.post('user', user_input)
    print(send_input)


# read from firebase
def readFromFirebase():
    recieve_data = firebase.get('user', None)
    print("Database : ", recieve_data)


writeToFirebase("tom", 1212121)
readFromFirebase()
