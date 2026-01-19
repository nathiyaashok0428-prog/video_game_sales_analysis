🎮 Video Game Sales & Engagement Analysis
📌 Project Overview

This project performs an end-to-end Exploratory Data Analysis (EDA) on video game datasets using Python, SQL, and Power BI.
The goal is to clean, merge, store, and visualize video game sales, ratings, and user engagement data to derive meaningful business insights.

🎯 Problem Statement

Raw video game data is available across multiple datasets with:

Missing values

Inconsistent formats

No direct relationships

This makes analysis difficult.
The objective is to:

Clean and standardize the data

Merge datasets for unified analysis

Store cleaned data in SQL

Build interactive Power BI dashboards

📂 Datasets Used
1️⃣ games.csv (Game Metadata & Engagement)
Column	Description
Title	Game name
Release Date	Game launch date
Team	Developer studio
Rating	User rating
Times Listed	Popularity metric
Number of Reviews	Review count
Genres	Game genres
Plays	Total plays
Playing	Active players
Backlogs	Games pending
Wishlist	Wishlisted count
2️⃣ vgsales.csv (Sales Data)
Column	Description
Name	Game name
Platform	Console/PC
Year	Release year
Genre	Game genre
Publisher	Publishing company
NA_Sales	North America sales
EU_Sales	Europe sales
JP_Sales	Japan sales
Other_Sales	Other regions
Global_Sales	Total sales
🏗️ Project Architecture
CSV Files
   ↓
Python (Data Cleaning & Merge)
   ↓
SQL Database
   ↓
Power BI (EDA & Dashboards)

🧹 Data Cleaning & Processing (Python)

Performed using Pandas:

Removed duplicates

Handled missing values

Standardized column names

Converted data types

Merged datasets using game name

Exported cleaned dataset

Scripts:

scripts/
 ├── data_clean_merge.py
 ├── db_pipeline.py

🗄️ Database Design (SQL)

Created tables programmatically

Inserted cleaned data using Pandas to_sql()

Ensured schema consistency

Database:

MySQL / SQLite (local)

Table: video_game_sales

📊 Exploratory Data Analysis (Power BI)
Visuals Implemented:

Bar Charts

Column Charts

Line Charts

Stacked Bar Charts

Scatter Plots

Tables

Matrix (Heatmaps using conditional formatting)

📈 Business Questions Answered (30)
🎮 Game Metadata (games.csv)

Top-rated games

Best developers by rating

Most common genres

Backlog vs wishlist

Release trends

Rating distribution

Most wishlisted games

Average plays per genre

Most productive studios

💰 Sales Analysis (vgsales.csv)

Top sales region

Best-selling platforms

Sales trend by year

Top publishers

Top global games

Regional sales per platform

Platform evolution

Regional genre preference

Yearly regional sales change

Avg sales per publisher

Top games per platform

🔁 Merged Dataset Analysis

Top genres by sales

Rating vs sales correlation

Platforms with high-rated games

Sales & release trend

Wishlist vs sales

High engagement but low sales

Wishlist/backlog vs rating

Engagement by genre

Best genre-platform combinations

Regional genre heatmap

🔥 Key Insights

Action & Sports genres dominate global sales

North America leads game revenue

High wishlist does not always guarantee high sales

User ratings show moderate correlation with sales

Platform performance changes over time

🛠️ Technology Stack
Tool	Purpose
Python	Data cleaning & merging
Pandas	Data manipulation
SQL	Data storage
Power BI	Visualization & dashboards
GitHub	Version control
🚀 Future Scope

Sales forecasting using ML

Advanced DAX measures

Real-time data integration

Recommendation systems

👩‍💻 How to Run the Project
Python
python scripts/data_clean_merge.py
python scripts/db_pipeline.py

Power BI

Load cleaned CSV or SQL table

Build visuals as per EDA questions

Apply filters & conditional formatting

📌 Author

Nathiya
Data Analytics Trainee
Skills: Python | SQL | Power BI | EDA | Data Cleaning
