#A country is big if:
#It has an area of at least three million (i.e., 3000000 km2), or
#It has a population of at least twenty-five million (i.e., 25000000).
#Write a solution to find the name, population, and area of the big countries.
#Return the result table in any order.

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country= (world["area"]>=3000000) | (world["population"]>=25000000)
    output= world.loc[big_country , ["name","population","area"]]
    return output