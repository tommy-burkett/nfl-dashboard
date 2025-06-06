# NFL Dashboard
This project uses National Football League data to create an interactive dashboard that visualizes key NFL team statistics across multiple seasons. Even though there are many categories under season statistics, this project emphasizes offensive and defensive performances during the 17-game regular season. The National Football League, or sports in general, are increasingly becoming data-centered, with individual and team performances at the forefront. Teams and analysts use these statistics for game plans, player analysis, and predictions. This dashboard will provide users with an organized and simplified interface to visually represent these performances.  
 
The visualizations in this dashboard allow for quick and easy comparisons between teams across each of the last five seasons, saving fans, like me, from having to scroll through dense and disorganized spreadsheets. Additionally, for those who play Fantasy Football each season, this interactive dashboard will highlight teams that perform well offensively, which will help guide you through your fantasy draft and in-season trades. Further, through these visualizations, users can uncover team trends and patterns due to the project’s five-year data range. Lastly, this project prioritizes reproducibility, so this dashboard will be updated at the end of each season, always displaying the previous five-year interval. 

The data utilized for this project consists of National Football League play-by-play data summed up across an entire 17-game season. This data was aggregated by Pro Football Reference, which is a reliable website for NFL data. Each row in the dataset represents one of the 32 NFL teams for that season. Link to data source: https://www.pro-football-reference.com/ 

---
#### Files Included
`data/` 
- This folder contains two separate folders. The first `input_data/` folder holds Offensive and Defensive NFL season statistics from 2020-2024, directly downloaded from the aforementioned data source. The `cleaned_data/` folder holds the cleaned and combined statistics from the five NFL seasons. The cleaned data is then used to create the dashboard.  

`src/`
- This folder contains the `preprocessing.py` and `dashboard.py` files. The `preprocessing.py` file cleans the raw data gathered and returns the clean data found in the `data/cleaned_data/` folder. The `dashboard.py` file has the source code for creating and formatting the dashboard.

`writeup/`
- This folder contains a six page PDF file that outlines the overall project goals, the data and methods used, a demonstration of the dashboard, and the references utilized to create this project.

`main.py`
- The file used to run the app.
---
#### How to Run the Dashboard
- Open the repository through GitHub Desktop or clone it to your terminal
- CD the directory in your terminal 
- To launch the dashboard, run `"python main.py"` in your terminal. The app should then be available at http://127.0.0.1:8050/

