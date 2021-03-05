
import string;
#TODO
def BMI(height_ft, height_in, weight_lbs):
    height_ft = height_ft * 12;
    height_in += height_ft;
    weight_metric = weight_lbs * 0.45;
    height_metric_in = height_in * 0.025;
    height_metric_in = height_metric_in ** 2;
    stepfour = weight_metric / height_metric_in
    stepfour = round(stepfour, 1);
    if(stepfour < 18.5):
        index = "Underweight: ";
        index += str(stepfour);
    elif(stepfour >= 30):
        index = "Obese: ";
        index += str(stepfour);
    elif(stepfour >= 18.5 and stepfour <= 24.9):
        index = "Normal Weight: ";
        index += str(stepfour);
    elif(stepfour >= 25 and stepfour <= 29.9):
        index = "Overweight: ";
        index += str(stepfour);
    return index;

#TODO
def Retire(current_age, annual_salary, perc_save, desired_goal):
    saving = annual_salary * perc_save;
    employ = saving * 0.35;
    saving += employ;
    goal = desired_goal / saving;
    goal = round(goal, 0);
    if(goal + current_age >= 100):
        out = "Goal cannot be met with current parameters ";
        out += str(goal);
    elif(goal + current_age < 100):
        out = "Goal can be met in ";
        out += str(goal);
        out += " years";
    return out;


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
