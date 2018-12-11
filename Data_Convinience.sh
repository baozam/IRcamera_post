#!/bin/bash

#edit by kazama 2018

chmod 700 *
go="./GOKUCHO_kazama"

frame="150"
run="3043"
rate="60"
I="1"
J="1"

for h in `seq 2`
    do
    if [ $h -eq 1 ] ; then
        echo "Convert"
        mode="0"
    elif [ $h -eq 2 ] ; then
        echo "Max"
        mode="3"
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
        for j in `seq 3`
        do
            if [ $j -eq 1 ] ; then
                echo "Q : heat flux"
                parameter="1"
            elif [ $j -eq 2 ] ; then
                echo "T : temperature"
                parameter="2"
            elif [ $j -eq 3 ] ; then
                echo "H : Thermal conductive"
                parameter="3"
            fi
            a=$(($i+$j))
            echo $i $j $a
            expect -c "
                spawn ./${go}
                expect \"MODE:\"
                send \"${mode}\n\"
                expect \"PARAMETER:\"
                send \"${parameter}\n\"
                expect \"POSITION:\"
                send \"${position}\n\"
                expect \"FRAME:\"
                send \"${frame}\n\"
                expect \"RUN:\"
                send \"${run}\n\"
                expect \"RATE:\"
                send \"${rate}\n\"
                expect \"pixel I:\"
                send \"${I}\n\"
                expect \"pixel J:\"
                send \"${J}\n\"
                interact
            "
        done
    done
done
