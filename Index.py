# Detect_-phishing.py
import Condition1
import Condition2
import Condition3
import Condition4
import pandas as pd
import os
import webbrowser
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# Get website argument from command line
website = os.sys.argv[1]

# Run feature extraction conditions
Condition1.category1(website)
Condition2.category2(website)
Condition3.category3(website)
Condition4.category4(website)

# Load test and training data
read = pd.read_csv(r'phishing5.txt', header=None, sep=',')
read = read.iloc[:, -1].values

dataset = pd.read_csv(r'TrainingDataset1.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1001)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, criterion="mse", random_state=2)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(estimator=regressor, X=X_train, y=y_train, cv=5)
accuracy.mean()
accuracy.std()

# Predict phishing status
Detect_phishing_website = regressor.predict(read)

if Detect_phishing_website == 1:
    top = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("safe.jpg"))
    background = tk.Label(top, image=img, bd=0)
    background.pack(fill="both", expand=False)
    background.image = img
    background.rowconfigure(0, weight=100)
    background.rowconfigure(3, weight=100)
    background.columnconfigure(0, weight=100)
    background.columnconfigure(3, weight=100)
    
    reply = messagebox.askyesno("REQUEST!!!", "Can I redirect to this Legitimate Website?")
    
    if reply == True:
        webbrowser.open(website)
    else:
        exit()
        
    top.mainloop()

elif Detect_phishing_website > 0 and Detect_phishing_website < 0.6:
    top = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("alert.jpg"))
    background = tk.Label(top, image=img, bd=0)
    background.pack(fill='both', expand=False)
    background.image = img
    background.rowconfigure(0, weight=100)
    background.rowconfigure(3, weight=100)
    background.columnconfigure(0, weight=100)
    background.columnconfigure(3, weight=100)
    
    reply = messagebox.askyesno("WARNING!!!", "Do you want to continue? It's a Suspicious website??")
    
    if reply == True:
        webbrowser.open(website)
    else:
        exit()
        
    top.mainloop()

else:
    top = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("danger.jpg"))
    background = tk.Label(top, image=img, bd=0)
    background.pack(fill='both', expand=False)
    background.image = img
    background.rowconfigure(0, weight=100)
    background.rowconfigure(3, weight=100)
    background.columnconfigure(0, weight=100)
    background.columnconfigure(3, weight=100)
    
    reply = messagebox.askyesno("ALERT!!!", "Do you want to continue? It's a phishing website??")
    
    if reply == True:
        webbrowser.open(website)
    else:
        exit()
        
    top.mainloop()
