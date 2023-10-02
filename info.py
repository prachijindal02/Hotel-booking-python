from os import stat
from tkinter import*
from PIL import Image, ImageTk #pip install pillow


class Info_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1600x700+0+0")
        self.root.config(bg='black')



        ##################  info ###########################
        img3 = Image.open("final.png")
        img3 = img3.resize((1100,660),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=35,width=1120,height=700)






if __name__ == "__main__":
    root=Tk()
    Obj=Info_details(root)
    root.mainloop()
