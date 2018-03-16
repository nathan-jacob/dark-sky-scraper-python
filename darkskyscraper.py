from urllib.request import urlopen
wiki = "https://darksky.net/forecast/30.27,-97.724/us12/en"
page = urlopen(wiki)
#gets the page
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
#gives me a way to view the page
all_tables=soup.find_all('span')
right_table=soup.find('span', class_='summary swap')
weather = str(right_table.encode("utf-8"))
weather = weather[29:-9]
#\xcb\x9a\xc2\xa0u"\u00b0"
weather = weather.replace("\\xcb\\x9a\\xc2\\xa0", "\xb0")
basic = soup.find_all('span', class_='num')


basic1 = soup.find_all('span', class_="summary-high-low")
basic1 = str(basic1[0]).encode("utf-8")


feels = basic1
feels = feels[87:89].decode('utf-8')

low = basic1
low = low[147:149].decode('utf-8')

high = basic1
high = high[208:210].decode('utf-8')



basic[0] = str(basic[0])
basic[1] = str(basic[1])
basic[2] = str(basic[2])
basic[3] = str(basic[3])
basic[4] = str(basic[4])
basic[5] = str(basic[5])
wind = basic[0][23:-7] + "mph"
humidity = basic[1][23:-7] + "%"
dewpoint = basic[2][18:-7] + "\xb0"
UVindex = basic[3][18:-7]
visibility = basic[4][23:-7] + "mi"
pressure = basic[5][23:-7] + "mb"


tommorrow=soup.find_all('span')
right_table=soup.find('span', class_='next swap')
tommorrow = str(right_table.encode("utf-8"))
tommorrow = tommorrow[50:-11]
tommorrow = tommorrow.replace("\\xc2\\xa0", " ")
tommorrow = tommorrow.replace(".\\n", " ")

right_table=soup.find('div', class_='summary')
week = str(right_table.encode("utf-8"))
week = week[35:-11]
week = week.replace("\\xc2\\xb0", "\xb0")
week = week.replace(".\\n", " ")



from prettytable import PrettyTable
t = PrettyTable(['today', weather])
t.add_row(['UVindex', UVindex])
t.add_row(['humidity', humidity])
t.add_row(['dewpoint', dewpoint])
t.add_row(['pressure', pressure])
t.add_row(['feels like', feels])
t.add_row(['high', high])
t.add_row(['low', low])
print(t)


from tkinter import *

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= t)
    #this creates a new label to the GUI
    label.pack()

root = Tk()

button = Button(root, text="Check weather", command=printSomething)
button.pack()

root.mainloop()
