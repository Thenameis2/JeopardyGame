import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from PIL import ImageTk,Image # impprting so i can add pictures
#creating GUI window 
root = Tk() #window
root.geometry(
'752x546'
) # size of the GUI window 
root.title("Jeopardy") # title for GUI 

c = Canvas(root, bd = 5, bg = "blue", height = 950, width = 950)
c.pack()

# image = ImageTk.PhotoImage(Image.open("Paris.jpeg"))

#class score():


#def callback():
  #  global buttonClicked
  #  buttonClicked = not buttonClicked 
#topic one 
def catagory1(): 
    mes = "The catagory is Movies"
    showinfo(title = "Movie Catagories",message = mes) 

full_score = []
def question1():
    mes = askstring('200', 'Who played Iron Man in Iron Man 1, coreect spelling of nouns')
    answer = "Tony"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2():
    mes = askstring('400', 'How many stars Wars movies are there ')
    answer = "12"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3():
    mes = askstring('600', 'In The Matrix, does Neo take the Blue pill or the Red pill?')
    answer = "Red"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4():
    mes = askstring('800', 'Which movie is the most death-packed film ever made with an average of five people dying every minute?')
    answer = "300"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5():
    mes = askstring('1000', 'What power is possessed by Violet in "The Incredibles"?')
    answer = "invisibility"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score

shownScore = []
def scores():
    global total
    total = 0
    for i in full_score:
       total = int(total) + int(i)
       shownScore.append(total)
    showinfo(message= str(total))

     
topic1 = Button(root, text="Movies ", width=10, height=5, bg = "blue", fg="blue",command=catagory1).place(x=0,y=0) #creates and places button on GUI
Question1 = Button(root, text="200 ", width=10, height=5, background = "blue", fg="yellow" ,command=question1).place(x=0,y=92)
Question2 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2).place(x=0,y=184)
Question3 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3).place(x=0,y=276)
Question4 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4).place(x=0,y=368)
Question5 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5).place(x=0,y=452)


#ScoreLabel = Label(root,text= "Your score ", command = scores).place(x = 0, y = 0)


#topic 2
def catagory2(): 
    mes = "The catagory is Places"
    showinfo(title = "Place Catagories",message = mes) 

def question1_part2():
    mes = askstring('200', 'What island boasts Mount Fuji?')
    answer = "Honshu"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2_part2():
    mes = askstring('400', 'What state made the U.S. the fourth largest country in land mass in 1959? ')
    answer = "Alaska"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3_part2():
    mes = askstring('600', 'What island has endured Mount Etnas wrath over 140 times?')
    answer = "Sicily"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4_part2():
    mes = askstring('800', 'Which extends further North- Japan, North Korea or turkey?')
    answer = "Japan"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5_part2():
    mes = askstring('1000', 'What U.S. state is said to have as many cows as people?')
    answer = "Wisconsin"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score
topic2 = Button(root, text="Places ", width=10, height=5, bg = "blue", fg="blue",command=catagory2).place(x=125,y=0)
Question6 = Button(root, text="200 ", width=10, height=5, bg = "blue", fg="yellow",command=question1_part2).place(x=125,y=92)
Question7 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2_part2).place(x=125,y=184)
Question8 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3_part2).place(x=125,y=276)
Question9 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4_part2).place(x=125,y=368)
Question10 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5_part2).place(x=125,y=452)

#topic 3
def catagory3(): 
    mes = "Are you smarter than a 5th grader"
    showinfo(title = "Place Catagories",message = mes) 

def question1_part3():
    mes = askstring('200', 'What is 5+3?')
    answer = "8"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2_part3():
    mes = askstring('400', 'What is the spoken language in Mexico? ')
    answer = "Spanish"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3_part3():
    mes = askstring('600', 'How many countires are in Africa?')
    answer = "54"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4_part3():
    mes = askstring('800', 'Which continent is least populated?')
    answer = "Antarctica"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5_part3():
    mes = askstring('1000', 'Where were french fries invented?')
    answer = "Belgium"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score
topic3 = Button(root, text="Smarter than 5th grader", width=10, height=5, bg = "blue", fg="blue",command=catagory3).place(x=250,y=0)
Question6 = Button(root, text="200 ", width=10, height=5, bg = "blue", fg="yellow",command=question1_part3).place(x=250,y=92)
Question7 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2_part3).place(x=250,y=184)
Question8 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3_part3).place(x=250,y=276)
Question9 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4_part3).place(x=250,y=368)
Question10 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5_part3).place(x=250,y=452)

#topic 4
def catagory4(): 
    mes = "The catagory is Science"
    showinfo(title = "Science Catagories",message = mes) 

