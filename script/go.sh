#!/bin/bash


function classify(){
    python_file="$1"
    python="/home/haolimin/virtual/venv/bin/python"
    $python $python_file
    echo "classify is done ..."
}


function main()
{
    echo "classifying ..."
    classify classify.py
    echo "The process of classification is over."
}


main
