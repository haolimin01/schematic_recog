#!/bin/bash


function rename()
{
    cd "$1"
    images=($(ls *.jpg))
    index=0
    for element in ${images[*]}
    do
        name=$(printf "%s%04d%s" "P_" $index ".jpg")
        mv $element $name > /dev/null 2>&1
        let index++
    done
    echo "rename $1 is done ..."
}


function gene_label()
{
    cd "$1"
    renamed=($(ls *.jpg))
    rm label > /dev/null 2>&1
    for i in ${renamed[*]}
    do
        echo "`pwd`/$i" >> label
    done
    echo "generate_label $1 is done ..."
}


function gene_train_pos_label()
{
    cd "$1"
    rm -f label > /dev/null 2>&1
    images=(`ls *.jpg`)
    for element in ${images[*]}
    do
        echo "$element 1 0 0 20 20" >> label
    done
    echo "positive label is done ..."
}


function gene_train_neg_label()
{
    cd "$1"
    rm -f label > /dev/null 2>&1
    images=(`ls *.jpg`)
    for element in ${images[*]}
    do
        echo "./negative/$element" >> label
    done
    echo "negative label is done ..."
}


function resize_image()
{
    python_file="$1"
    python="/home/haolimin/virtual/venv/bin/python"
    $python $python_file
    echo "resize image is done ..."
}


function train(){
    cd ..
    opencv_createsamples -vec pos.vec -info ./positive/label -bg ./negative/label -w 20 -h 20 -num 400
    echo "pos.vec is created ..."
    sleep 5
    rm -rf ./xml > /dev/null 2>&1
    mkdir xml
    opencv_traincascade -vec pos.vec -bg ./negative/label -data ./xml -w 20 -h 20 -precalcIdxBufSize 4096  -numPos 200 -numNeg 400 -numStages 21
}


function classify(){
    python_file="$1"
    python="/home/haolimin/virtual/venv/bin/python"
    $python $python_file
    echo "classify is done ..."
}


function main()
{
    (rename ../positive/)
    (rename ../negative/)
    (gene_label ../positive/)
    (gene_label ../negative/)
    (resize_image resize_image.py)
    (gene_train_pos_label ../positive/)
    (gene_train_neg_label ../negative/)
    (train)
    echo "The process of training is over. The result is in xml file."
    sleep 5
    echo "classifying ..."
   # classify classify.py
    echo "The process of classification is over."
}


main
