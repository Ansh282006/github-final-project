#!/bin/bash

# Simple Interest Calculator
# Formula: SI = (P * R * T) / 100

echo "Simple Interest Calculator"
echo "--------------------------"

read -p "Enter principal amount: " principal
read -p "Enter rate of interest (%): " rate
read -p "Enter time period (years): " time

# Calculate simple interest using awk for floating-point math
interest=$(awk "BEGIN {printf \"%.2f\", ($principal * $rate * $time) / 100}")

echo ""
echo "Principal Amount : $principal"
echo "Rate of Interest : $rate%"
echo "Time Period      : $time years"
echo "Simple Interest  : $interest"
