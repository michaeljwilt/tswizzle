
View(swift)

plot <- ggplot(swift, aes(x=tempo))

plot + geom_boxplot()


# Run a linear regression model using:
#DV - Popularity
#IV - acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence, duration_min





###Assumption Testing###

##Normality##
#Saving transformed columns into new df for ease of use

# acousticness
plotNormalHistogram(sqrt(swift$acousticness))
swift$SQacousticness <- sqrt(swift$acousticness)

# danceability
plotNormalHistogram(swift$danceability ^2)
swift$SRdanceability <- swift$danceability ^2

# energy
plotNormalHistogram(swift$energy)

# instrumentalness
swift$LGinstrumentalness <- log(swift$instrumentalness)
swift1 <- NaRV.omit(swift) # Remove all NA values since instrumentalness had 0s to begin with
plotNormalHistogram((swift1$LGinstrumentalness))

# liveness 
plotNormalHistogram(log(swift1$liveness))
swift1$LGliveness <- log(swift1$liveness)

# loudness
plotNormalHistogram(swift$loudness)

# speechiness
plotNormalHistogram(log(swift$speechiness))
swift1$LGspeechiness <- log(swift$speechiness)

# tempo
plotNormalHistogram(swift1$tempo)

# valence
plotNormalHistogram(swift1$valence)

# duration_min
plotNormalHistogram(sqrt(swift1$duration_min))
swift1$SRduration_min <- sqrt(swift1$duration_min)


#Speechiness violates normality so we may exclude it from our model


##Build Model


#Without speechiness
model <- lm(popularity~SQacousticness + SRdanceability + energy + LGinstrumentalness+ LGliveness + loudness + tempo + valence + SRduration_min, data=swift1)
summary(model)


#Findings:
# Tempo, Loudness and Danceability are not significant in determining popularity of a song

# Move forward with: acousticness, energy, instrumentalness, liveness, valence, duration_min

