#!/bin/bash

result="{ \"files\" : { "
echo $feature_files
for file in $(find ./features -type f -name "*.feature"); do
    result+=" \"$file\","
done
result+=" } }"
echo $result