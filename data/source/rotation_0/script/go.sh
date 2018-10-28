#!/bin/bash


W=20
H=50
function rename()
{
    cd "$1"
    images=($(ls))
    index=0
    path=`pwd`
    file_type=${path##*/}
    case $file_type in
        "positive")
            image_type="p"
            ;;
        "negative")
            image_type="n"
            ;;
        "temp")
            image_type="r"
            ;;
        *)
            image_type=""
            echo "error image path"
            ;;
        esac
    for element in ${images[*]}
    do
        name=$(printf "%s_%04d%s" $image_type  $index ".jpg")
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
        echo "$element 1 0 0 $W $H" >> label
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


function rotation90()
{
    python_file="$1"
    python="/home/haolimin/virtual/venv/bin/python"
    $python $python_file
    echo "rotation operation is done ..."
}


function train(){
    cd ..
    opencv_createsamples -vec pos.vec -info ./positive/label -bg ./negative/label -w $W -h $H -num 600
    echo "pos.vec is created ..."
    sleep 5
    rm -rf ./xml > /dev/null 2>&1
    mkdir xml
    opencv_traincascade -vec pos.vec -bg ./negative/label -data ./xml -w $W -h $H -maxFalseAlarmRate 0.47 -minHitRate 0.999 -precalcIdxBufSize 4096  -numPos 400 -numNeg 800 -numStages 19
}


function classify()
{
    python_file="$1"
    python="/home/haolimin/virtual/venv/bin/python"
    $python $python_file
    echo "classify is done ..."
}


function copy_image()
{
    from="$1"
    to="$2"
    cp $from $to
    echo "copy from $from to $to is done ..."
}


function main()
{
    #(rename ../temp/)
    #(gene_label ../temp/)
    #(rotation90 rotation.py)
    #(copy_image "../temp/*" "../positive/")
    #(rename ../positive/)
    #(rename ../negative/)
    #(gene_label ../positive/)
    #(gene_label ../negative/)
    #(resize_image resize_image.py)
    #(gene_train_pos_label ../positive/)
    #(gene_train_neg_label ../negative/)
    (train)
    echo "The process of training is over. The result is in xml file."
    #sleep 5
    #echo "classifying ..."
    #classify classify.py
    #echo "The process of classification is over."
}


main
