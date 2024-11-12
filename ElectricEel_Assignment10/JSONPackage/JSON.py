# Name: Shelby Sash, Danny Barnhouse
# email: sashsk@mail.uc.edu, barnhodw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: November 14,2024
# Course #/Section: IS4010/ 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using Github to execute an API call using JSON
# Brief Description of what this module does: Execute an api call, print something interesting from the end point JSON code
# Citations: Stack overflow, Reddit
# Anything else that's relevant: N/A

#json 
import json
import requests
import csv 

#should be architected as a class
class NewsAPI: 
    """
    Interact with NewsApI server to fetch titles and write to csv file
    """
    
    def __init__(self): #constructor
      self.parsed_json = None  

    def APIUtilities(self): 
        #newsapi.org
        
        #submit to api server
        response = requests.get('https://newsapi.org/v2/everything?domains=wsj.com&apiKey=9325db089c73469280e232711f5afbce')
        json_string = response.content
        self.parsed_json = json.loads(json_string) # Now we have a python dictionary -- parsing

        #extract something interesting: The titles of the articles
        print("The titles of the articles are: ")
        for articles in self.parsed_json['articles']:  #iterate over values in articles key
            print (articles["title"])
            
    #write results to csv file
    def write_to_csv(self):
        
        with open('newsArticles.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write headers
            writer.writerow(['Title'])
            # Write data rows
            for articles in self.parsed_json['articles']:
                writer.writerow([articles['title']])
        #print("Data written to 'newsArticles.csv'")

           