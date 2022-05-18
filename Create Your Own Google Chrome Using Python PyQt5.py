#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://pypi.org/project/PyQt5/


# In[2]:


# !pip install PyQt5


# In[3]:


pip install PyQtWebEngine


# In[4]:


from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys


# In[ ]:


class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://Google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar=QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction('forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        reload_btn = QAction('reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        home_btn = QAction('home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.browser.urlChanged.connect(self.update_url)
        
        
        
        
        
    def navigate_home(self):
            self.browser.setUrl(QUrl('http://Google.com'))
            
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    def update_url(self,q):
        self.url_bar.setText(q.toString())
    
    
        
app=QApplication(sys.argv)
QApplication.setApplicationName("Python browser")
window = MainWindow()
app.exec_()


# In[ ]:





# In[ ]:




