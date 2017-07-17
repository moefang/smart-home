#!/bin/bash
train_file=..
test_file=..
java -Xms256m -Xmx4096m -cp ./grmm-0.1.3/dist/mallet.jar:./grmm-0.1.3/lib/mallet-deps.jar:./grmm-0.1.3/lib/grmm-deps.jar \
    edu.umass.cs.mallet.grmm.learning.GenericAcrfTui \
    --training train_file \
    --testing  test_file\
    --model-file ./tmpls.txt > stdout.txt 2> stderr.txt
