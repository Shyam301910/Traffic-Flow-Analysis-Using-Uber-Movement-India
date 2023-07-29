# Introduction
Studies on city layout and traffic patterns have long been of interest to urban planning. Given the growing accessibility of GPS and cell phone data over the past ten years, this interest has grown. Despite the fact that significant work has been done in this field, the GPS taxi trajectory data sets used in early research often only covered very short periods of time, hence a temporal component was infrequently incorporated in traffic flow. Since traffic needs have a dynamic behaviour, urban flow cannot be depicted using simply static metrics. Fortunately, the development of the digital age has led to a huge increase in the amount of knowledge regarding human mobility and location. In this paper, we present a dynamic analysis of the only newly developed and very potent Uber ride data collection, and we apply the findings to predict urban mobility. In order to determine the traffic on the routes that are available, we constructed a number of graphs depending on the connectivity between the various cities. The degree of each and every ward in the city can be used to do this. In order to examine the traffic flow using the retrieved dataset, we also calculated additional crucial metrics like betweenness, closeness, centrality, etc. We have excellent reason to believe that the availability of affordable ride-sharing services like Uber has significantly increased the variety and quantity of people who use cabs as their primary mode of transportation.

# Dataset
Using web scraping, we will use the dataset that was taken directly from the Uber website https://movement.uber.com/?lang=hi-IN.
Uber's data cannot be utilised to immediately construct a graph on which we can identify traffic congestion. Instead, we must create a graph that represents the fundamental city structure upon which trips depend. To depict the proximity of the zones on which Uber accumulates data, we constructed a spatial graph. The data is provided alongside a GeoJSON file(bangalore_wards.json) that details the polygons used to define a city's zones. We were able to load the geometry and generate an adjacency matrix for any two supplied polygons that were contacting one another using the Rgeos and rgdal package. The adjacency matrix obtained from the R algorithm was used to create a graph using pandas, network, and matplotlib.

# Working 
In the pynb file sin_project.ipynb, various social network measures are calculated like Centrality, node degree, Between Centrality, Closeness Centrality, Reciprocity, Density, Complement of the graph, Shortest Path, Diameter of path, Eccentricity, Girvan Newman Algorithm, Clustering, Modularity, Page rank.
All the measures calculated contribute to faster movement and better traffic flow in the city. The graph is also divided into communities for better analysis using Girvan-Newman method. After this, the modularity of the communities of the graph is also calculated. Based on the location of the centroid of the region that each node represents, the visualizations plot the nodes on a map. This enables one to appreciate the basic urban framework on which journeys rely.

