# Data Profiling Project

This project is designed to provide a comprehensive data profiling solution using OpenAI, scikit-learn, LangChain, and Streamlit. It allows users to load datasets, perform statistical analysis, train machine learning models, and generate insightful reports.

## Project Structure

```
data-profiling-project
├── src
│   ├── app.py                # Main entry point for the Streamlit application
│   ├── data_profiling.py     # Functions for data profiling and visualization
│   ├── model_training.py      # Functions for training and evaluating machine learning models
│   ├── report_generation.py   # Functions for generating reports using OpenAI and LangChain
│   └── utils
│       └── __init__.py       # Utility functions and constants
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd data-profiling-project
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using `venv` or `conda`.

   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Run the Streamlit application:**
   Navigate to the `src` directory and run the following command:
   ```
   streamlit run app.py
   ```

2. **Data Profiling:**
   Use the data profiling functionalities to load your dataset and generate statistical summaries and visualizations.

3. **Model Training:**
   Train machine learning models using the provided functions in `model_training.py`.

4. **Report Generation:**
   Generate insightful reports based on the data profiling results using the functionalities in `report_generation.py`.

## Overview of Functionalities

- **Data Profiling:** Load data and generate statistical summaries and visualizations.
- **Model Training:** Preprocess data, train models, and evaluate their performance.
- **Report Generation:** Create textual summaries and insights based on data profiling results.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.