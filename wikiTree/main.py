from tkinter import *
from tkinter import ttk
from scraper import Scraper

links = {}
app = Tk()
def callback():
	links =  Scraper.getLinks(searchEntry.get())
	print(links)
app.title("WikiTree")
app.geometry("500x450")

lblTitle = ttk.Label(app, text="WikiTree", font=(('Arial'), 22))
searchLabel = ttk.Label(app, text="Enter Link or Keyword: ")
searchEntry = ttk.Entry(app, width=30)
searchButton = ttk.Button(app, text="Run", command=callback)
lblTitle.grid(row=0, column=1)
searchLabel.grid(row=1, column=0)
searchEntry.grid(row=1, column=1)
searchButton.grid(row=1, column=2,padx=3)
# ttk.Label(app, text="Treeview(hierarchical)").pack()

# Creating treeview window
# treeview = ttk.Treeview(app)
#
# # Calling pack method on the treeview
# treeview.pack()
#
# # Inserting items to the treeview
# # Inserting parent
# treeview.insert('', '0', 'item1',
# 				text='GeeksforGeeks')
#
# # Inserting child
# treeview.insert('', '1', 'item2',
# 				text='Computer Science')
# treeview.insert('', '2', 'item3',
# 				text='GATE papers')
# treeview.insert('', 'end', 'item4',
# 				text='Programming Languages')
#
# # Inserting more than one attribute of an item
# treeview.insert('item2', 'end', 'Algorithm',
# 				text='Algorithm')
# treeview.insert('item2', 'end', 'Data structure',
# 				text='Data structure')
# treeview.insert('item3', 'end', '2018 paper',
# 				text='2018 paper')
# treeview.insert('item3', 'end', '2019 paper',
# 				text='2019 paper')
# treeview.insert('item4', 'end', 'Python',
# 				text='Python')
# treeview.insert('item4', 'end', 'Java',
# 				text='Java')
#
# # Placing each child items in parent widget
# treeview.move('item2', 'item1', 'end')
# treeview.move('item3', 'item1', 'end')
# treeview.move('item4', 'item1', 'end')

# Calling main()
app.mainloop()