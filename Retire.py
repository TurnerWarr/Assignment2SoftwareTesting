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
