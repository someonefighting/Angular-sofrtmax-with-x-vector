#!/bin/bash
./filter.py utt2spk wav.scp > wav
./filter.py utt2spk vad.scp > vad
./filter.py utt2spk feats.scp > feats
./filter.py utt2spk text > t
mv wav wav.scp
mv vad vad.scp
mv feats feats.scp
mv t text

