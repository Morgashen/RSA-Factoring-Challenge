#!/usr/bin/env python3
"""
Factorize numbers from file into two factors  
"""
import os
import sys
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def get_factors(number):
    """Find two factors for given number"""
    factor = 2
    factors = []
    
    while factor * factor <= number:
        if number % factor == 0:
            factors.append(factor) 
            number //= factor
        else:
            factor += 1

    if number > 1:
        factors.append(number)

    return factors

def main():
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Factorize numbers from file")
    parser.add_argument("infile", help="Input file path")
    parser.add_argument("-o", "--outfile", help="Output file path")
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.infile):
        sys.exit("Error: Input file not found")
        
    if not os.path.isfile(args.infile):
        sys.exit("Error: Invalid input file")    
        
    # Open input and output files
    try:
        with open(args.infile, 'r') as file_in:
            lines = file_in.readlines()
            
        if args.outfile:
            file_out = open(args.outfile, 'w') 
        else:
            file_out = sys.stdout
            
    except FileNotFoundError:
        logging.exception("Cannot open file")  
        sys.exit(1)
        
    # Factorize each number        
    for line in lines:
        num = int(line.strip())
        
        factors = get_factors(num)
        
        if len(factors) == 2:
            factor_str = str(factors[0]) + " * " + str(factors[1])
        else:
            factor_str = str(num)
        
        output = f"{num} = {factor_str}\n" 
        
        print(output.strip())
        
        if args.outfile:
            file_out.write(output)
            
    logging.info("Finished factorizing numbers")
        
if __name__ == '__main__':
    main()
