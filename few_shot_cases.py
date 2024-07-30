few_shot_examples_ask = [
    
# Round 1 | Keyword: Yangtze River
'''
Known information: ["is not a country", "is either a city or a landmark", "is not a city"]
**Key attribute**: "man-made structure" 
**Question**: "Is it a man-made structure?" 
****Reasoning****: 
Man-made vs. Natural: This question helps to differentiate between natural landmarks (e.g., Grand Canyon) and man-made structures (e.g., Eiffel Tower). 
Broad Categories: Man-made structures include a wide range of possibilities (e.g., buildings, monuments), whereas cities are all man-made but represent a different category. 
Even Split: The distinction between natural and man-made provides an even split, maximizing information gain by effectively narrowing down the possibilities based on the answer.
''',

'''
Known information: ["is not a country", "is either a city or a landmark", "is not a city", "not a man-made structure", "is not in North America"]
**Key attribute**: "in Asia" 
**Question**: "Is it located in Asia?" 
****Reasoning****: 
Geographic Focus: Identifying the continent will significantly narrow down the possible natural landmarks. 
Large Landmarks: Asia has several major natural landmarks (e.g., Mount Everest, Great Wall). 
Even Split: Given the global distribution of landmarks, this question will effectively split the remaining possibilities.
''',

'''
Known information: ["is not a country", "is either a city or a landmark", "is not a city", "not a man-made structure", "is not in North America", "is in Aisa", "is in China", "is a river"]
**Key attribute**: "longest river in China"
**Question**: "Is it the longest river in China?"
****Reasoning****: 
Length-Specific Focus: Knowing whether it is the longest river will help confirm or eliminate the Yangtze River.
Major Rivers: The Yangtze River is the longest river in China, followed by the Yellow River.
Effective Split: This question will help confirm or deny one of the most prominent landmarks in China, providing a clear yes/no split.',
''',


# Round 2 | Keyword: Congo
'''
Known information: ["is a country"]
**Key attribute**: "in Europe"
**Question**: "Is this country in Europe?"
**Reasoning**: 
Continental Focus: Knowing the continent will help significantly narrow down the list of possible countries.
Effective Reduction: Europe has many countries, so confirming or eliminating Europe will reduce the search space.
Balanced Distribution: Countries are evenly distributed across continents, providing an effective yes/no split.
''',

'''
Known information: ["is a country", "not in Europe", "not in Asia", "in Africa", "not in Northern Africa", "not in Eastern Africa", "not in Western Africa", "in Southern Africa"]
**Key attribute**: "landlocked country"
**Question**: "Is this country landlocked?"
**Reasoning**:
To further narrow down the possibilities within Southern Africa, I will focus on another well-known country in that region.
Geographical Focus: Knowing whether the country is landlocked will significantly narrow down the possibilities within Southern Africa.
Effective Reduction: There are several landlocked countries in Southern Africa, so confirming or eliminating this will help focus the search.
Balanced Distribution: This provides a clear yes/no split, effectively narrowing down the search.
''',

'''
Known information: ["is a country", "not in Europe", "not in Asia", "in Africa", "not in Northern Africa", "not in Eastern Africa", "not in Western Africa", "in Southern Africa", "not landlocked", "Portuguese is not an official language"]
**Key attribute**: "borders the Indian Ocean"
**Question**: "Does this country border the Indian Ocean?"
**Reasoning**: 
Geographic Focus: Knowing whether the country borders the Indian Ocean can help narrow down the options.
Effective Reduction: There are only a few countries in Southern Africa that border the Indian Ocean.
Balanced Distribution: This question provides a clear yes/no split, effectively narrowing down the search.
 ''',
 
# round 3 | Keyword: Ryan 
'''
Known information: ["not is a place", "is a person"]
**Key attribute**: "a historical figure"
**Question**: "Is this person a historical figure?"
**Reasoning**:
Time Frame: Identifying whether the person is historical can significantly narrow down the possibilities.
Effective Reduction: This helps focus on either historical or contemporary figures.
Balanced Distribution: This question provides a clear yes/no split, guiding the search effectively.
''',

'''
Known information: ["not is a place", "is a person", "is a historical figure", "is involved in the entertainment industry.", "is not primarily known for their work in music.", "is primarily known for their work as an actor.", "has not won an Academy Award (Oscar)."]
**Key attribute**: "primarily known for television work"
**Question**: "Is this person primarily known for their work in television?"
**Reasoning**:
Medium Focus: Identifying whether the person is known for television can help narrow down the possibilities.
Effective Reduction: This helps distinguish between actors primarily known for television versus those known for film.
Balanced Distribution: This question provides a clear yes/no split, effectively guiding the search.
'''

'''
Known information: ["not is a place", "is a person", "is a historical figure", "is involved in the entertainment industry.", "is not primarily known for their work in music.", "is primarily known for their work as an actor.", "has not won an Academy Award (Oscar).", "is not primarily known for their work in television.", "is primarily known for their work in action movies.", "is associated with a major action movie franchise."]
**Key attribute**: "known for science fiction action movies"
**Question**: "Is this person known for their work in science fiction action movies?"
**Reasoning**:
Genre Specificity: Identifying whether the person is known for science fiction action movies can help narrow down the possibilities.
Effective Reduction: This helps distinguish between different types of action movie genres, such as sci-fi, fantasy, or military.
Balanced Distribution: This question provides a clear yes/no split, guiding the search effectively.
''',

# round 4 | Keyword: Noosa
'''
Known information: ["is not a person", "is a place", "is not a country", "is a city"]
**Key attribute**: "a capital city"
**Question**: "Is it a capital city?"
**Reasoning**:
Geographic Focus: This question helps determine if the city is a capital, significantly narrowing the possibilities.
Effective Reduction: If the answer is yes, it focuses on capital cities, eliminating all non-capital cities. If no, it eliminates all capital cities from consideration.
Context Relevance: Knowing whether the city is a capital helps tailor subsequent questions to specific types of cities.
Balanced Distribution: Capital cities are a smaller subset of cities, providing an effective yes/no split.
''',

'''
Known information: ["is not a person", "is a place", "is not a country", "is a city", "is not a capital city", "is in the Southern Hemisphere."]
**Key attribute**: "in the Southern Hemisphere"
**Question**: "Is this city in the Southern Hemisphere?"
**Reasoning**:
Hemispheric Focus: This question splits the world into two large, nearly equal parts, effectively narrowing down possibilities.
Effective Reduction: If the answer is yes, it narrows the focus to cities in the Southern Hemisphere, eliminating those in the Northern Hemisphere. If no, it focuses on Northern Hemisphere cities.
Balanced Distribution: The Earth is divided evenly by the equator, providing a clear yes/no split that maximizes information gain.
''',


'''
Known information: ["is not a person", "is a place", "is not a country", "is a city", "is not a capital city", "is in the Southern Hemisphere", "not in Africa.", "not in South America.", "is in Australia or Oceania", "in Australia", "is a coastal city."]
**Key attribute**: "a well-known tourist destination"
**Question**: "Is this city a well-known tourist destination?"
**Reasoning**:
Tourism Focus: This question helps determine if the city is popular with tourists, which can narrow down the list of coastal cities.
Effective Reduction: If the answer is yes, it focuses on well-known tourist cities, eliminating less-known cities. If no, it narrows down to less-touristic coastal cities.
Context Relevance: Many of Australia's coastal cities are also popular tourist destinations, making this an important distinction.
Balanced Distribution: Tourist versus non-tourist cities provide a clear yes/no split.
''',

'''
Known information: ["is not a person", "is a place", "is not a country", "is a city", "is not a capital city", "is in the Southern Hemisphere", "not in Africa.", "not in South America.", "is in Australia or Oceania", "in Australia", "is a coastal city", "is a well-known tourist destination", "is not Gold Coast", "is not in New South Wales", "is in Queensland", "is not associated with the Great Barrier Reef"]
**Key attribute**: "popular for its beaches"
**Question**: "Is this city popular for its beaches?"
**Reasoning**:
Tourism Focus: Identifying if the city is known for its beaches can help narrow down the possibilities.
Effective Reduction: If the answer is yes, it focuses on coastal cities popular for their beaches, eliminating inland cities or those known for other attractions. If no, it narrows down to other types of tourist destinations.
Context Relevance: Many coastal cities in Queensland are known for their beaches, making this a significant distinction.
Balanced Distribution: Coastal versus inland tourist destinations provide a clear yes/no split.
''',

'''
Known information: ["is not a person", "is a place", "is not a country", "is a city", "is not a capital city", "is in the Southern Hemisphere", "not in Africa.", "not in South America.", "is in Australia or Oceania", "in Australia", "is a coastal city", "is a well-known tourist destination", "is not Gold Coast", "is not in New South Wales", "is in Queensland", "is not associated with the Great Barrier Reef", "popular for its beaches"]
**Key attribute**: "located on the Sunshine Coast"
**Question**: "Is this city located on the Sunshine Coast?"
**Reasoning**:
Regional Focus: Identifying if the city is on the Sunshine Coast can significantly narrow down the possibilities.
Effective Reduction: If the answer is yes, it focuses on cities on the Sunshine Coast, eliminating cities in other coastal regions of Queensland. If no, it narrows down to other coastal areas.
Context Relevance: The Sunshine Coast is known for its beach destinations, making this a significant distinction.
Balanced Distribution: This question provides a clear yes/no split, effectively guiding the search.
'''
]

# testing Regular Expression based response parse
test = '''
**Key attribute** "located on the Sunshine Coast"
**Question**: "Is this city located on the Sunshine Coast?"
'''

import re
import random

for example in random.sample(few_shot_examples_ask, 6):
    print(example)

pattern = re.compile(r'\*\*([^*]+)\*\*:?\s*(.*?)(?=\*\*|$)', re.DOTALL)
for k, v in pattern.findall(test.lower()):
    print(k)
    print(v.strip())