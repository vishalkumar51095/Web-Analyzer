
from bs4 import BeautifulSoup as bs

html="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" /><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css" /><link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css" /><link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <link href="https://fonts.googleapis.com/css?family=Happy Monkey" rel="stylesheet" /><link href="https://fonts.googleapis.com/css?family=Bungee Hairline" rel="stylesheet" /><link rel="shortcut icon" type="image/jpg" href="http://varanasikshetra.com/varanasipictures/logos/logo.png" />
<title>This is my Title</title>
  <style>
      </style>
      </head>
      
      <body>
      <h1>This is a Heading</h1>
      </body>
      </html?
"""
#print(html)
scraper = bs(html, 'html.parser')
title=scraper.find_all("body")
item=title[0]
print(item)
print(item.text)