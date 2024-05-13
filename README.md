# Zimbabwe News Article Clustering

This project uses Scrapy spiders to gather news articles from several Zimbabwean news websites, performs text clustering on the collected data, and presents the clustered articles in a Streamlit web application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setting up the Virtual Environment](#setting-up-the-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Collecting the Data](#collecting-the-data)

## Prerequisites

- **Python:** Ensure you have Python 3.8 or higher installed.
- **Git:** You'll need Git to clone this repository.
- **Virtual Environment (Recommended):** We highly recommend using a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

## Setting Up the Virtual Environment

1. **Create a Virtual Environment:**
   - If you are using `venv`:
     ```bash
     python -m venv env  
     ```
   - If you are using `conda`:
     ```bash
     conda create -n env python=3.8  
     ```
     Replace `env` with your preferred environment name.

2. **Activate the Virtual Environment:**
   - **Linux/macOS:**
     ```bash
     source env/bin/activate
     ```
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```

## Installing Dependencies

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/victoryeovil/news_scrapper.git](https://github.com/victoryeovil/news_scrapper.git)
   cd your-repository
   ```



2. **Install Requirements:**

    ```(env) pip install -r requirements.txt
    ```

# Collecting the Data

1. **Run the Spiders:**
    ```
    scrapy crawl spider_name
    ```
