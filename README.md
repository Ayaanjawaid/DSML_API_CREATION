# 🏦 Loan Approval Prediction API

This is a simple Flask-based API that predicts loan approval status using a pre-trained machine learning model (`classifier.pkl`). The model takes basic applicant information and returns whether the loan is **Approved** or **Rejected**.

---

## 📦 Requirements

- Python 3.x  
- Flask  
- scikit-learn  
- pickle (standard library)

Install dependencies using:

```bash
pip install flask scikit-learn

🧪 Testing with Postman
You can test the  endpoint using Postman:
1. 	Set method to POST
2. 	URL: http://127.0.0.1:5000/predict
3. 	Body → raw → JSON:

{
  "Gender": "Female",
  "Married": "No",
  "ApplicantIncome": 3000,
  "LoanAmount": 150,
  "Credit_History": 0
}

📌 Notes
• 	The model expects numerical inputs derived from categorical values:
• 	: Male → 0, Female → 1
• 	: Yes → 1, No → 0
• 	Ensure  is present in the same directory.

🧠 Author
Made by Ayan — passionate about data analytics, storytelling, and building intelligent applications.
