#!/bin/bash

#edit by kazama 2018

chmod 700 *
go="python graph_create.py"

frame="150"
run="3043"


for h in `seq 3`
    do
    if [ $h -eq 1 ] ; then
        echo "Q : Heat Flux"
        parameter="0"
    elif [ $h -eq 2 ] ; then
        echo "T : Temperature"
        parameter="1"
    elif [ $h -eq 3 ] ; then
        echo "H : Thermal Conduction"
        parameter="2"
    fi
    for i in `seq 2`
        do
        if [ $i -eq 1 ] ; then
            echo "Front"
            position="0"
        elif [ $i -eq 2 ] ; then
            echo "Back"
            position="1"
        fi
        expect -c "
            spawn ${go}
            send \"${parameter}\n\"
            send \"${run}\n\"
            send \"${position}\n\"
            send \"${frame}\n\"
            interact
        "
    done
done
