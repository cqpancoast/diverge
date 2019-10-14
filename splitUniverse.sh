#!/bin/bash

## UNIVERSE SPLITTER ##
# Queries ANU's QRNG thing and spits out either a zero or a one for no arguments, or if you do supply an argument it takes the huge-ass number mod whatever that is.

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
bigAssNumber=$(python ~/Code/GitHub/qrng/quantumRNG.py)
if (($bigAssNumber < "0"))
	then
	bigAssNumber=$bigAssNumber*-1
fi
echo $(($bigAssNumber % $modBy))

