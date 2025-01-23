# Project Proposal: Python Program for Psychometric Data Analysis

## Overview
This project focuses on developing a Python-based program to analyze psychometric data collected from mice engaged in a vibrotactile stimulus detection task. The program will process behavioral data stored in `.mat` files and perform signal detection theory (SDT) analyses. 

The program will be designed to receive raw behavioral data from `.mat` files. it will recieve an input of specific day ranges (e.g., Day 19-20) and mouse IDs (e.g., O1, O2). It will output analyzed psychometric data for the selected mice and days. While this project proposal focuses on the program’s preliminary functionality, the tool will ultimately be integrated into the user's broader research efforts as the data set and experimental conditions expand.

## Objectives
1. Develop a Python program capable of analyzing psychometric data from tactile stimulus detection tasks.
2. Automate data processing and analysis, incorporating SDT metrics such as hit rates, false alarm rates, sensitivity (d'), and criterion (c).
3. Lay the groundwork for future program development, which will include analyzing data from optogenetic photoinhibition experiments and supporting additional analytical features.

## Problem Statement and Significance
Understanding how mice perceive and respond to tactile stimuli is crucial for studying sensory processing and decision-making. Current methods for analyzing behavioral data often require manual processing, which can be time-consuming and prone to error. This project addresses these challenges by creating an automated, flexible tool tailored to the user's research needs. The program will streamline psychometric data analysis, ensure accuracy and reproducibility, and enable efficient data processing for large-scale experiments. By automating critical aspects of the analysis, it will free up time for deeper exploration of sensory processing and decision-making in mice.

## Proposed Approach
1. **Data Input:** The program will accept `.mat` files containing raw behavioral data, allowing the user to specify:
   - Day ranges (e.g., Day 19-20).
   - Mouse IDs (e.g., O1, O2).
2. **Data Analysis:** The program will compute key psychometric parameters, including:
   - Hit rate and false alarm rate.
   - Sensitivity (d') and criterion (c) based on SDT.
3. **Output:** The analyzed data will be presented as psychometric curves, highlighting key trends and insights.
4. **Future Development:** While not part of this proposal, the program will later incorporate functionality for analyzing optogenetic data and additional experimental conditions.

