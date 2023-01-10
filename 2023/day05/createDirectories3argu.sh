#!/bin/bash

for (( i=$2;i<=$3;i++))
do
        mkdir $1-$i
done

ls


# in this script you have to write 3 arguments i.e bash createDirectories3argu.sh movie 1 20
