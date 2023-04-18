#!/bin/bash

result="{ \"files\" : { $(for i in $(find ./features -type f -name "*.feature"); do echo " \"$i\","; done;) } }";
echo $result