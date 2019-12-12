cat input1.txt | awk '{sum+=int($1/3)-2} END {print sum}'
