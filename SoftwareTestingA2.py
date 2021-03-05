from Retire import *
from BMI import *
import string;

def main():
    #initialize container
    s = " ";
    while(s != "Q"):
        print("Please Select a function to use:\n");
        print("Body Mass Index - one\n");
        print("Retirement Calculation - two\n");
        print("Exit - q");

        #force uppercase so that inputs can be uniform
        s = input("Input selection: ");
        s = str(s);
        s = s.upper();
        print("");
        
        #Predict someone will try an integer to select a function
        if(s == "ONE" or s == "1"):
            print("Body Mass Index Selected\n");
            #Get input variables
            height_ft = input("Height in Feet[without inches]: ");
            height_in = input("Remaining Height in inches: ");
            weight_lbs = input("Weight in Pounds: ");
            index = BMI(float(height_ft), float(height_in), float(weight_lbs));
            print(index);
            print("");
            print("");
        elif (s == "TWO" or s == "2"):
            print("Retirement Selected\n");
            #Get input variables
            c_age = input("Current Age: ");
            an_sal = input("Annual Salary[10,000 = 10000]: ");
            p_sav = input("Percentage Saved[20% = .20]: ");
            d_goal = input("Desired Savings Goal[5,000 = 5000]: ");
            goal = Retire(float(c_age), float(an_sal), float(p_sav), float(d_goal));
            print(goal);
            print("");
            print("");
        elif(s != "Q"):
            print("Invalid Selection, Try again\n");
        
    print("Goodbye!");
    
    return 0;
main();
