# Name: Shelby Sash, Danny Barnhouse
# email: sashsk@mail.uc.edu, barnhodw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: November 14,2024
# Course #/Section: IS4010/ 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using Github to execute an API call using JSON
# Brief Description of what this module does: The entry point for the project
# Citations: Stack overflow
# Anything else that's relevant: N/A


from JSONPackage.JSON import *

#main py

def main():
    #instance of NewsAPI
    News_Api = NewsAPI()
   
    # Call APIUtilities & write to csv
    News_Api.APIUtilities()
    News_Api.write_to_csv()

if __name__ == "__main__":
    main()