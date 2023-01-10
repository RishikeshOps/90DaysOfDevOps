#!/bin/bash

for (( i=1;i<=$2;i++))
do
        mkdir $1-$i
done

ls


#when youb run this script you have to write 2 arguments after filename i.e bash createDirectories.sh day 90
