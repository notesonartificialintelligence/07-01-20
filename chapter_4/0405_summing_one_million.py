#Gabriel Abraham
#notesonartificialintelligence
#Make a list of the numbers from one to 1M, then use min() and max() to ensure the list actually starts 
#at 1 and ends at 1M, then use sum()

#List Comprehension
million_list = [value for value in range(1,1_000_001)]

summ_of = sum(million_list)
min_of = min(million_list)
max_of = max(million_list)

print(f"The sum of 1 - 1M is: {summ_of}")
print(f"The smallest value in our Million List is: {min_of}")
print(f"The largest value in our Million List is: {max_of}")