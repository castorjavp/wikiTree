from tkinter import *
from tkinter import ttk
from scraper import Scraper
from collections import deque

links = {}
app = Tk()

linksSeen = set()

def callback():
	treeLabel.config({"text":f"Tree View for {searchEntry.get()}"})
	populateTreeView(treeview, searchEntry.get())

def populateTreeView(treeview,url):
	randomLinks = Scraper.getLinks(url, linksSeen)
	insertParentLinks(treeview, randomLinks)
	for title,link in randomLinks.items():
		q = deque()
		q.append({"title":title, "link":link})
		while get_all_children(treeview, title) <= 16:
			parent = q.popleft()
			childrenLinks = Scraper.getLinks(parent["link"], linksSeen)
			for titleChild, linkChild in childrenLinks.items():
				treeview.insert("", 0, titleChild, text=titleChild)	
				treeview.move(titleChild, parent["title"],"end")
				q.append({"title": titleChild, "link": linkChild})				
		
def get_all_children(treeview, item=""):
	children = treeview.get_children(item)
	if len(children) == 0:
		return 0
	for child in children:
		return len(treeview.get_children(item)) + get_all_children(treeview, child)

def insertParentLinks(treeview, links):
	i=0
	for title,link in links.items():
		treeview.insert("", f"{i}", title , text=title)
		i+=1

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