def question1_part4():
    mes = askstring('200', 'What is H20 known as?')
    answer = "water"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2_part4():
    mes = askstring('400', 'Electrons,protons,_______? ')
    answer = "Neutrons"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3_part4():
    mes = askstring('600', '4th planet from the sun?')
    answer = "Mars"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4_part4():
    mes = askstring('800', 'Which is faster, light or sound?')
    answer = "light"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5_part4():
    mes = askstring('1000', 'how many days does it take for the earth to orbit the sun?')
    answer = "365"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score
topic4 = Button(root, text="Science ", width=10, height=5, bg = "blue", fg="blue",command=catagory4).place(x=375,y=0)
Question6 = Button(root, text="200 ", width=10, height=5, bg = "blue", fg="yellow",command=question1_part4).place(x=375,y=92)
Question7 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2_part4).place(x=375,y=184)
Question8 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3_part4).place(x=375,y=276)
Question9 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4_part4).place(x=375,y=368)
Question10 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5_part4).place(x=375,y=452)

#topic 5
def catagory5(): 
    mes = "The catagory is Tec"
    showinfo(title = "Tec Catagories",message = mes) 

def question1_part5():
    mes = askstring('200', 'What year was TikTok invented?')
    answer = "2016"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2_part5():
    mes = askstring('400', 'What year was Instagram invented? ')
    answer = "2010"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3_part5():
    mes = askstring('600', 'How many megabytes are in a Gibabyte?')
    answer = "1000"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4_part5():
    mes = askstring('800', 'What year was the internet invented?')
    answer = "1983"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5_part5():
    mes = askstring('1000', 'S.T.E.A.___?')
    answer = "M"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score
topic5 = Button(root, text="Tec ", width=10, height=5, bg = "blue", fg="blue",command=catagory5).place(x=500,y=0)
Question6 = Button(root, text="200 ", width=10, height=5, bg = "blue", fg="yellow",command=question1_part5).place(x=500,y=92)
Question7 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2_part5).place(x=500,y=184)
Question8 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3_part5).place(x=500,y=276)
Question9 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4_part5).place(x=500,y=368)
Question10 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5_part5).place(x=500,y=452)

#topic 6
def catagory6(): 
    mes = "The catagory is Random"
    showinfo(title = "Random Catagories",message = mes) 

def question1_part6():
    mes = askstring('200', 'How many zodiacs are there?')
    answer = "12"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(200)
        showinfo(message ="you got " + str(200) + " points" ) 
        
    else:
        full_score.append(-200)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(200) + " points" )
    return full_score
            
def question2_part6():
    mes = askstring('400', 'What is the plural of sheep? ')
    answer = "sheep"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(400)
        showinfo(message ="you got " + str(400) + " points" ) 
        
    else:
        full_score.append(-400)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(400) + " points" )
    return full_score

def question3_part6():
    mes = askstring('600', 'what is the slowest animal in the world?')
    answer = "sloth"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(600)
        showinfo(message ="you got " + str(600) + " points" ) 
        
    else:
        full_score.append(-600)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(600) + " points" )
    return full_score

def question4_part6():
    mes = askstring('800', 'Bagels originated from which country?')
    answer = "Poland"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(800)
        showinfo(message ="you got " + str(800) + " points" ) 
        
    else:
        full_score.append(-800)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(800) + " points" )
    return full_score

def question5_part6():
    mes = askstring('1000', 'what is the highest grossing movie?')
    answer = "Avatar"
    if mes == answer:
        showinfo(message = "correct") 
        full_score.append(1000)
        showinfo(message ="you got " + str(1000) + " points" ) 
        
    else:
        full_score.append(-1000)
        showinfo(message = "wrong ")
        showinfo(message ="you lost " + str(1000) + " points" )
    return full_score
topic6 = Button(root, text="Random ", width=10, height=5, bg = "blue", fg="blue",command=catagory6).place(x=625,y=0)
Question6 = Button(root, text="200 ", width=10, height=5, bg = "blue", fg="yellow",command=question1_part6).place(x=625,y=92)
Question7 = Button(root, text="400 ", width=10, height=5, bg = "blue", fg="yellow",command=question2_part6).place(x=625,y=184)
Question8 = Button(root, text="600 ", width=10, height=5, bg = "blue", fg="yellow",command=question3_part6).place(x=625,y=276)
Question9 = Button(root, text="800 ", width=10, height=5, bg = "blue", fg="yellow",command=question4_part6).place(x=625,y=368)
Question10 = Button(root, text="1000 ", width=10, height=5, bg = "blue", fg="yellow",command=question5_part6).place(x=625,y=452)

#topic7 = Button(root, text="Mixed ", width=10, height=5, bg = "blue", fg="blue",command=button_click).place(x=750,y=0)

#newScore = newScore + full_score
shown_score = Button(root, text= "player one Score:" ,command= scores).place(x=0,y=0)
#showinfo(message ="you have " + str(scores) + " points" )


root.mainloop()


