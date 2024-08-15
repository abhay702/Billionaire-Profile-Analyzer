

# Billionaire Profile Analyzer

## Description

The Billionaire Profile Analyzer is a web application designed to scrape, analyze, and visualize data about billionaires using Python libraries. This project focuses on understanding the financial status, sources of income, and demographic information of the world's wealthiest individuals.

The app is built with `Streamlit` for deployment, `pandas` for data manipulation, `Plotly Express` for interactive visualizations, and `PIL` for image processing.

## Features

- **Interactive Charts**: Visualize distributions by industry, country, and other criteria.
- **Detailed Data Tables**: Filter and explore data with ease.
- **Dynamic Histograms**: Generate histograms based on user-selected criteria.

## Screenshots

![Distribution by Industry](https://github.com/abhay702/Forbes_Scraper/assets/106369018/9ad61fdb-a03e-4978-af5e-bd2b9faf9c11)
![Distribution by Country](https://github.com/abhay702/Forbes_Scraper/assets/106369018/d2a5b913-c8c5-4931-93ec-e17be0f20581)
![Net Worth Visualization](https://github.com/abhay702/Forbes_Scraper/assets/106369018/a2b646ee-c449-4773-9848-f306ef9ca327)
![Data Table Example](https://github.com/abhay702/Forbes_Scraper/assets/106369018/b81a9581-5e9e-48c9-aa7e-38728c8c4e6e)

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.7 or higher
- pip (Python package installer)

### Cloning the Repository

To get a copy of this project up and running on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/abhay702/Billionaire-Profile-Analyzer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Billionaire-Profile-Analyzer
   ```

3. **Install the Required Dependencies**:

   Install the necessary Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To deploy the application locally, run the following Streamlit command from the project directory:

```bash
streamlit run main.py
```

### Important Notes

- **Data Processing**: Before running the app, make sure to update the data processing scripts (e.g., `scripts.ipynb`) to ensure the data is properly read and processed.
- **Customization**: Modify parameters and configurations as needed to optimize performance based on your local setup.

## Credits

This project was developed with the help of several resources and tools:

- **Data Sources**:
  - [Forbes](https://www.forbes.com/): Providing comprehensive data on billionaires.

- **Python Libraries**:
  - [Pandas](https://pandas.pydata.org/): For data manipulation.
  - [Streamlit](https://streamlit.io/): For creating the web application.
  - [Plotly Express](https://plotly.com/python/plotly-express/): For interactive data visualization.
  - [Pillow (PIL)](https://python-pillow.org/): For image processing.
  - [Requests](https://requests.readthedocs.io/en/master/): For making HTTP requests.
  - [CSV Module](https://docs.python.org/3/library/csv.html): For handling CSV files.

