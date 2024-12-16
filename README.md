# Laptop Price Predictor

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Project Files](#project-files)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

Welcome to the **Laptop Price Predictor** application! This Streamlit-based app is designed to predict the price of a laptop based on its specifications. Whether you are comparing laptops for purchase or simply exploring the market trends, this tool provides quick and reliable price estimations.

---

## Features

### 💡 Key Functionalities:
1. **User-Friendly Interface**:
   - Built using [Streamlit](https://streamlit.io/), the app provides an intuitive interface for entering laptop specifications.
2. **Laptop Specifications Input**:
   - Select or enter specifications like brand, processor, RAM size, storage type, screen size, GPU, and more.
3. **Price Prediction**:
   - Predicts the laptop price using a trained machine learning model.
4. **Real-Time Deployment**:
   - Accessible online, no setup required on the user’s end.
5. **Visual Insights**:
   - Displays how each specification influences the predicted price.

---

## Dataset

The prediction model is trained using a curated dataset containing laptop specifications and prices. The dataset includes features such as brand, processor, RAM, storage, GPU, and screen size, which are critical for accurate price prediction.

---

## Project Files
```
Laptop_Price_Predictor/
|-- data/                     # Dataset for training the model
|-- models/                   # Trained ML models
|-- app.py                    # Main Streamlit application
|-- requirements.txt          # Required Python dependencies
|-- README.md                 # Project documentation
```

---

## How It Works

1. **Data Preprocessing**:
   - Extracted relevant features (brand, processor, RAM, storage, etc.) from the dataset.
   - Cleaned and transformed the data for compatibility with the machine learning model.
2. **Model Building**:
   - Created a regression model using algorithms from `scikit-learn` to predict continuous price values.
   - Serialized the trained model and other required data into `.pkl` files for efficient loading during app usage.
3. **Interactive Application**:
   - Streamlit serves as the frontend interface, where users can input laptop specifications and view predicted prices.

---

## Setup Instructions

### 🔄 Clone the Repository:
```bash
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor
```

### 🚀 Create a Virtual Environment:
```bash
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
```

### 🛠️ Install Dependencies:
```bash
pip install -r requirements.txt
```

### 📝 Run the Application:
```bash
streamlit run app.py
```

Access the app locally at: `http://localhost:8501`

---

### 🌐 Deployed Web-App on Streamlit
You can access the live version of the **Laptop Price Predictor** app [here](https://laptop-price-predictor-app-711.streamlit.app/).

---


## Contributing

Contributions are always welcome! If you have ideas to improve the app or find any bugs, feel free to:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

---

## Acknowledgments

- The dataset used for training the model was curated from publicly available laptop price datasets.
- Special thanks to the Streamlit community for making app deployment so effortless.

---
