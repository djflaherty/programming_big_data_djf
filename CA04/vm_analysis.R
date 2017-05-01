# set workding directory to my local git hub repo
git.dir <- 'C:/Users/deird/programming_big_data_djf/CA04'
setwd(git.dir)

# load in the active days CSV file and set col headings
mydata <- read.csv('active_days.csv', header = TRUE, col.names = c("Day","NbrCommits"))
fix(mydata)

#convert the number of commits to numeric
mydata$NbrCommits <- as.numeric(mydata$NbrCommits)

#create vectors for the days and the number of commits
days <- mydata$Day
commits <- mydata$NbrCommits

# Give the chart file a name
png(file = "barchart_active_days.png")

# Plot the bar chart
barplot(commits,names.arg = days,xlab = "Weekday",ylab = "Number of Commits",col = "blue",
        main = "Active Days",border = "red")

# Save the file
dev.off()