import tkinter
import customtkinter
from pytube import YouTube



#Code download YoutubeVideos
#Excecute "python3 YTDownloader.py" from the folder path on the terminal.
#OR run "zsh ytDownloaderSh.sh" from the home directory in the terminal.

#Download function
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback = on_progress)
        title.configure(text=ytObject.title)
        video = ytObject.streams.get_highest_resolution()
        finishLabel.configure(text="")
        #Starting the download
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download error", text_color="red")
    
def on_progress(stream, chunk:bytes, bytes_remaining:int):
    total_size = stream.filesize_mb
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text= per + "%")
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion)/100)



#System settings to have the dark/light appareance of the system and the color theme.
customtkinter.set_appearance_mode("System")
#customtkinter.set_default_color_theme("Blue")

#App frame for the GUI
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert your YouTube link")
title.pack(padx=10, pady=10)

#link input field
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

#Finish downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#To create the Progress bar 
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=15, pady=10)

app.mainloop()




#link = input("Enter your Youtube link: ")
#yt = YouTube("'" + link + "'")

#vidRes = input("Enter the desired resolution (without the p): ")

#vid = yt.streams.get_by_resolution(resolution = vidRes+"p")

#if vid == None:
#   print("No " + vidRes + "p resolution")
#else:
#    print("Title: ", yt.title)
 #   print("Date: ", yt.publish_date)
  #  print("Size: ", vid.filesize_mb)
   # print("Downloading...")
    #vidDownload = vid.download("/home/gilmar/Videos")
#print("Download finished.")

#Run app
