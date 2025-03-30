# Comparing-Loan-Default-Predictions-Using-Machine-Learning
**A Comparative Approach to Model Selection and Data Balancing Methods**

This repository contains my Master’s Thesis in Business Analytics (University of Kent), focusing on predicting loan default risks using various machine learning algorithms. The main goal is to evaluate and compare the performance of Logistic Regression, Decision Tree, and Random Forest under different approaches to handle imbalanced data, such as cost-sensitive learning, oversampling (SMOTE), and undersampling.

Data file is quire big so if you need the raw data, please contact me.
---

## Table of Contents
1. [Overview](#1-overview)  
2. [Data Description](#2-data-description)  
3. [Methodology](#3-methodology)  
4. [Results](#4-results)  
5. [Repository Structure](#5-repository-structure)  
6. [Key Takeaways](#6-key-takeaways) 
---

## 1. Overview
- **Title**: “Comparing Loan Default Predictions Using Machine Learning: A Comparative Approach to Model Selection and Data Balancing Methods”  
- **Program**: MSc in Business Analytics, University of Kent  
- **Author**: Joseph Do  
- **Supervisor**: Dr. Mingzhe Wei  
- **Word Count**: ~8,800 words  

In this thesis, I explored how different classification models can be used to predict the risk of loan default in a peer-to-peer lending dataset, while highlighting the importance of imbalanced data handling techniques.

---

## 2. Data Description
- **Source**: Public LendingClub loan data (2000–2007), Kaggle.  
- **Size**: ~2 million rows, 19 features after cleaning.  
- **Key Features**:
  - `loan_amnt`, `int_rate`, `annual_inc`, `grade`, `emp_length`, etc.  
  - **Target variable**: `loan_status` (1 = defaulted, 0 = fully paid).  
- **Imbalance**: ~11.7% default vs. ~88.3% non-default.  
- **Preprocessing**:
  1. Data cleaning (removing outliers, missing values).  
  2. Handling categorical features (dummy variables).  
  3. Correlation checks, dropping highly correlated features.  

---

## 3. Methodology
- **Models**: Logistic Regression (LR), Decision Tree (DT), Random Forest (RF).  
- **Handling Imbalanced Data**:  
  - Oversampling (SMOTE, SMOTE + Tomek Links).  
  - Undersampling.  
  - Cost-sensitive Learning (assigning higher weights to minority class).  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score, Specificity, AUC.  
- **Validation**: Train/test split (80:20), 10-fold cross-validation for robustness.

---

## 4. Results
- **Random Forest + Oversampling** achieved the highest metrics (Accuracy ~93%, F1 ~93%, AUC ~0.96).  
- **Decision Tree + Oversampling** also performed well (Accuracy ~88%), but was still behind Random Forest.  
- **Logistic Regression** showed balanced performance but lower scores overall compared to tree-based methods.  
- **Cost-Sensitive** methods can improve certain metrics but require careful calibration of cost values.

**Conclusion**: Properly handling imbalanced data (particularly with SMOTE) and using ensemble methods (Random Forest) significantly improves loan default prediction.

---

## 5. Repository Structure
```plaintext
├── README.md                 # This file
├── Thesis.pdf                # Main thesis document in PDF
├── data/                     # Folder with data or a link to Kaggle
├── Colab_code/               # code notebooks with cleaning data and analysis before using SPSS to run model

## 6. Key Takeaways

1. **Imbalanced Data**  
   - Sử dụng các kỹ thuật như **SMOTE**, **Tomek Links**, và **Cost-Sensitive Learning** giúp mô hình nhận biết tốt hơn các trường hợp thiểu số (vỡ nợ), tăng độ chính xác tổng thể.  
   - Tránh để mô hình “lờ đi” lớp thiểu số, vì chi phí sai lầm (false negatives) trong dự đoán vỡ nợ rất cao.

2. **Model Selection**  
   - **Ensemble Methods (Random Forest)** thường vượt trội so với mô hình đơn lẻ (Logistic Regression, Decision Tree) do khả năng khắc phục overfitting, tăng độ ổn định.  
   - **Decision Tree** đơn giản, dễ giải thích nhưng dễ bị overfitting nếu không được pruning đúng cách.

3. **Metrics**  
   - **Accuracy** có thể gây hiểu lầm trong bài toán lệch nhãn cao, nên xem xét **Precision, Recall, F1-score, Specificity** hoặc **AUC** để đánh giá toàn diện hơn.  
   - Trong dự đoán vỡ nợ, **Recall** (khả năng tìm đúng khách hàng vỡ nợ) thường được ưu tiên.

4. **Practical Implication**  
   - Doanh nghiệp tài chính cần triển khai mô hình phân tích rủi ro sớm để hạn chế phát sinh nợ xấu, nâng cao hiệu quả tín dụng.  
   - Kết quả nghiên cứu cho thấy, kết hợp Machine Learning với các chiến lược cân bằng dữ liệu (ví dụ SMOTE) giúp ngân hàng giảm thiểu rủi ro và ra quyết định cho vay tối ưu hơn.

5. **Future Work**  
   - Mở rộng sang các mô hình Deep Learning hoặc kết hợp kỹ thuật Boosting (XGBoost, LightGBM) có thể mang lại kết quả tốt hơn.  
   - Tập trung xác định chi phí sai lầm (misclassification cost) rõ ràng hơn để áp dụng **Cost-Sensitive Learning** hiệu quả trong bối cảnh thực tế.
