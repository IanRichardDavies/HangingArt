#!/bin/bash
conda env create -f environment.yml
conda activate hangingart
python setup.py install
echo HangingArt setup installation finished