# **Network Security: Phishing Website Detection Using Machine Learning**

## **📌 Overview**  
Phishing attacks pose a significant cybersecurity threat, tricking users into providing sensitive information through deceptive websites. This project utilizes **machine learning** to detect **phishing websites** based on various extracted features from URLs.  

## **🚀 Project Objective**  
The goal of this project is to develop an intelligent system that can distinguish between **legitimate** and **phishing** websites using machine learning models. The system analyzes URL attributes such as domain registration length, SSL certificate status, presence of suspicious characters, and page behavior to detect malicious sites with high accuracy.  

## **📂 Dataset Description**  
The dataset consists of several key URL-based features, including:  
- **URL structure attributes:** Presence of IP address, URL length, special characters (e.g., `@`, `//`, `-`).  
- **Security indicators:** SSL certificate status, HTTPS token, age of the domain.  
- **Behavioral features:** Redirects, pop-ups, iframe usage, abnormal URLs, and Google Index status.  
- **Network-based attributes:** DNS record availability, web traffic ranking, and links pointing to the page.  
- **Target Label (`Result`):**  
  - `1` → **Legitimate website**  
  - `-1` → **Phishing website**  

## **🛠️ Technologies Used**  
- **Programming Language:** Python  
- **Machine Learning Models:** Logistic Regression, Decision Tree, Random Forest, SVM, etc.  
- **Libraries & Tools:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn  

## **📊 Model Performance & Evaluation**  
The models are evaluated based on key performance metrics such as:  
- **Accuracy**  
- **Precision, Recall, and F1-Score**  
- **Confusion Matrix & ROC Curve**  

## **📌 How to Run the Project**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/lakku153/Network-Security-Project.git
   cd Network-Security-Project
   ```  
2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```    
3. **Test the system with new URLs:**  
   ```bash
   python predict.py --url "http://34.207.147.23:8080/docs"
   ```  

## **📌 Future Enhancements**  
- **Deploy the model as a web-based API** for real-time phishing detection.  
- **Improve model accuracy** by integrating deep learning techniques.  
- **Expand the dataset** to enhance detection capabilities for evolving phishing tactics.  

## **📄 License**  
This project is open-source and available under the **MIT License**.  

## **📬 Contact**  
For queries or collaborations, feel free to reach out via **[GitHub Issues](https://github.com/lakku153/Network-Security-Project/issues)**.  
