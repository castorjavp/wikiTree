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
	insertLinksToParents(treeview, randomLinks)


def insertLinks(treeview, links):
	i=0
	for title,link in links.items():
		treeview.insert("", f"{i}", title , text=title)
		i+=1

def insertLinksToParents(treeview, parentLinks):
	for title, link in parentLinks.items():
		currentLinkChildren = Scraper.getLinks(link, linksSeen)
		for k,v in currentLinkChildren.items():
			treeview.insert("", 0, k, text=k)	
			treeview.move(k,title,"end")
			print(treeview.parent(item=title))
			if len(get_all_children(treeview,treeview.parent(item=k))) >= 16:
				return

		insertLinksToParents(treeview, currentLinkChildren)

def getSizeOfParent(treeview, parent="", size=0):
	children = treeview.get_children(parent)
	size += len(children)
	for child in children:
		return size + getSizeOfParent(treeview, child, size)

def get_all_children(tree, item=""):
    children = tree.get_children(item)
    for child in children:
        children += get_all_children(tree, child)
    return children

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