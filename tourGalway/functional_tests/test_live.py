# -*- coding: utf-8 -*-
#The first line is the encoding to use in this file in this case UTF-8
from selenium import webdriver
import unittest
import time
#Next we import all the packages we need
#We import selenium and unittest which is a test package in python
#We are also importing time which allows us to set a wait so that we can see the output in the brower 

#We create a class NewVistorTest which inherits from TestCase  
class NewVisitorTest(unittest.TestCase):
#setUp runs at the begining of the test and setups whatever we need, in this case it lauches the Firefox browser
    def setUp(self):
        self.browser = webdriver.Firefox() #lauch Firefox browser, requires geckodriver.exe to be on your PATH
        self.browser.implicitly_wait(3)

#tearDown runs at the end of the test and will clear up anything we have setup so in this case it will quit the browser
    def tearDown(self):
   		self.browser.quit() #
#This is our test method
#Here we are testing that the phrase Welcome to Django is being displayed in the page available at http://localhost:8000, our development server
    def test_title(self):
        self.browser.get('http://localhost:8000')
        time.sleep(5)


#This launches the unittest Test runner, it looks for methods that start with test and executes them, we are setting warnings to ignore as we are not interested at the moment.
if __name__ == '__main__':
    unittest.main(warnings='ignore')