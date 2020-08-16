#!/bin/bash

for file in *.vcf
do

python3 vcf_to_csv.py $file >> total.csv

done