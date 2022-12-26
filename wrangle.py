
#--------------------Importing--------------------#
#Import Packages
#%%
import pandas as pd


#Import Dataset
#%%
swift = pd.read_csv("taylor_swift_spotify.csv")
swift.head()




#--------------------Data Wrangling--------------------#

#Drop Uneccessary Columns
#%%
swift.drop(["id", "uri", "Unnamed: 0"], axis=1, inplace=True)


#Convert release_date from object to datetime
#%%
swift["release_date"] = pd.to_datetime(swift["release_date"])
swift.release_date.info



#Convert our song duration from milliseconds to minutes in a new column
#%%
swift["duration_min"] =  round((swift["duration_ms"] / 1000) / 60, 2)


# #Commented out duration_ms drop so we can use and compare it's significance later
# #%%
# swift.drop("duration_ms", axis=1, inplace=True)





#--------------------Data Exploration--------------------#

#View Initial Stats for all variables
#%%
swift.describe()


##Things to notice and explore further
    # 1. Instrumentalness min and 25% is 0.000
    # 2. Popularity has a min of 0

#%%
swift.loc[swift["instrumentalness"] == 0]
#While instrumentalness has 0 score for these, popularity varies as do other variables
#I think we should keep these in since it may play a role


#Let's explore popularity
swift.loc[swift["popularity"] == 0]
#It appears that a majority of these songs are either karaoke or voice memo versions
#We should remove these since it will affect our statistical analysis and ML models




#Create new variable dropping songs with popularity of 0
#%%
swift1 = swift.loc[swift["popularity"] != 0]
swift1.shape

#Comparing the shape to ensure we made a change
#%%
swift.shape


#Verifying our songs with 0 popularity were removed
#%%
swift1.loc[swift["popularity"] == 0]




#Correlation Matrix to see correlation between our variables
#%%
swift1.corr()




#--------------------Preparing for Statisticalk Modeling--------------------#
####
## Dependent Variable = Popularity
##IV = (acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, 
#valence, duration_min release_year, release_month, Track Number, 
#(if the name is in the title of the album or if it's not))


#Export file as csv for stats use in R
#%%
# swift1.to_csv(r'/Users/michaelwilt/Desktop/taylorSwiftProject/forStats.csv', index=False)