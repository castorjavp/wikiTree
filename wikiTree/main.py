from tkinter import *
from tkinter import ttk
from scraper import Scraper


links = {}
app = Tk()

linksSeen = set()

def callback():
	treeLabel.config({"text":f"Tree View for {searchEntry.get()}"})
	populateTreeView(treeview, searchEntry.get())

def populateTreeView(treeview,url):
	randomLinks = Scraper.getLinks(url, linksSeen)
	i=0
	for title,link in randomLinks.items():
		treeview.insert("", f"{i}", title , text=title)
		i+=1
	for title, link in randomLinks.items():
		currentLinkChildren = Scraper.getLinks(link, linksSeen)
		for k,v in currentLinkChildren.items():
			treeview.insert("", f"{i}", k, text=k)	
			treeview.move(k,title,"end")	

app.title("WikiTree")
app.geometry("800x450")

lblTitle = ttk.Label(app, text="WikiTree", font=(('Arial'), 22))
searchLabel = ttk.Label(app, text="Enter Link or Keyword: ")
searchEntry = ttk.Entry(app, width=30)
searchButton = ttk.Button(app, text="Run", command=callback)
lblTitle.grid(row=0, column=1)
searchLabel.grid(row=1, column=0)
searchEntry.grid(row=1, column=1)
searchButton.grid(row=1, column=2,padx=3)

treeLabel = ttk.Label(app, text="Tree View")
treeLabel.grid(row=2,column=1)

# Creating treeview 
treeview = ttk.Treeview(app)
treeview.grid(row=3, column=0, columnspan=5, sticky=W+E)

app.mainloop()