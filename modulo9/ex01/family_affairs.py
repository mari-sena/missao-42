#!/usr/bin/env python3

família_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

def check_reds(member):
    if família_dupont[member] == 'red':
        return True
    else:
        return False

def find_the_redheads(family_members):
    family_members = list(filter(check_reds, family_members))
    return family_members


print(find_the_redheads(família_dupont))

# filter