#Maks (GROOD) Shkunda
#09.03.2022 - START
#21.03.2022 - END
#------------TEST-----
# 5*2+10
# (6+10-4)/(1+1*2)+1
#---------------------
#---------Joke-------
#There are 10 types of people:who understand binary code and those not
#---------Imoport---------
import os
#--------Function-------
#this function set priority for our Arithmetic operator
def prior():
    global prior_in_list
    global prior_current
    if OpArray[-1] == "*":
        prior_in_list = 2
    elif OpArray[-1] == "/":
        prior_in_list = 2
    elif OpArray[-1] == "+":
        prior_in_list = 1
    elif OpArray[-1] == "-":
        prior_in_list = 1
    else:
        prior_in_list = 0

    if tokenized[i] == "*":
        prior_current = 2
    elif tokenized[i] == "/":
        prior_current = 2
    elif tokenized[i] == "+":
        prior_current = 1
    elif tokenized[i] == "-":
        prior_current = 1
    else:
        prior_current = 0

#This function count what we have
def counting():
    global last_num
    global pre_lust_num
    global res_count
    last_num = int(result_array[ind_of_last_n])
    pre_lust_num = int(result_array[ind_of_last_n-1])
    if outPutArray[0] == "+":
        res_count = pre_lust_num + last_num
    elif outPutArray[0] == "-":
        res_count = pre_lust_num - last_num
    elif outPutArray[0] == "*":
        res_count = pre_lust_num * last_num
    elif outPutArray[0] == "/":
        res_count = pre_lust_num / last_num
#---------END------
#-----------Variable-----
#---------Tokenizer----
number = ['1','2','3','4','5','6','7','8','9','0']
Example = input("What to count:")
untokenize = []
tokenized = []
in_num_1 = False
in_num = False
lol = 0
count_times = 0
#-------Polske_numerovanie---
symbols = ["-","+","*","/","(",")"]
numbers = []
outPutArray = []
OpArray = []
root_in_num = False
prior_in_list = 0
prior_current = 0
#---------Count-------------
result_array = []
res_count = 0
ind_of_last_n = 0
last_num = 0
pre_lust_num = 0

#We split input to elements
#Every elements have own place
for i in range(len(Example)):
    #This command add current element to array with every symbols
    untokenize.append(Example[i])
#Adding . to array this wix bug we will delete it in the end
untokenize.append(".")


roll = 0
#We repeat it how long is this array
for roll in range(len(untokenize)):
    #check is current element in numbers(array)
    in_num = untokenize[roll] in number
    # check is current element in symbols(array)
    in_sym = untokenize[roll] in symbols
    # check is current element a dot that we put in the end
    dot_l = untokenize[roll] == "."
    #we create variable with current element
    char = untokenize[roll]
    #if current element in numbers we go on
    if in_num == True:
        #if lenght of array is bigger than index of current elemen plus 1
        if len(untokenize)>= i+1:
            #we try to do this if we can it will be did
            try:
                #we repeat this infinit times
                while True:
                    #check is next number in number(array)
                    in_num_1 = untokenize[roll+1] in number
                    #we record how many times we did it
                    count_times +=1
                    #if next number in number(array)
                    if in_num_1 == True:
                        #if this is first time we go here
                        if count_times == 1:
                            #we take 2 numbers and add it to ech others
                            char = str(untokenize[roll])+str(untokenize[roll+1])
                            roll +=1
                        #if this time is not first we go here
                        else:
                            #we add to what we have current
                            char = char + str(untokenize[roll+1])
                            roll += 1
                    else:
                        count_times = 0
                        if char in tokenized[-1]:
                            pass
                        else:
                            tokenized.append(char)
                        break
            #if our try is not successful we go here
            except:
                # add to the end corrent element
                tokenized.append(char)
        #if not we go here
        else:
            # add to the end current element
            tokenized.append(char)
    #if current element in symbols
    elif in_sym == True:
        # add to the end current element
        tokenized.append(char)
    #if current element is dot(.)
    elif dot_l == True:
        #add to the end current element
        tokenized.append(char)
    #if current element isn't number or symbol we skip it
    else:
        #skip
        pass
tokenized.pop()


print("---Tokenized---")
print(tokenized)
print("------------")

for i in range(len(tokenized)):
    root_in_symbols = tokenized[i] in symbols
    if root_in_symbols == True:
        brk_in_symbols = "(" in OpArray
        cur_is_cl_brak = tokenized[i] == ")"
        if len(OpArray) == 0:
            OpArray.append(tokenized[i])
        elif tokenized[i] == "(":
            OpArray.append(tokenized[i])
        elif brk_in_symbols == True and cur_is_cl_brak == True:
            OpArray.append(tokenized[i])
            ind_op = OpArray.index("(")
            ind_cls = OpArray.index(")")
            OpArray.remove("(")
            OpArray.remove(")")
            for i in range(ind_cls-2,ind_op-1,-1):
                outPutArray.append(OpArray[i])
                OpArray.remove(OpArray[i])
        elif tokenized[i] == ")":
            OpArray.append(tokenized[i])
        else:
            prior()
            if prior_in_list >= prior_current:
                outPutArray.append(OpArray[-1])
                OpArray.pop()
                OpArray.append(tokenized[i])
            else:
                OpArray.append(tokenized[i])
    else:
        outPutArray.append(tokenized[i])

for i in range(len(OpArray)):
    outPutArray.append(OpArray[-1])
    OpArray.pop()



print("----Numerovanie----")
print(outPutArray)
print("-----------------")

for i in range(len(outPutArray)):
    in_symbols = outPutArray[0] in symbols
    if in_symbols == True:
        ind_of_last_n = result_array.index(result_array[-1])
        counting()
        result_array.remove(result_array[-1])
        result_array.remove(result_array[-1])
        result_array.append(res_count)
        outPutArray.remove(outPutArray[0])
    else:
        result_array.append(outPutArray[0])
        outPutArray.remove(outPutArray[0])

print("-----Result--------")
print(result_array)
print("-----Result--------")