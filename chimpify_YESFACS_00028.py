from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog
from tkinter import ttk
import pandas as pd
import time
import os

timestr = time.strftime("%Y-%m-%d - %H_%M_%S") #assign a timestamp to filename
os.chdir(os.path.expanduser('~/Documents/chimpify/testYESFAC')) #assign the default directory files saves to

class Application(Frame): #create class (create definition of the object)

    def __init__(self, parent): #create object from definition (class)
        Frame.__init__(self, parent) #create frame as object

        self.parent = parent #parent within class Application
        self.initUI() #run within class Application

    def initUI(self): #create the runUI as an object

        self.parent.title("LMS, Inc. - chimpify@YESFACS - Created by MLAROE") #Window title
        self.pack(fill=BOTH, expand=1) #Defines how the title fills its geometry

        menubar = Menu(self.parent) #argument to call Menu function
        self.parent.config(menu=menubar) #parent of child in menu bar

        fileMenu = Menu(menubar) #argument for menubar 
        fileMenu.add_command(label="Open the CLICKS .csv", command=self.onOpen_clicks) #add child, execute function self.onOpen
        fileMenu.add_command(label = "Open the OPENED .csv", command = self.onOpen_opened)
        fileMenu.add_command(label = "Concat opens and clicks", command = self.onOpen_catclicks)
        fileMenu.add_command(label = "Dedupe opens and clicks", command = self.onOpen_dedupe)
        fileMenu.add_command(label = "Open the NOT-OPENED", command = self.onOpen_notopened)
        fileMenu.add_command(label = "Open the BOUNCES", command = self.onOpen_Bounce)
        fileMenu.add_command(label = "Open the UNSUBS", command = self.onOpen_unsubs)
        fileMenu.add_command(label = "concat all files", command = self.onOpen_allfiles)
        fileMenu.add_command(label = "Finalize", command = self.onOpenfinal)
        menubar.add_cascade(label="Select a File", menu=fileMenu) #label for menu info; Gives a name and calls the fileMenu argument

        self.txt = Text(self) #calls tkinter: Text module as argument self.txt
        self.txt.pack(fill=BOTH, expand=1) #for displaying contents of the file in the window (function for a later version)
        

    
        
    def onOpen_clicks(self): #argument for opening the file 

        ftypes = [('CSV files', '*.csv')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '': #if not empty
            csv_inputclicks = self.read_clickCSV(fl)
            self.txt.insert(END, csv_inputclicks)
        
        
    def read_clickCSV(self, filename): #defines everything done to the clicks-csv
        global label #allows the label from def main(): to be affected (global)
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_clicks.csv' that has been appended!", font = labelfont) #displays a new output as a result of the function
        
        f = open(filename, "r") #opens the file that was chosen in the function onOpen
                
                
        outfile_clicks = open('chimpify_clicks %s.csv' % timestr, 'w')
        #print('yay!') #troubleshooting
        
        csv_inputclicks = pd.read_csv(f)
        csv_inputclicks.insert(22, 'Opened', 1)
        csv_inputclicks.insert(23, 'Bounce', '')
        csv_inputclicks.insert(24, 'unsubscribe_reason', '')
        csv_inputclicks.insert(25, 'Unsub', '')
                
        csv_inputclicks.to_csv(outfile_clicks, index = False)
        return csv_inputclicks
        
    def onOpen_opened(self):
        f2types = [('CSV files', '*.csv')]
        dlg2 = filedialog.Open(self, filetypes = f2types)
        fl2 = dlg2.show()
        
        if fl2 != '':
            csv_inputopened = self.read_openedCSV(fl2)
            self.txt.insert(END, csv_inputopened)
    
    def read_openedCSV(self, filename):
        global label
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_opened.csv' that has been appended!", font = labelfont)
        f2 = open(filename, "r")
        
        
        outfile_opened = open('chimpify_opened %s.csv' % timestr, 'w')
        
        csv_inputopened = pd.read_csv(f2)
        csv_inputopened.drop('Opens', axis=1, inplace=True)
        csv_inputopened.insert(22, 'Opened', 1)
        csv_inputopened.insert(23, 'Bounce', '')
        csv_inputopened.insert(24, 'unsubscribe_reason', '')
        csv_inputopened.insert(25, 'Unsub', '')
        csv_inputopened.insert(26, 'URL', '')
        csv_inputopened.insert(27, 'Clicks', '')
        
        csv_inputopened.to_csv(outfile_opened, index = False)
        return csv_inputopened
        
    def onOpen_catclicks(self):
        filenames = filedialog.askopenfilenames()
        
        if filenames != '':
            csv_OandC = self.catclicksandopened(filenames)
            self.txt.insert(END, csv_OandC)
       
        """if filenames != '':
            text8 = self.allfilesConcat(filenames)
            self.txt.insert(END, text8)"""
    
            
    def catclicksandopened(self, filenames):
        global label
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_concat.csv' that has been merged!", font = labelfont)
        
        
        name1 = (filenames[0])
        name2 = (filenames[1])
        #f3 = open(filename, "r")
        csv_clicks = pd.read_csv(name1)
        csv_opens = pd.read_csv(name2)
        
        opensandclicks = (csv_clicks, csv_opens)        
        csv_OandC = pd.concat(opensandclicks)
        
        #for row in csv_clicks:
            #print(row) #debugging
        #print(csv_OandC) 
        output_concat = open('chimpify_concat %s.csv' % timestr, 'w')
        csv_OandC.to_csv(output_concat, index = False) 
        return csv_OandC
        
        
    def onOpen_dedupe(self):
        f4types = [('CSV files', '*.csv')]
        dlg4 = filedialog.Open(self, filetypes = f4types)
        fl4 = dlg4.show()
        
        if fl4 != '':
            deduplicate = self.deduped(fl4)
            self.txt.insert(END, deduplicate)
            
    def deduped(self, filename):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_deduped.csv' that has been deduped!", font = labelfont)    
        
        f4 = open(filename, "r")
        csv_dedupe = pd.read_csv(f4)
        deduplicate = csv_dedupe.drop_duplicates(subset = ['Email Address'])
        output_dedupe = open('chimpify_dedupe %s.csv' % timestr, 'w')
        deduplicate.to_csv(output_dedupe, index = False)
        return deduplicate
        
        
    def onOpen_notopened(self):
        f5types = [('CSV files', '*.csv')]
        dlg5 = filedialog.Open(self, filetypes = f5types)
        fl5 = dlg5.show()
        
        if fl5 != '':
            csv_notopened = self.notOpened(fl5)
            self.txt.insert(END, csv_notopened)
            
    def notOpened(self, filename):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_notopened.csv' that has been appended!", font = labelfont)        
        
        f5 = open(filename, "r")
        csv_notopened = pd.read_csv(f5)
        csv_notopened.insert(22, 'Opened', 0)
        csv_notopened.insert(23, 'Bounce', '')
        csv_notopened.insert(24, 'unsubscribe_reason', '')
        csv_notopened.insert(25, 'Unsub', '')
        csv_notopened.insert(26, 'URL', '')
        csv_notopened.insert(27, 'Clicks', '')
        
        output_notopened = open('chimpify_notopened %s.csv' % timestr, 'w')
        csv_notopened.to_csv(output_notopened, index = False)
        return csv_notopened
        
        
        
    def onOpen_Bounce(self):
        f6types = [('CSV files', '*.csv')]
        dlg6 = filedialog.Open(self, filetypes = f6types)
        fl6 = dlg6.show()
        
        if fl6 != '':
            csv_bounced = self.bounces(fl6)
            self.txt.insert(END, csv_bounced)
            
    def bounces(self, filename):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_bounces.csv' that has been appended!", font = labelfont)
        
        f6 = open(filename, "r")
        csv_bounced = pd.read_csv(f6)
        csv_bounced.insert(22, 'Opened', '')
        csv_bounced.rename(columns={'Bounce Type': 'Bounce'}, inplace=True)
        csv_bounced.insert(24, 'unsubscribe_reason', '')
        csv_bounced.insert(25, 'Unsub', '')
        csv_bounced.insert(26, 'URL', '')
        csv_bounced.insert(27, 'Clicks', '')
        
        output_bounced = open('chimpify_bounces %s.csv' % timestr, 'w')        
        csv_bounced.to_csv(output_bounced, index = False)
        return csv_bounced
        
        
        
    def onOpen_unsubs(self):
        f7types = [('CSV files', '*.csv')]
        dlg7 = filedialog.Open(self, filetypes = f7types)
        fl7 = dlg7.show()
        
        if fl7 != '':
            csv_unsubs = self.unsubs(fl7)
            self.txt.insert(END, csv_unsubs)
        
        if fl7 == '': return
            
    def unsubs(self, filename):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_unsubs.csv' that has been appended!", font = labelfont)
        
        f7 = open(filename, "r")
        csv_unsubs = pd.read_csv(f7)
        csv_unsubs.rename(columns = {'reason': 'unsubscribe_reason'}, inplace = True)
        csv_unsubs.drop('description', axis=1, inplace=True)
        csv_unsubs.insert(23, 'Unsub', 1)
        csv_unsubs.insert(22, 'Opened', '')
        csv_unsubs.insert(23, 'Bounce', '')
        csv_unsubs.insert(26, 'URL', '')
        csv_unsubs.insert(27, 'Clicks', '')
        
        output_unsubs = open('chimpify_unsubs %s.csv' % timestr, 'w')
        csv_unsubs.to_csv(output_unsubs, index = False)
        return csv_unsubs
        
        
    def onOpen_allfiles(self):
        
        filenames = filedialog.askopenfilenames()
        #print(filenames) #debugging
        
        
        #bounce_file = pd.read_csv(filename1)
        #print(bounce_file) #debugging
        
        if filenames != '':
            allconcat = self.allfilesConcat(filenames)
            self.txt.insert(END, allconcat)
            
    def allfilesConcat (self, filenames):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'chimpify_concatall.csv' that has been appended!", font = labelfont)
        
        filename1 = (filenames[0])
        filename2 = (filenames[1])
        filename3 = (filenames[2])
        filename4 = (filenames[3])
        #print("yay!", filename1) #debugging
        fname1 = open(filename1, "r")
        fname2 = open(filename2, "r")
        fname3 = open(filename3, "r")
        fname4 = open(filename4, "r")
        readfname1 = pd.read_csv(fname1)
        #print(readfname1)
        readfname2 = pd.read_csv(fname2)
        readfname3 = pd.read_csv(fname3)
        readfname4 = pd.read_csv(fname4)
        all_csv = (readfname1, readfname2, readfname3, readfname4)
        allconcat = pd.concat(all_csv)
        #print("oh boy!", filename2) #debugging
        #print("woozah!", filename3) #debugging
        #print("ZOMG!!", filename4) #debugging
        #print(allconcat, "huzzah!") #debugging
        
        allconcat.rename(columns = {'Email Address': 'Email_Address', 'Name 1': 'Name_1', 'Member Rating': 'Member_Rating',
                                    'Facility 1': 'Facility1', 'State 1': 'State1', 'Zip 1': 'Zip1', 'Phone 1': 'Phone1',
                                    'Facility 2': 'Facility2', 'Street 2': 'Street2', 'CITY 2': 'CITY2', 
                                    'State 2': 'State2', 'Zip 2': 'Zip2', 'Phone 2': 'Phone2', 'Facility 3': 'Facility3',
                                    'Street 3': 'Street3', 'CITY 3': 'CITY3', 'State 3': 'State3', 'Zip 3': 'Zip3',
                                    'Phone 3': 'Phone3', 'Street 1': 'Street1'}, inplace = True)
        #allconcat.rename(columns =)
        
        
        output_concatall = open('1 chimpify_concatall %s.csv' % timestr, 'w')
        allconcat.to_csv(output_concatall, index = False)
        return allconcat
        
        
    def onOpenfinal(self):
        f9types = [('CSV files', '*.csv')]
        dlg9 = filedialog.Open(self, filetypes = f9types)
        fl9 = dlg9.show()
        
        if fl9 != '':
            finalize = self.finalize(fl9)
            self.txt.insert(END, finalize)
        
        if fl9 == '': return
        
    def finalize(self, filename):
        global label        
        labelfont = ('times', 10, 'bold') #label text info
        label.config(text = "Look in your 'chimpify' folder for the 'Final.csv' that has finished!", font = labelfont)    
        
        f9 = open(filename, "r")
        csv_finish = pd.read_csv(f9)
        finish = csv_finish.sort_values('Unsub').drop_duplicates(subset = ['Email_Address'], keep = 'first')
        output_dedupe = open('chimpify_Final %s.csv' % timestr, 'w')
        finish.to_csv(output_dedupe, index = False)
        return finish
        
        
        
def main():
    global label #allows the label from def main(): to be affected (global)
    root = Tk()
    
    labelfont = ('times', 17, 'bold') #label text info
    label = ttk.Label(root, text = "Select your .csv file to append") #initial label text
    label.config(font = labelfont) #insert labelfont argument
    label.pack(side = "bottom", padx = 20) #places the label on the bottom of the window with a padding of 20 pixels
    
    Application(root) 
    root.geometry("500x360+360+360") #main window geometry
    root.mainloop()


if __name__ == '__main__':
    main()


