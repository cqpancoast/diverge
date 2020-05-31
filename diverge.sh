#!/bin/bash

modBy=2
if ! [ -z $1 ]
  then
  modBy=$1
fi
if (($modBy < "1"))
        then
        echo "Mod argument must be 1 or above, got:"
  echo $modBy
  exit 1
fi
bigAssNumber=$(python grabANUmeasurement.py)
if (($bigAssNumber < "0"))
  then
  bigAssNumber=$bigAssNumber*-1
fi
echo $(($bigAssNumber % $modBy))

