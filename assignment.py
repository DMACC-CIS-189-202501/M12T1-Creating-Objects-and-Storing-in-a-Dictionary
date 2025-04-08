# TODO 1: Delete this line and put your docstring here



import csv
class County:

    def __init__(self, population):
        # TODO 2: Finish the county Object init
        # Add the required arguments to the constructor  and attributes to the 
        # County class, one attribute for each column in the dataset.
        # Since the final object is a dictionary of type str:County, you can leave out the county name if desired
        # so at a minimum include:
        # per_capita_income, median_household_income, median_family_income,population,number_of_households

        ##### YOUR CODE HERE, one example given #####
        self.population = population
        pass


    def get_population_as_float(self):
        """
        Return the population as a float.
        """
        # Population likely came in as a string with commas in it
        # This will strip commas and convert it to a float
        population_without_commas = self.population.replace(',','')
        population = -1.0
        try:
            population = float(population_without_commas)
        except:
            raise ValueError(f"Failed converting population to float: {population_without_commas}")
        return population

# ---- Note Country object is above this line, now we are onto our main function(s)

def read_csv_to_county_dictionary():
    #Initialize empty dictionary
    counties = dict()

    # Opens the CSV File
    with open("Iowa_2010_Census_Data_Population_Income.csv", newline='') as fcsv:
        # Reads it in using a builtin method
        reader = csv.DictReader(fcsv)
        for d in reader:
            # TODO 3: Write this code to read in the lines; as a hint this is what you did in countyDemos
            # counties[d["county"]] = CountyDemos(d["population"], d["nbr_households"])
            # Note: There is a header row you may or may not need to skip, and 2 rows that does not contain a rank
            # you will want to skip those; something like if rank is equal to None continue else add to counties dict
            
            #Placeholder
            pass

    return counties

def main():
    # Step 1: Read in County data to a dictionary object
    county_dict = read_csv_to_county_dictionary()

    # Step 2: compute the total population for all counties in Iowa
    # Note: as a comparison line 23 has "3,046,355" so your calculation should equal that
    # TODO 4: write the code here or create another function and call it
    # Hint: The County Demos had:
    #    pop_sum = 0
    #    for key in county:
    #       pop_sum += int(dcounties[key].population.replace(',',''))
    #    print(pop_sum)


    # return the population


# Bonus: If you want to push yourself and your understanding; how would you change/modify/create a new function similar to the above that does the median household income instead of total population?

if __name__ == "__main__":
    total_population = main()

    print(f"The total population for the state of Iowa is..............: {total_population}")
    print(f"Our expected value is (it is ok if yours is missing commas): 3,046,355")