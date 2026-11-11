# Detect_-phishing.py
To evaluate, detect, and warn users about potentially malicious or fraudulent URLs before they navigate to them. ​Core Technologies: Python, scikit-learn (Random Forest Regressor), Pandas, Tkinter for graphical user interface (GUI) alerts, and modular condition checks (Condition1, Condition2, Condition3, Condition4) for feature extraction.
Feature Extraction: The script accepts a target URL via command line (os.sys.argv[1]) and runs it through multiple modular condition scripts to analyze structural red flags.  
​Machine Learning Model: It loads training datasets (TrainingDataset1.csv) and utilizes a Random Forest Regressor to classify and predict the threat level of the website based on historical patterns.  
​Interactive UI Alerts: Using tkinter and image assets (safe.jpg, alert.jpg, danger.jpg), the application generates distinct warning dialogs and safety prompts:  
​Safe Sites: Prompts a confirmation dialog asking if you want to proceed to the legitimate website.  
​Suspicious/Phishing Sites: Triggers warnings and alerts, allowing you to abort or override the action.  
