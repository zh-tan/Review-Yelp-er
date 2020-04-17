# Review-Yelp-er
The Review Yelp-er (Helper) - A Review Generator that creates a review easily! 

A text generation project as part of BT4222 - Mining Web Data for Business Insights. 

Minimum word count restriction has posed to be a problem for writing reviews on User-Generated Content (UGC) platforms such as Yelp. This has hindered many satisfied customers to leave feedback on Yelp. We also had a user story from our very own team member while he was on exchange in the US, where he had a positive experience with Yelp’s and most of the recommendations. However, the need for a minimum word count is a chore for him, be it to give positive or negative reviews. Thus, he ended up not writing reviews for some restaurants just because of the minimum word count and this posed an issue for crowd-sourced review platform as they are unable to ensure accurate and updated reviews on the restaurants as most users do not want to write them.

Hence, we thought that we could use Deep Learning to solve this problem by creating a Review "Yelp-er". By suggesting sentences based on an input, this would help users like our teammate by giving them suggestions and possibly even writing the whole review. 


# Consolidated dataset
Google drive to store our dataset and models as the files are big and can't be be uploaded to github. (https://drive.google.com/open?id=1SwM1IzteNN5q229w_2KE1NFL1CSnj-Hn)

# General Setup
1. Run pip install -r requirements.txt
2. Download dataset and checkpoints from google drive and place it in the instructions specified in the sections
3. If running on local, ensure that CUDA is installed and you have a good GPU

# System Requirements
1. Lots of RAM (At least 20GB)
2. At least 1 GPU
3. Harddisk memory of at least 20GB (3GB for 1 model checkpoint, Yelp Dataset is 5GB before cleaning)

# Data Cleaning
__Objective__ \
To preprocess the dataset, which can be found at https://www.yelp.com/dataset

__Content__
1. Basic NLP Text cleaning
2. Convert from json to csv
3. Inner join business.json and review.json
4. Filter to keep only current open businesses
5. Filter to keep review stars 1 and 5
6. Filter to keep reviews that have more than 1 usefulness rating


# Exploratory Data Analysis
__Objective__ \
To observe the distribution of words between a good review and a bad review. \
View scatterplot at https://zh-tan.github.io/review-yelper.github.io/. \
It takes about 2-5mins to load. 

__Content__
1. Produce scatterplot using scattertext
![](images/scatterplot.jpeg.png) 


# LSTM
__Objective__ \
Train 2 LSTM models on 1 star and 5 star reviews. Note that this is only scoped to food-related reviews.

__Setup__
1. Ensure that the reviews1_cleaned.txt and reviews5_cleaned.txt are in the datafiles folder (lstm_final/datafiles).
2. Code needs to be ran on tensorflow version 1
3. Code has to be ran on colab with 25gb ram (>12 gb ram will be used) and runtime has to be either GPU or TPU.

__Content__
1. Train on food reviews (1 star)
2. Train on food reviews (5 stars)

# GPT-2
__Objective__ \
This is the training phase of GPT-2. Elaborated in our report and presentation, we have decided to train on both general and food models. 

__Setup__
1. Ensure that gpt-2-simple package is installed and you have sufficient RAM and GPU to train the large model
2. Make sure that dataset is in same folder as notebook (GPT-2/)
3. This was trained in Colab with GPU and High RAM (30GB RAM) and Google Cloud Platform (1x P100 GPU and 15GB n1-standard-4 CPUs)
4. Ensure you have at least 10 GB of harddisk space

__Content__ \
Train 2 GPT-2 Large models on Food and General dataset.
1. Trained on General (Review star 1) 
2. Trained on General (Review star 5) 
3. Trained on Food (Review star 1) 
4. Trained on Food (Review star 5) 

__Autoregressive Property__ \
To demonstrate the autoregressive property of GPT-2, we have created Sankey Diagrams where it shows the prediction of the next token for GPT-2. This is important as it helps us understand how the model is predicting for 1 star vs 5 star reviews. 

Review Star 1 \
![](images/review_star_1.gif) \
Review Star 5 \
![](images/review_star_5.gif) \

__PCA on Tensorboard__ 
![](images/tensorboard_pca_graph.gif) 



# Demo
__Objective__ \
To generate a Proof-of-Concept using the trained GPT-2 models, we created an app that simulates the autocomplete feature. Instead of just suggesting a word, the autocomplete feature is able to suggest 3 sentences based on the input given. 

__Setup__ 
1. Ensure that the checkpoint files are in the checkpoint folder (Demo/checkpoint). Download the files from Google Drive link provided above
![](images/demo_directory.jpeg) 

2. Ensure you are in the directory of the py files and just run main.py
![](images/starting_demo.jpeg) 

__Instructions__ 
1. There are dropdowns for you to select the type of model to use (1 star or 5 star)
2. There is a scale on "complexity", which uses temperature scaling to enable the mode to generate more complex outputs. A higher number results in more flamboyant language. 
3. Key in text
4. Click submit
5. Repeat

__Example__ 
1. You may key in any input you like. Let's say the fish and chips were bad but I do not know how to describe it, let's key in "The fish and chips was"
2. Click on submit and the model will generate 3 suggestions for you to pick
![](images/demo_1.jpeg) 
3. Click on any of the suggestions and the text would autocomplete your input
![](images/demo_2.jpeg) 
4. You may edit the model's suggestion and click on submit once the description is fitting
![](images/demo_3.jpeg) 
5. Repeat until you are satisfied with the length and quality of the review generated

# Contributions
1. Lucas - Data cleaning, Exploratory Data Analysis
2. Adrian - Data cleaning, LSTM modelling
3. Zhe Hao - Data cleaning, Scattertext visualisation, GPT-2 modelling, Sankey Diagrams 
4. Ryan - Demo, Field Study
5. Kai Le - Demo, Field Study
