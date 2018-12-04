#########################################################################
# File Name: functions.sh
# Author: Tim Wang
# mail:spookw@foxmail.com
#Created Time:Tue 04 Dec 2018 11:48:02 PM CST
#########################################################################
#!/bin/bash

get_lan_ip () {
    #
    ip addr | \
    ##awk -F'[ $|]+' '//{}'
    ##[ $|]+ means multi seperator and if one charactor come up many times,
    ##    treat as one time
    ##    '//{}' means regular expression between //
        ##  split $3 with seperator . and store every element into array N
        awk -F'[ /]+' '/inet/{
            split($3,N,".")
            if ($3 ~ /^192.168/) {
                print $3
            }
            if (($3 ~ /^172/) && (N[2] >= 16) && (N[2] <= 31)) {
                print $3
            }
            if ($3 ~ /^10\./) {
                print $3
            }
        }'
    return $?
}


