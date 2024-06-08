
# Billionaire Profile Analyzer

## Description





This project is developed as part of learning how to scrape web data using Python libraries such as `requests` and `json`, and deploying a web application using Streamlit. It leverages `pandas` for data manipulation, `Plotly Express` for data visualization, and `PIL` for image processing. The app visualizes data about billionaires, highlighting their financial status, sources of income, and demographic information.




## Features


- Interactive charts showing distribution by industry and country and other criteria.
- Detailed data tables with filtering options.
- Dynamic histograms based on user-selected criteria.

## Screenshots

![image](https://github.com/abhay702/Forbes_Scraper/assets/106369018/9ad61fdb-a03e-4978-af5e-bd2b9faf9c11)

![image](https://github.com/abhay702/Forbes_Scraper/assets/106369018/d2a5b913-c8c5-4931-93ec-e17be0f20581)

![image](https://github.com/abhay702/Forbes_Scraper/assets/106369018/a2b646ee-c449-4773-9848-f306ef9ca327)

![image](https://github.com/abhay702/Forbes_Scraper/assets/106369018/b81a9581-5e9e-48c9-aa7e-38728c8c4e6e)

## Installation

The requirements can be installed using the following command.
Please ensure that you are working in the right directory, where the project has been clonned.

```bash
  pip install -r requirements.txt

```
    
## Usage


To deploy the app locally, execute the following Streamlit command. Modify the URL as necessary based on your setup:

Please Note:

Make necessary changes in the code (i.e., scripts.ipynb) to ensure that the data is read properly. Adjust or fine-tune the parameters as needed to optimize performance.

```bash
streamlit run main.py

```


## Credits

This project would not have been possible without the following resources:

- **Data Sources**
  - Forbes: Providing the data on billionaires.
  
- **Python Libraries**
  - [Pandas](https://pandas.pydata.org/): For data manipulation.
  - [Streamlit](https://streamlit.io/): For creating the web application.
  - [Plotly Express](https://plotly.com/python/plotly-express/): For interactive data visualization.
  - [Pillow (PIL)](https://python-pillow.org/): For image processing capabilities.
  - [Requests](https://requests.readthedocs.io/en/master/): For making HTTP requests.
  - [Python CSV Module](https://docs.python.org/3/library/csv.html): For reading and writing CSV files.

---
