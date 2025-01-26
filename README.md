# NBA Rookie Classifier Project

This project focuses on building a machine learning model to predict whether a rookie NBA player is worth investing in, based on their statistical performance. The objective is to determine if a player is likely to last more than 5 years in the NBA, providing valuable insights for investors seeking to identify future basketball talents.

## Project Overview

### Dataset
- **File**: `nba_logreg.csv`
- Contains statistical data for NBA rookie players.

### Objective
- Develop a classification model to predict if a player will last over 5 years in the NBA.
- Optimize the model to meet investor needs by minimizing false negatives (maximizing recall).

## Key Steps

1. **Data Preparation and Model Training**
   - Processed and cleaned the dataset.
   - Trained and validated a **classifier** using appropriate statistical and machine learning techniques.
   - Adjusted scoring functions to prioritize recall, ensuring promising players are identified.

2. **Evaluation**
   - Analyzed model performance.
   - Justified metrics and approaches used to align with the project's goal.

3. **API Integration**
   - Deployed the trained classifier as a RESTful API using **Flask**.
   - API accepts player statistics as input and returns a prediction on their potential to last more than 5 years in the NBA.

## Usage

### API
- Endpoint: `/predict`
- Method: `POST`
- Input: JSON object containing player statistics.
- Output: Prediction (`true` or `false`) indicating whether the player is worth investing in.

## Highlights
- Focused on investor-centric metrics and practical implementation.
- Delivered a robust model integrated into a functional REST API for real-world usability.

---

This project provides a data-driven solution for identifying future NBA stars and supporting informed investment decisions.
