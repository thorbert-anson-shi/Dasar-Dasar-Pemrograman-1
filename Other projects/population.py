SECONDS_PER_HOUR = 3600
HOURS_PER_YEAR = 24 * 365
CURR_POPULATION = 307_357_870

birth_rate = SECONDS_PER_HOUR / 7
death_rate = SECONDS_PER_HOUR / 13
immigration_rate = SECONDS_PER_HOUR / 35

yearly_growth = (birth_rate - death_rate + immigration_rate) * HOURS_PER_YEAR

num_of_years = int(input("Number of years: "))

print(num_of_years * yearly_growth)
print(CURR_POPULATION + num_of_years * yearly_growth)
