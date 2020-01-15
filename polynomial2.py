def formater(string):                               #formats the given polynomial to signs(+/-), constant term, and power-coefficient blocks
    string = string.replace("*", "")                #removes the power and multiplication symbols                       OUTPUT: "x^5-5x2+x-1"
    string = string.replace("^", "")                #removes the power symbols                                          OUTPUT: "x5-5x2+x-1"
    strlst, sign, k = [], [], 1
    if string[0].isalnum():
        string = '+'+string                         #adds sign(+/-) to the first term of the polynomial for convinence  OUTPUT: "+x5-5x2+x-1"
        sign.append(1)
    for i in range(1, len(string)):
        if string[i] == '+':                        #If the sign of the term is +
            strlst.append(string[k:i])              #seperates the blocks of polynomial                                 OUTPUT: [x5,5x2,x,1]
            k = i+1
            sign.append(1)                          #seperates the signs of coeffs of polnomial including the const.    OUTPUT: [1,-1,1,-1]
        elif string[i] == '-':                      #If the sign of the term is -
            strlst.append(string[k:i])              #seperates the blocks of polynomial                                 OUTPUT: [x5,5x2,x,1]
            k = i+1
            sign.append(-1)                         #seperates the signs of coeffs of polnomial including the const.    OUTPUT: [1,-1,1,-1]

    return [strlst, sign[:-1], sign[-1]]            #[[blocks of polymonial], [signs of coeffs], constant term] = [['x5', '5x2', 'x'], [1, -1, 1], -1]


def digit(str):                                     #str to int function customized for power(), coeff()
    if str.isdigit():
        return int(str)
    else:
        return str


def power(lst):                                     # creates a list of powers of the individual terms                  INPUT: ['x5', '5x2', 'x']
    powlst = [digit(lst[i][lst[i].find('x')+1:]) for i in range(0, len(lst))]       #takes the number after 'x' as power of the term in each element of the input list
    powlst = [1 if x == '' else x for x in powlst]          #if there's no number after 'x', its taken as 1
    return powlst                                   #                                                                   OUTPUT: [5,2,1]                                                             


def coeff(lst):                                     # creates a list of coeffs of the individual terms                  INPUT: ['x5', '5x2', 'x']
    coefflst = [digit(lst[i][0:lst[i].find('x')]) for i in range(0, len(lst))]      #takes the number before 'x' as coeff of the term in each element of the input list
    coefflst = [1 if x == '' else x for x in coefflst]      #if there's no number after 'x', its taken as 1
    return coefflst                                 #                                                                   OUTPUT: [1,5,2]


def main(string, value=1):
    formatted = formater(string)                    #                                                                   OUTPUT: [['x5', '5x2', 'x'], [1, -1, 1], -1]
    powers = power(formatted[0])                    #                 INPUT: ['x5', '5x2', 'x']                         OUTPUT: [5,2,1]
    coeffs = coeff(formatted[0])                    #                 INPUT: ['x5', '5x2', 'x']                         OUTPUT: [1,5,2]
    signs = formatted[1]                            #                                                                   OUTPUT: [1,-1,1]
    constant = formatted[2]                         #                                                                   OUTPUT: -1
    y = 0
    for i in range(0, len(powers)):
        y += signs[i]*coeffs[i]*(value**powers[i])  #substituting value to the polynomial
    return y+constant                               #adding constant term


print(main("x^5-5x**2+x-1")==-8)


#Order of execution:
#1. main
#    1.1 formater()
#    1.2 power()
#        1.2.1 digit()
#    1.3 coeff()
#        1.3.1 digit()
#    1.4 returns value