import string;

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
