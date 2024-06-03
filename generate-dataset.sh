#!/bin/bash

generate_number() {
    od -An -N4 -tu4 /dev/urandom | tr -d ' '
}

generate_ascii() {
	head -c 75 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 100
}


filename=$1
num_iterations=$2


# Concatenate the output and write to the file
for ((i = 0; i < num_iterations; i++)); do
	number1=$(generate_number)
	number2=$(generate_number)
	ascii=$(generate_ascii)
	echo "${number1} ${number2} ${ascii}" >> $filename
done