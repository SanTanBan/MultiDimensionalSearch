import itertools
import matplotlib.pyplot as plt
import numpy as np

# Dichotomous Search
def Dichotomous_Method(expression,distinguishability_constant=0.0001,starting_value=-9999,ending_value=9999,stopping_interval_length=0.001):
    print(expression)
    #print("Dichotomous Search starts here")
    #distinguishability_constant=float(input("Enter the Distinguishability_Constant or calculating criteria of the two internal points within the specified interval"))
    #starting_value=float(input("Enter the starting value of the interval: "))
    #ending_value=float(input("Enter the ending value of the interval: "))
    if ending_value<starting_value:
        starting_value=starting_value-ending_value
        ending_value=starting_value+ending_value
        starting_value=ending_value-starting_value
        print("Since your Ending_Value should be greater than the Starting_Value, they have been interchanged")
    #stopping_interval_length=float(input("Enter the stopping criteria, i.e. the length of the interval after which no evaluations need to take place"))
    if stopping_interval_length<2*distinguishability_constant:
        stopping_interval_length=2*distinguishability_constant
        print("The stopping criteria, i.e. length of the interval required to be achieved, has been updated to twice that of the distinguishability constant so as to ensure the alogorithm stops")
    while(ending_value-starting_value>stopping_interval_length):
        Lambda=((starting_value+ending_value)/2)-distinguishability_constant
        Mu=((starting_value+ending_value)/2)+distinguishability_constant
        expression_at_Lambda = expression.replace('x','('+str(Lambda)+')')
        expression_at_Mu = expression.replace('x','('+str(Mu)+')')
        val_fn_at_Lambda = eval(expression_at_Lambda)
        val_fn_at_Mu = eval(expression_at_Mu)
        if(val_fn_at_Lambda>val_fn_at_Mu):
            starting_value=Lambda
        else:
            ending_value=Mu
        #print("The value of the expression at Lambda=",Lambda," is:",val_fn_at_Lambda)
        #print("The value of the expression at Mu=",Mu," is:",val_fn_at_Mu)
    return (ending_value+starting_value)/2

# SanBan Search
import random
def SanBan_Method(expression,starting_value=-999,another_value=0,ending_value=999,stopping_interval_length=0.0001):
    print("SanBan Search starts here")
    print("For SanBan search, Interval_Start_Value, Interval_End_Value and any random value between the start and end is required")
    #starting_value=float(input("Enter the starting value of the interval: "))
    #ending_value=float(input("Enter the ending value of the interval: "))

    if ending_value<starting_value:
        starting_value=starting_value-ending_value
        ending_value=starting_value+ending_value
        starting_value=ending_value-starting_value
        print("Since the Ending_Value should be greater than the Starting_Value, they have been interchanged")

    if another_value>ending_value or another_value<starting_value:
        another_value=random.random()
        another_value=another_value*starting_value+(1-another_value)*ending_value
        print("The random value between Start and End has been modified")

    middle_value=(ending_value+starting_value)/2
    while (ending_value-starting_value)>stopping_criteria:
        if middle_value>another_value:
            Lambda=another_value
            Mu=middle_value
        else:
            Lambda=middle_value
            Mu=another_value
        expression_at_Lambda = expression.replace('x','('+str(Lambda)+')')
        expression_at_Mu = expression.replace('x','('+str(Mu)+')')
        val_fn_at_Lambda = eval(expression_at_Lambda)
        val_fn_at_Mu = eval(expression_at_Mu)
        if(val_fn_at_Lambda>val_fn_at_Mu):
            return SanBan_Method(expression,starting_value=Lambda,another_value=Mu,ending_value=ending_value,stopping_interval_length=0.0001)
        else:
            return SanBan_Method(expression,starting_value=starting_value,another_value=Lambda,ending_value=Mu,stopping_interval_length=0.0001)
    return middle_value

# Cyclic Co-Ordinate Search
def Cyclic_CoOrdinate_Method(expression,starting_dimensions,stopping_criteria):
    dimensions=starting_dimensions
    for k in starting_dimensions:
        temp_expression=expression
        for i in starting_dimensions:
            if i==k:
                temp_expression = temp_expression.replace(str(i),"x")
            if i!=k:
                temp_expression = temp_expression.replace(str(i),"("+str(starting_dimensions[i])+")")
        print(temp_expression)
        starting_dimensions[k]=Dichotomous_Method(temp_expression)
    # The Stopping Criteria
    stop=1
    for i in starting_dimensions:
        if abs(starting_dimensions[i]-dimensions[i])>stopping_criteria[i]:
            stop=0
    if stop==0:
        return Cyclic_CoOrdinate_Method(expression,starting_dimensions,stopping_criteria)
    elif stop==1:
        return starting_dimensions

# Cyclic Co-Ordinate search with Acceleration Step
def Cyclic_CoOrdinate_with_Acceleration(expression,starting_dimensions_values,stopping_criteria):
    dimensions=starting_dimensions_values
    for k in starting_dimensions_values:
        temp_expression=expression
        for i in starting_dimensions_values:
            if i==k:
                temp_expression = temp_expression.replace(str(i),"x")
            if i!=k:
                temp_expression = temp_expression.replace(str(i),"("+str(starting_dimensions_values[i])+")")
        starting_dimensions_values[k]=Dichotomous_Method(temp_expression)
    # Acceleration Step which is the Summation of all Dimensions
    accelerated_dimension={}
    for i in starting_dimensions_values:
        accelerated_dimension[i]=str("(")+str(starting_dimensions_values[i])+str("+x)")
    temp_expression = expression
    for i in starting_dimensions_values:
        temp_expression = temp_expression.replace(str(i),accelerated_dimension[i])
    x=Dichotomous_Method(temp_expression)
    for i in starting_dimensions_values:
        starting_dimensions_values[i]+=x
    """# Multiple Acceleration Steps # This involves negating all possible combinations of the directions
    number_of_dimensions=len(starting_dimensions_values)
    for h in range(number_of_dimensions):
        S=list(itertools.combinations(starting_dimensions_values, h))
        for j in S:
            accelerated_dimension={}
            for i in starting_dimensions_values:
                if i in j:
                    accelerated_dimension[i]=str("(")+str(starting_dimensions_values[i])+str("-x)")
                else:
                    accelerated_dimension[i]=str("(")+str(starting_dimensions_values[i])+str("+x)")
            temp_expression = expression
            for k in starting_dimensions_values:
                temp_expression = temp_expression.replace(str(k),accelerated_dimension[k])
            x=Dichotomous_Method(temp_expression)
            for k in starting_dimensions_values:
                if i in j:
                    starting_dimensions_values[k]-=x
                else:
                    starting_dimensions_values[k]+=x"""
    # The Stopping Criteria
    stop=1
    for i in starting_dimensions_values:
        if abs(starting_dimensions_values[i]-dimensions[i])>stopping_criteria[i]:
            stop=0
    if stop==0:
        return Cyclic_CoOrdinate_with_Acceleration(expression,starting_dimensions_values,stopping_criteria)
    elif stop==1:
        return starting_dimensions_values

#This is the Main Program

expression="(x1**3-x2)**2+2*(x2-x1)**4" # The input expression is to be entered here
start_dimension={"x1":2.0,"x2":0.0} #Dimensions with the starting values and entered here

final_evaluation=expression
for i in Answer:
    final_evaluation = final_evaluation.replace(str(i),str(Answer[i]))
print("The minimized value is", eval(final_evaluation))
print(Answer)