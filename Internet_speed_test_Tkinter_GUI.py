from tkinter import *
import speedtest
root = Tk()
root.title("Internet Speed Test")
root.geometry("500x500")
root.config(bg = "red")
def testspeed():
    ts = speedtest.Speedtest()
    ts.get_servers()
    download = str(round(ts.download()/(10**6),2))+"  Mbps"
    upload = str(round(ts.upload()/(10**6),2))+"  Mbps"
    label_download.config(text=download)
    label_upload.config(text=upload)
    pass
label = Label(root, text = "Internet Speed Testing", font = ("Calibri", 30, "bold" ), bg = "red", fg = "white").place(x=60, y=30, width=380, height=50)

label = Label(root, text = "Download Speed", font = ("Calibri", 25, "bold", "italic" )).place(x=60, y=100, width=380, height=50)
label_download = Label(root, text = "00  Mbps", font = ("Calibri", 20, "bold" ))
label_download.place(x=60, y=155, width=380, height=50)
label = Label(root, text = "Upload Speed", font = ("Calibri", 25, "bold", "italic")).place(x=60, y=220, width=380, height=50)
label_upload = Label(root, text = "00  Mbps", font = ("Calibri", 20, "bold" ))
label_upload.place(x=60, y=275, width=380, height=50)
button = Button(root, text = "Test Speed", font = ("Calibri", 30, "bold"), relief=RAISED, command=testspeed).place(x=60, y=350, width=380, height=50)

root.mainloop()
"""The code imports the Tkinter module and the speedtest module, which is used to test the internet connection speed.

Then, a Tkinter window is created with the title "Internet Speed Test", a size of 500x500 pixels, and a red background.

The testspeed function is defined, which uses the speedtest module to get the download and upload speeds in megabits per second (Mbps). These speeds are then converted to strings and displayed on the window using labels.

The main layout of the window is created using labels and a button. The labels display the text "Internet Speed Testing", "Download Speed", "Upload Speed", and the button displays the text "Test Speed". The labels for the download and upload speeds are initially set to "00" and will be updated with the actual speeds when the "Test Speed" button is clicked.

Finally, the mainloop function is called to start the event loop and display the window."""