#!/bin/bash
awk -F ' ' '{if(NF>200){printf $1" ";for(i=2;i<=90;i++){printf $(i)" "};printf "\n"}}' spk2utt > spk2utt_test
awk -F ' ' '{if(NF>200){printf $1" ";for(i=100;i<=NF;i++){printf $(i)" "};printf "\n"}}' spk2utt > spk2utt_enroll
