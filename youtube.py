from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
font= ('Dosis', 15)
flie_size = 0

#oncomplete callback function
def completeDownload(stream=None, file_path=None):
    showinfo("Message", "File has been downloaded Successfully...")
    downloadBtn['text'] = 'Download Video'
    downloadBtn['state'] = 'active'
    urlField.delete(0,END)

#onprogress callback function
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    try:
        percent = (100*((flie_size - bytes_remaining)/ flie_size))
        downloadBtn['text']= "{:00.0f}% downloaded ".format(percent)
    except Exception as e:
        print('Oops')


def startDownload(url):
    global file_size
    save_to_path= askdirectory()
    if save_to_path is None:
        return
    try:
        yt=YouTube(url)
        st = yt.streams.first()
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)
        file_size = st.filesize
        st.download(output_path=save_to_path)
    except Exception as e:
        print(e)

# btnClick Function

def btnClicked():
    try:
        downloadBtn['text'] = 'Please wait...'
        downloadBtn['state'] = 'disabled'
        url=urlField.get()
        if url == '':
            return
        # print(url)
        thread=Thread(target=startDownload, args=(url,))
        thread.start()
    except Exception as e:
        print(e)
        print('Some thing wrong')



# Gui
root = Tk()
root.title('My Youtube Downloader ')
root.iconbitmap('images/icon.ico')
root.geometry('500x600')
root.configure(bg='#2C3335')
# Main Icon Section
file = PhotoImage(file  ='images/newgold.png')
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP , pady=5,padx=5)

# Making URL Field
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()
#Download Button
downloadBtn= Button(root, text='Download Video', font='Saira 15 bold', relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)
downloadBtn.configure(width = 15,relief ='flat', bg='#FF362E', fg='white')
root.mainloop()

