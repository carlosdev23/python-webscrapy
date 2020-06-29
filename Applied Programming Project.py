#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Name: Ahmed Saboor Khan
# We new selenium to run this program I used because our content loaded a bit late.
import requests
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


# In[77]:


url = "https://www.udemy.com/courses/search/?q=python"

# Change argument to the location you installed the chrome driver
# (see selenium installation instructions, or get the driver for your
# system from https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome('C:/Users/shah/Downloads/chromedriver_win32/chromedriver')
driver.get(url)

# Give the javascript time to render
time.sleep(7)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source)
# The text containing title and price are in a
# div with class caption.

# Declare variables.
lectureName = []
lectureHours = []
lectureOriginalPrice = []
lectureDiscountPrice = []

for coursesContent in soup.find_all("div", {"class": "course-list--container--3zXPS"}):   
    for courseContent in coursesContent.contents:
        # get lecture hours.
        for courseDuration in courseContent.find_all(class_="udlite-text-xs course-card--course-meta-info--1hHb3"):
            #print( courseDuration.contents[0].get_text().replace(' total hours', '') );
            lectureHours.append( float(courseDuration.contents[0].get_text().replace(' total hours', '') ));
        # get lecture name.
        for courseName in courseContent.find_all(class_="course-card--course-title--2f7tE"):
            #print(courseName.get_text());
            lectureName.append( courseName.get_text());
        # get lecture price and orginal price.
        for price in courseContent.find_all(class_="course-card--price-text-container--2sb8G"):
            if len( price.contents ) == 2:
                lectureDiscountPrice.append( float(price.contents[0].find_all('span')[2].get_text().replace('$', ''))*2);
                lectureOriginalPrice.append( float(price.contents[1].find_all('span')[2].get_text().replace('$', '')));
                #print( price.contents[0].find_all('span')[2].get_text() );
                #print( price.contents[1].find_all('span')[2].get_text() );
                
#print( lectureName)
##print( lectureHours)
#print( lectureOriginalPrice)
#print( lectureDiscountPrice)


# In[85]:



#print(lectureDiscountPrice );
plt.bar([0.25,1.25,2.25,3.25,4.25],lectureDiscountPrice[0:5],
label="Discount Course Price",color='b',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],lectureOriginalPrice[0:5],
label="Original Course Price", color='r',width=.5)
plt.legend()
plt.xlabel('Courses')
plt.ylabel('Prices')
plt.title('Orginal Price vs Discount Price')
plt.show()


# In[74]:


style.use('ggplot')
plt.plot([1,2,3,4,5,6,7,8],lectureHours,'g',label='line one', linewidth=5)
plt.title('Course Duration With Ranging')
plt.ylabel('Course Duration In Hours -Y axis')
plt.xlabel('Course Ranges - X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()


# In[92]:


plt.scatter([1,2,3,4,5],lectureDiscountPrice[0:5], label='Discount Price',color='r')
plt.scatter([1,2,3,4,5],lectureOriginalPrice[0:5],label='Original Price',color='b')
plt.xlabel('Course')
plt.ylabel('Price')
plt.title('Course Vs Price')
plt.legend()
plt.show()


# In[103]:


x = [1,2,3,4,5,6,7,8,9,10]
label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
plt.bar(x[0:5], lectureHours[0:5], tick_label=lectureName[0:5])
plt.xlabel('Course')
plt.ylabel('Hours')
plt.title('Course Vs Hourse')
plt.show()


# In[ ]:




