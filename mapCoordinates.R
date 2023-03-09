library(tidyverse)
library(sf)
library(mapview)

# Coordinates saved in csv with following structure (dms or dec):
# Name1 12°13'14"S 150°15'E
# Name2 16°17'S  151°18'19"E

coordinates <- read_csv("coordinates.csv", col_names=FALSE)

# Transform dms to dec if necessary
coordinates$lat_dec <- dms2dec(coordinates$X2)
coordinates$lon_dec <- dms2dec(coordinates$X3)

# Map with mapview
mapview(coordinates, xcol = "lon_dec", ycol = "lat_dec", crs = 4269, grid = FALSE, legend = TRUE)
