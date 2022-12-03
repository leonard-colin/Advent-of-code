import re

with open("/Users/leonardcolin/code/AdventOfCode/day4/batch_file.txt") as file:
    data = file.read().split("\n\n")

def valid_passports(data):

    valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0
    passports = []
    
    
    for lines in data:
        lines = lines.replace("\n", " ").split()
        passport = {}

        for l in lines:
            k, v = l.split(":")
            passport[k] = v
        passports.append(passport)
            
        
        if all(val in passport.keys() for val in valid_fields):
           valid_count += 1
    return passports

    # return valid_count
    

# def count(passports):

#     valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
#     valid_count = 0

#     for passport in passports:

#         if all(val in passport.keys() for val in valid_fields):
#             valid_count += 1
#     print(valid_count)

    # return valid_count
            
number_of_passports = valid_passports(data)
# print(number_of_passports)
for passport in number_of_passports:
    print(passport['hgt'])

for passport in number_of_passports:
    if 1920 <= passport['byr'] <= 2002 and\
        2010 <= passport['iyr'] <= 2020 and\
        2020 <= passport['eyr'] <= 2030 and\
        (("cm" in passport['hgt']) and (150 <= passport['hgt'] <= 193)) or\
        (("in" in passport['hgt']) and (59 <= passport['hgt'] <= 76)) and\
        passport['hcl'] == r"^#[0-9a-f]{6}$"

#print(number_of_passports)

# for passport in number_of_passports:
#     print(passport)
        
        # print(re.search(r"^#[0-9a-f]{6}$", passport['hcl']))
