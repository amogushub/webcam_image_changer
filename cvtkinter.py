from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np

root = Tk()
root.geometry('400x400')
root.title("Alterador de vídeo")

path = cv2.VideoCapture(0)

def new_canny():
    global panelA
    global panelB
    newWindow = Toplevel(root)

    newWindow.title("New Window")

    newWindow.geometry("1000x600")
    panelA = Label(newWindow) 
    panelA.place(x=100, y = 100, height = 400, width = 400)
    panelB = Label(newWindow)
    panelB.place(x=500, y = 100, height = 400, width = 400)
    textoori = Label(newWindow, text = "Imagem original", font=50)
    textoori.place(x=100, y = 20, height = 50, width = 150)
    textoalt = Label(newWindow, text = "Imagem contornada", font=50)
    textoalt.place(x=500, y = 20, height = 50, width = 150)
    canny()
def new_gaussian():
    global panelA
    global panelB
    newWindow = Toplevel(root)

    newWindow.title("New Window")

    newWindow.geometry("1000x600")
    panelA = Label(newWindow) 
    panelA.place(x=100, y = 100, height = 400, width = 400)
    panelB = Label(newWindow)
    panelB.place(x=500, y = 100, height = 400, width = 400)
    textoori = Label(newWindow, text = "Imagem original", font=50)
    textoori.place(x=100, y = 20, height = 50, width = 150)
    textoalt = Label(newWindow, text = "Apenas cores azuis", font=50)
    textoalt.place(x=500, y = 20, height = 50, width = 150)
    gaussian()
def new_cascade():
    global panelA
    global panelB
    newWindow = Toplevel(root)

    newWindow.title("New Window")

    newWindow.geometry("1000x600")
    panelA = Label(newWindow) 
    panelA.place(x=100, y = 100, height = 400, width = 400)
    panelB = Label(newWindow)
    panelB.place(x=500, y = 100, height = 400, width = 400)
    textoori = Label(newWindow, text = "Imagem original", font=50)
    textoori.place(x=100, y = 20, height = 50, width = 150)
    textoalt = Label(newWindow, text = "Faces detectadas", font=50)
    textoalt.place(x=500, y = 20, height = 50, width = 150)
    cascade()
def new_laplacian():
    global panelA
    global panelB
    newWindow = Toplevel(root)

    newWindow.title("New Window")

    newWindow.geometry("1000x600")
    panelA = Label(newWindow) 
    panelA.place(x=100, y = 100, height = 400, width = 400)
    panelB = Label(newWindow)
    panelB.place(x=500, y = 100, height = 400, width = 400)
    textoori = Label(newWindow, text = "Imagem original", font=50)
    textoori.place(x=100, y = 20, height = 50, width = 150)
    textoalt = Label(newWindow, text = "Gradiente de imagem contornada", font=50)
    textoalt.place(x=500, y = 20, height = 50, width = 250)
    laplacian()
def canny():
    _, frame = path.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(opencv_image, 50, 100)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    edged = Image.fromarray(edged)
    image = ImageTk.PhotoImage(image.resize((400,400)))
    edged = ImageTk.PhotoImage(edged.resize((400,400)))
    panelA.photo_image = image
    panelA.configure(image=image)
    panelB.photo_image = edged
    panelB.configure(image=edged)
    panelA.after(10, canny)
def gaussian():
    _, frame = path.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(opencv_image, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    edged = cv2.GaussianBlur(res,(15,15),0)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    edged = Image.fromarray(edged)
    image = ImageTk.PhotoImage(image.resize((400,400)))
    edged = ImageTk.PhotoImage(edged.resize((400,400)))
    panelA.photo_image = image
    panelA.configure(image=image)
    panelB.photo_image = edged
    panelB.configure(image=edged)
    panelA.after(10, gaussian)
def cascade():
    _, frame = path.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    edged = image
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image.resize((400,400)))
    panelA.photo_image = image
    panelA.configure(image=image)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(edged,(x,y),(x+w,y+h),(255,0,0),2)
    edged = Image.fromarray(edged)
    
    
    edged = ImageTk.PhotoImage(edged.resize((400,400)))
    
    
    panelB.photo_image = edged
    panelB.configure(image=edged)
    panelA.after(10, cascade)
def laplacian():
    _, frame = path.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lap = cv2.Laplacian(frame, cv2.CV_64F)
    lap = np.uint8(lap)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    edged = Image.fromarray(lap)
    image = ImageTk.PhotoImage(image.resize((400,400)))
    edged = ImageTk.PhotoImage(edged.resize((400,400)))
    panelA.photo_image = image
    panelA.configure(image=image)
    panelB.photo_image = edged
    panelB.configure(image=edged)
    panelA.after(10, laplacian)
btn1 = Button(root, text="Canny", command=new_canny)
btn1.place(x=100, y = 300, height = 50, width = 100)
btn2 = Button(root, text="Gaussian", command=new_gaussian)
btn2.place(x=200, y = 300, height = 50, width = 100)
btn3 = Button(root, text="Cascade", command=new_cascade) 
btn3.place(x=100, y = 350, height = 50, width = 100)
btn4 = Button(root, text="Laplacian", command=new_laplacian)
btn4.place(x=200, y = 350, height = 50, width = 100)
root.mainloop()
