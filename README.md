Using a dataset on house prices in the US, I built a linear regression model to predict house prices w.r.t. their size. 

I first loaded in my dataset and extracted the relevent columns. I could then visualise the data to determine any trends. Next I begun training my model, before running my test set through the model to generate price predictions. These predictions could be easily visualised using pyplot, so I could analyse my results and discuss their meaning. 

Conclusions:
The general trend is as expected - as size increases so does price. We see growth of around $1m for every 500 ft^2, although this growth only increases as we reach larger floor areas. Of course, house price is determined by much more than simply surface area, with factors like location, utilities, garden, etc all being important. Therefore, this model could either be:
1. used to set a 'baseline' price for a property, before that price is then adjusted according to other paremeters
2. updated to include these parameters sourced from larger datasets, to provide a more accurate representation of house price
