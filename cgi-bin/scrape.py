from bs4 import BeautifulSoup
#importing data from form to python file
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

print(searchterm)