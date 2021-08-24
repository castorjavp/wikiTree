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
	insertLinks(treeview, randomLinks)
	print(randomLinks)
	index = 0
	for title, link in randomLinks.items():	
		insertLinksToParent(treeview, title, link, index)
		index+=1


def insertLinks(treeview, links):
	i=0
	for title,link in links.items():
		treeview.insert("", f"{i}", title , text=title)
		i+=1
def insertLinksToParent(treeview, title, link, index):
	print(get_all_children(treeview, treeview.get_children()[index]))
	if get_all_children(treeview, treeview.get_children()[index]) >= 72:
		return		
	currentLinkChildren = Scraper.getLinks(link, linksSeen)
	for k,v in currentLinkChildren.items():
		treeview.insert("", 0, k, text=k)	
		treeview.move(k,title,"end")
	for title, link in currentLinkChildren.items():		
		insertLinksToParent(treeview, title,link,index)

def insertLinksToParents(treeview, parentLinks, i=0):
	print(treeview.get_children()[i])
	print(get_all_children(treeview, treeview.get_children()[i]))
	if get_all_children(treeview, treeview.get_children()[i]) >= 13:
		i+=1
		return		
	for title, link in parentLinks.items():
		currentLinkChildren = Scraper.getLinks(link, linksSeen)
		for k,v in currentLinkChildren.items():
			treeview.insert("", 0, k, text=k)	
			treeview.move(k,title,"end")		
		insertLinksToParents(treeview, currentLinkChildren,i)

def getSizeOfParent(treeview, parent="", size=0):
	children = treeview.get_children(parent)
	size += len(children)
	for child in children:
		return size + getSizeOfParent(treeview, child, size)

def get_all_children(treeview, item=""):
	children = treeview.get_children(item)
	if len(children) == 0:
		return 0
	for child in children:
		return len(treeview.get_children(item)) + get_all_children(treeview, child)
    

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