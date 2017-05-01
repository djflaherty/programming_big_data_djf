# set workding directory to my local git hub repo
git.dir <- 'C:/Users/deird/programming_big_data_djf/CA04'
setwd(git.dir)

####################################################################################
#                           Active Days
####################################################################################

# load in the active days CSV file and set col headings
mydata <- read.csv('active_days.csv', header = TRUE, col.names = c("Day","NbrCommits"))
fix(mydata)

#create vectors for the days and the number of commits
days <- mydata$Day
commits <- mydata$NbrCommits

# give the bar chart file a name
png(file = 'barchart_active_days.png')

# plot the bar chart
barplot(commits,names.arg = days,xlab = "Weekday",ylab = "Number of Commits",col = "blue",
        main = "Active Days",border = "red")

# save the file
dev.off()

####################################################################################
#                           Active Hours
####################################################################################

# load in the active hours CSV file and set col headings
mydata <- read.csv('active_hours.csv', header = TRUE, col.names = c("Hour","NbrCommits"))
fix(mydata)

# create vectors for the hours and the number of commits
hours <- mydata$Hour
commits <- mydata$NbrCommits

# give the bar chart file a name
png(file = 'barchart_active_hours.png')

# plot the bar chart
barplot(commits,names.arg = hours,xlab = "Hour",ylab = "Number of Commits",col = "blue",
        main = "Active Hours",border = "red")

# save the file
dev.off()

####################################################################################
#                           Change Totals per Author
####################################################################################

# load in the change totals CSV file and set col headings
mydata <- read.csv('change_totals.csv', header = TRUE)
fix(mydata)

# re-order the columns and drop the first col
mydata <- mydata[c("author", "additions", "deletions","modifications","replacements")]
fix(mydata)

# replace the system generated author name
mydata$author <- gsub('/OU=Domain Control Validated/CN=svn.company.net','System', mydata$author)
fix(mydata)

# create list of authors for the bar chart
authors <- mydata$author

# create legend for the bar chart
totals <- colnames(mydata)
totals <- totals[totals != 'author']

# create colours for the bar chart
colours <- c('green', 'red', 'blue','orange')

# create a matrix for the change totals & then transpose it
vals <- data.matrix(mydata[2:5])
newvals <- t(vals)

# give the stacked bar chart file a name
png(file = "barchart_change_totals.png")

# plot the stacked bar chart with labels perpendicular to x-axis
barplot(newvals,main="Change Totals by Author",names.arg = authors,xlab = "Author",ylab = "Number of Changes",las=2,col = colours)

# add the legend to the chart
legend("topright", totals, cex = 1.1, fill = colours)

# save the file
dev.off()
