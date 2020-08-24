from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os, shutil

class Sorting_App:
        def __init__(self, root):
                self.root = root
                self.root.title("Sorting Application")
                self.root.config(bg="white")
                self.root.geometry("1350x700+0+0")

                self.logo_icon = PhotoImage(file="images/00 - folder.png")
                self.btn_browse_icon = PhotoImage(file="images/00 - browse.png")
                title = Label(self.root, text="FILES SORTING APPLICATION",image=self.logo_icon, compound=LEFT, padx=20, pady=5, font="impact 40", bg= "#023548", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        # ------------------------------------------- BROWSE SECTION ----------------------------------------

                self.var_foldername = StringVar()
                lbl_select_folder = Label(self.root, text= "Select Folder", font= ("times new roman", 25), bg="white", fg= "black").place(x= 60, y= 120)
                txt_folder_name = Entry(self.root, font= ("times new roman", 15), textvariable= self.var_foldername, bg= "lightyellow", state="readonly").place(x= 250, y= 120, height= 40, width= 650)
                btn_browse = Button(self.root, command= self.browse_function, image=self.btn_browse_icon, bg="white", fg="white", activebackground= "white", activeforeground="white", cursor= "hand2").place(x= 920, y= 120)
                hr = Label(self.root, bg="lightgray").place(x= 60, y= 180, height= 2, width= 1230)

        # ----------------------------------------- EXTENSION SECTION --------------------------------------

                self.image_extensions = ["Image Extensions", '.img', '.jpg', '.jpeg', '.png', '.psd']
                self.video_extensions = ["Video Extensions", '.mp4', '.avi', '.mpeg4']
                self.audio_extensions = ["Audio Extensions", '.mp3', '.wav']
                self.document_extensions = ["Document Extension", '.pdf', '.html', '.mhtml', '.doc', '.ppt', '.pptx', '.docx', '.xlsx']

                self.folders = {
                        'images': self.image_extensions,
                        'videos': self.video_extensions,
                        'audios': self.audio_extensions,
                        'documents': self.document_extensions,
                }

                lbl_select_folder = Label(self.root, text= "Various Supported Extension", font= ("times new roman", 25), bg="white", fg= "black").place(x= 60, y= 190)
                self.image_box = ttk.Combobox(self.root, values= self.image_extensions, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.image_box.place(x= 60, y= 250, width= 270, height= 35)
                self.image_box.current(0)

                self.video_box = ttk.Combobox(self.root, values= self.video_extensions, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.video_box.place(x= 380, y= 250, width= 270, height= 35)
                self.video_box.current(0)

                self.audio_box = ttk.Combobox(self.root, values= self.audio_extensions, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.audio_box.place(x= 700, y= 250, width= 270, height= 35)
                self.audio_box.current(0)

                self.document_box = ttk.Combobox(self.root, values= self.document_extensions, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.document_box.place(x= 1020, y= 250, width= 270, height= 35)
                self.document_box.current(0)

        # ---------------------------------------- IMAGEICON SECTION -------------------------------------

                self.image_icon = PhotoImage(file="images/00 - images.png")
                self.audio_icon = PhotoImage(file="images/00 - audios.png")
                self.video_icon = PhotoImage(file="images/00 - videos.png")
                self.document_icon = PhotoImage(file="images/00 - documents.png")
                self.other_icon = PhotoImage(file="images/00 - others.png")

                Frame1 = Frame(self.root, bd= 2, relief= RIDGE, bg="white")
                Frame1.place(x= 60, y= 310, width= 1230, height= 300)
                self.lbl_total_files = Label(Frame1, text= "Total Files: ", font= ("times new roman", 20), bg="white", fg= "black")
                self.lbl_total_files.place(x= 10, y= 10)
                
                self.lbl_total_images = Label(Frame1, bd= 2, relief= RAISED, image= self.image_icon, compound= TOP, pady= 10, font=("times new roman", 20, "bold"), bg= "#0875B7", fg= "white")
                self.lbl_total_images.place(x= 15, y= 60, width= 230, height= 200)

                self.lbl_total_audios = Label(Frame1, bd= 2, relief= RAISED, image= self.audio_icon, compound= TOP, pady= 10, font=("times new roman", 20, "bold"), bg= "#0875B7", fg= "white")
                self.lbl_total_audios.place(x= 255, y= 60, width= 230, height= 200)

                self.lbl_total_videos = Label(Frame1, bd= 2, relief= RAISED, image= self.video_icon, compound= TOP, pady= 10, font=("times new roman", 20, "bold"), bg= "#0875B7", fg= "white")
                self.lbl_total_videos.place(x= 495, y= 60, width= 230, height= 200)

                self.lbl_total_documents = Label(Frame1, bd= 2, relief= RAISED, image= self.document_icon, compound= TOP, pady= 10, font=("times new roman", 20, "bold"), bg= "#0875B7", fg= "white")
                self.lbl_total_documents.place(x= 735, y= 60, width= 230, height= 200)

                self.lbl_total_others = Label(Frame1, bd= 2, relief= RAISED, image= self.other_icon, compound= TOP, pady= 10, font=("times new roman", 20, "bold"), bg= "#0875B7", fg= "white")
                self.lbl_total_others.place(x= 975, y= 60, width= 230, height= 200)

        # ---------------------------------------- IMAGEICON SECTION -------------------------------------

                lbl_status = Label(self.root, text= "STATUS", font= ("times new roman", 20), bg="white", fg= "black").place(x= 60, y= 630)
                self.lbl_st_total = Label(self.root, text= "", font= ("times new roman", 20), bg="white", fg= "red")
                self.lbl_st_total.place(x= 260, y= 630)
                
                self.lbl_st_moved = Label(self.root, text= "", font= ("times new roman", 20), bg="white", fg= "green")
                self.lbl_st_moved.place(x= 460, y= 630)
                
                self.lbl_st_left = Label(self.root, text= "", font= ("times new roman", 20), bg="white", fg= "orange")
                self.lbl_st_left.place(x= 660, y= 630)

        # -------------------------------------- STATUS & BUTTON SECTION ----------------------------------

                self.btn_clear = Button(self.root, command=self.clear, text="CLEAR", font= ("times new roman", 15, "bold"), bg="#262626", fg="white", activebackground= "#262626", activeforeground="white", cursor= "hand2")
                self.btn_clear.place(x= 870, y= 630, height= 45, width= 200)
                self.btn_start = Button(self.root, command=self.start_function, state=DISABLED, text="START", font= ("times new roman", 15, "bold"), bg="#ff5722", fg="white", activebackground= "#ff5722", activeforeground="white", cursor= "hand2")
                self.btn_start.place(x= 1090, y= 630, height= 45, width= 200)

        def Total_count(self):
                images = 0
                audios = 0
                videos = 0
                documents = 0
                others = 0
                self.count = 0
                cmbine_list = []
                for i in self.all_files:
                        if os.path.isfile(os.path.join(self.directry, i)) == True:
                                self.count += 1
                                ext = "."+i.split(".")[-1]
                                for folder_name in self.folders.items():
                                        for x in folder_name[1]:
                                                cmbine_list.append(x)
                                        if ext.lower() in folder_name[1] and folder_name[0] == "images":
                                                images+= 1
                                        if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                                                audios+= 1
                                        if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                                                videos+= 1
                                        if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                                                documents+= 1
                
# -------------------------------------- Calculating Other files only -----------------------------------

                for i in self.all_files:
                        if os.path.isfile(os.path.join(self.directry, i)) == True:
                                ext = "."+i.split(".")[-1]
                                if ext.lower() not in cmbine_list:
                                        others+= 1

                self.lbl_total_images.config(text= "Total Images\n" + str(images))
                self.lbl_total_audios.config(text= "Total Audios\n" + str(audios))
                self.lbl_total_videos.config(text= "Total Videos\n" + str(videos))
                self.lbl_total_documents.config(text= "Total Documents\n" + str(documents))
                self.lbl_total_others.config(text= "Other Files\n" + str(others))
                self.lbl_total_files.config(text= "Total Files: " + str(self.count))

        def browse_function(self):
                op = filedialog.askdirectory(title="Select folder for Sorting")
                if op != None:
                        self.var_foldername.set(str(op))
                        self.directry = self.var_foldername.get()
                        self.other_name = "others"
                        self.rename_folder()
                        self.all_files = os.listdir(self.directry)
                        length = len(self.all_files)
                        count= 1
                        self.Total_count()
                        self.btn_start.config(state=NORMAL)
                        
        def start_function(self):
                if self.var_foldername.get()!="":
                        self.btn_clear.config(state=DISABLED)
                        c = 0
                        for i in self.all_files:
                                if os.path.isfile(os.path.join(self.directry, i)) == True:
                                        c+= 1
                                        self.create_move(i.split(".")[-1], i)
                                        self.lbl_st_total.config(text= "TOTAL: "+str(self.count))
                                        self.lbl_st_moved.config(text= "MOVED: "+str(c))
                                        self.lbl_st_left.config(text= "LEFT: "+str(self.count - c))

                                        self.lbl_st_total.update()
                                        self.lbl_st_moved.update()
                                        self.lbl_st_left.update()

                        messagebox.showinfo("Success", "All files has moved successfully")
                        self.btn_start.config(state=DISABLED)
                        self.btn_clear.config(state=NORMAL)
                else:
                        messagebox.showerror("Error", "Please select the folder")

        def clear(self):
                self.btn_start.config(state=DISABLED)
                self.var_foldername.set("")
                self.lbl_st_total.config(text= "")
                self.lbl_st_moved.config(text= "")
                self.lbl_st_left.config(text= "")
                self.lbl_total_images.config(text= "")
                self.lbl_total_audios.config(text= "")
                self.lbl_total_videos.config(text= "")
                self.lbl_total_documents.config(text= "")
                self.lbl_total_others.config(text= "")
                self.lbl_total_files.config(text= "Total Files: ")



        def rename_folder(self):
                for folder in os.listdir(self.directry):
                        if os.path.isdir(os.path.join(self.directry, folder)) == True:
                                os.rename(os.path.join(self.directry, folder), os.path.join(self.directry, folder.lower()))


        def create_move(self, ext, file_name):
                find=False
                for folder_name in self.folders:
                        if "."+ext in self.folders[folder_name]:
                                if folder_name not in os.listdir(self.directry):
                                        os.mkdir(os.path.join(self.directry, folder_name))
                                shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, folder_name))
                                find=True
                                break

                if find != True:
                        if self.other_name not in os.listdir(self.directry):
                                os.mkdir(os.path.join(self.directry, self.other_name))
                        shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, self.other_name))


root = Tk()
obj = Sorting_App(root)
root.mainloop()