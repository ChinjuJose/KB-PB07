from tkinter import *

root = Tk()
root.title("Sentences")
root.geometry("400x400")
    
def check():
    palindromes = []
    reversedSentence=""
    sentence = input.get()
    words = sentence.split(" ")

    for word in words[::-1]:    
        reversedSentence = reversedSentence + word + " "
        if word.lower() == word[::-1].lower():
            palindromes.append(word)

    resultLabel1["text"] = "The reversed sentence: '"+reversedSentence+"'"
    resultLabel2["text"] = "Number of words: "+str(len(words))
    resultLabel3["text"] = "Palindrome words in the sentence: "+str(palindromes)

input = Entry(root)
input.place(relx=0.5, rely=0.2, anchor=CENTER)

btn = Button(root, text="Reverse and Check", command = check)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

resultLabel1 = Label(root,text="!")
resultLabel1.place(relx=0.5, rely=0.4, anchor=CENTER)

resultLabel2 = Label(root,text="!")
resultLabel2.place(relx=0.5, rely=0.5, anchor=CENTER)

resultLabel3 = Label(root,text="!")
resultLabel3.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()


