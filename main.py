import serial

ser = serial.Serial("COM6", 9600)
while True:


        import cv2
        from cvzone.HandTrackingModule import HandDetector
        import time
        import speech_recognition as sr
        import datetime
        import pyttsx3


        time.sleep(6)
        intro = "                                         Hello and welcome to the AI Phone Assistant. My name is APA, and I'm here to help you make phone calls and answer questions. To use the assistant, simply raise a certain number of fingers to select an option.If you raise one finger, I'll call your favorite number. If you raise two fingers, I'll ask you for a number to call. If you raise three fingers, I'll call the last number you dialed. If you raise four fingers, I'll tell you the current time. And if you raise five fingers, I'll tell you your account balance."



        balance = 100
        lstnum = 0
        favourite_num = "01008798070"



        # create a text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)  # speech rate in words per minute
        engine.setProperty('volume', 1)  # volume level between 0 and 1
        checkapa = True

        def print_left_balance(balance, amount):
            left_balance = balance - amount
            print("Left balance: ${:.2f}".format(left_balance))
        def convert_to_number(string):
            # Define a dictionary to map words to numbers
            word_to_num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
            # Replace words with their corresponding numbers
            for word, num in word_to_num.items():
                string = string.replace(word, num)
            # Remove spaces between characters
            new_string = ''.join(c for c in string if c != ' ')
            # Limit the length of the resulting string to 12 characters
            new_string = ''.join(c for c in new_string if c.isdigit())
            # Include only numeric characters in the output
            return new_string[:12]




        def recognize_speech():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak Anything :")

                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    # print(format(text))
                    return text
                except:
                    print("Sorry could not recognize what you said")

        detector = HandDetector(maxHands=1, detectionCon=0.8)
        video = cv2.VideoCapture(0)




        while checkapa :
                textint = recognize_speech()
                if textint.lower() == "apa" or textint.lower() == "a p a" or textint.lower() == "a pa" or textint.lower() == "ap a" or textint.lower() == "aba" or textint.lower() == "a b a" or textint.lower() == "a ba":
                    checkapa = False
                    engine.say("are you want skip introduction to save your time")
                    engine.runAndWait()
                    textintch = recognize_speech()
                    if textintch == "yes":
                        print("skip")
                        txt = "6"
                        ser.write(txt.encode())
                    else:
                        txt = "6"
                        ser.write(txt.encode())
                        engine.say(intro)
                        engine.runAndWait()









        while True:
            _, img = video.read()
            img = cv2.flip(img, 1)
            hand = detector.findHands(img, draw=False)
            if hand:
                lmlist = hand[0]
                if lmlist:
                    fingerup = detector.fingersUp(lmlist)
                    if fingerup == [0, 0, 0, 0, 0]:
                        lstnum =0
                        balance = 100
                        txt = "0"
                        ser.write(txt.encode())
                        engine.say("power off")
                        engine.runAndWait()
                        print("power off")
                        print("0")

                        checkapa = True
                        video.release()
                        cv2.destroyAllWindows()
                        break
                    if fingerup == [0, 1, 0, 0, 0]:
                        # speak the input string aloud

                        engine.say("your favourite number is "+favourite_num)
                        engine.runAndWait()
                        engine.say( "number is " + favourite_num + " are you sure to calling this number if yes tell yes else tell no")
                        engine.runAndWait()
                        textanswer = recognize_speech()
                        if textanswer == "yes":
                            txt = "1" + str(favourite_num)
                            ser.write(txt.encode())
                            engine.say("rining")
                            engine.runAndWait()
                            time.sleep(16)
                        else:
                            engine.say("you can choose 2 again and tell your number")
                            engine.runAndWait()



                        print(favourite_num)
                    if fingerup == [0, 1, 1, 0, 0]:
                        engine.say("you can input the number")
                        engine.runAndWait()
                        text = recognize_speech()
                        lstnum = text

                        # speak the input string aloud
                        engine.say("number is " + text + " are you sure to calling this number if yes tell yes else tell no")
                        engine.runAndWait()
                        textanswer = recognize_speech()
                        if textanswer == "yes":
                            txt = "2" + str(convert_to_number(text))
                            ser.write(txt.encode())
                            engine.say("rining")
                            engine.runAndWait()
                            time.sleep(16)
                        else:
                            engine.say("you can choose 2 again and tell your number")
                            engine.runAndWait()
                        print(convert_to_number(text))
                    if fingerup == [0, 1, 1, 1, 0]:

                        if lstnum !=0 :
                            # speak the input string aloud
                            engine.say("number is " + convert_to_number(lstnum) + " are you sure to calling this number if yes tell yes else tell no")
                            engine.runAndWait()
                            textanswerlast = recognize_speech()
                            if textanswerlast == "yes":
                                txt = "3" + str(convert_to_number(lstnum))
                                ser.write(txt.encode())
                                engine.say("rining")
                                engine.runAndWait()
                                time.sleep(16)
                                print(convert_to_number(lstnum))
                            else:
                                engine.say("you can choose 2 again and tell your number")
                                engine.runAndWait()

                        print("3")
                    if fingerup == [0, 1, 1, 1, 1]:
                        now = datetime.datetime.now()
                        txt = "4" + str("Current time: {:02d}:{:02d}".format(now.hour, now.minute))
                        ser.write(txt.encode())
                        engine.say("Current time: {:02d}:{:02d}".format(now.hour, now.minute))
                        engine.runAndWait()

                        print("Current time: {:02d}:{:02d}".format(now.hour, now.minute))
                        print("4")
                        time.sleep(16)
                    if fingerup == [1, 1, 1, 1, 1]:
                        txt = "5" + str("your left balance is "+ str(balance))
                        ser.write(txt.encode())
                        engine.say("your left balance is "+ str(balance))

                        engine.runAndWait()
                        print_left_balance(balance,0)
                        time.sleep(16)

                        print("5")
                    if fingerup == [1, 0, 0, 0, 0]:
                        print("6")
                    if fingerup == [1, 1, 0, 0, 0]:
                        print("7")
                    if fingerup == [1, 1, 1, 0, 0]:
                        print("8")
                    if fingerup == [1, 1, 1, 1, 0]:
                        print("9")

            cv2.imshow("Video",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.3)

        video.release()
        cv2.destroyAllWindows()