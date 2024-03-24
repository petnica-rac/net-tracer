#!/bin/bash

timestamp=$1

python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,12,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,15,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,9,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,9,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,9,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,9,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"

timestamp="2024,03,12,9,11,45"
python3 src/analyze_data/createGraph.py > "test_data/igor5"+$timestamp+".log"
