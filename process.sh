#!/bin/bash
echo "begin process..."
awk -F ',' '$4>=2008 {print $2","$3","$4","$5","$6","$7","$8+$9+$10+$11 > "tv_shows_new.csv" } ' tv_shows.csv
python click_test.py load_data tv_shows_new.csv
echo "counting finish!"
awk -F ',' '$8>=1 {print $2","$3","$4","$5","$6","$7","$8 > "tv_shows_Netflix.csv" } ' tv_shows.csv
python click_test.py load_data tv_shows_Netflix.csv
echo "Netflix finish!"
awk -F ',' '$9>=1 {print $2","$3","$4","$5","$6","$7","$9 > "tv_shows_Hulu.csv" } ' tv_shows.csv
python click_test.py load_data tv_shows_Hulu.csv
echo "Hulu finish!"
awk -F ',' '$10>=1 {print $2","$3","$4","$5","$6","$7","$10 > "tv_shows_Prime.csv" } ' tv_shows.csv
python click_test.py load_data tv_shows_Prime.csv
echo "Prime finish!"
awk -F ',' '$11>=1 {print $2","$3","$4","$5","$6","$7","$11 > "tv_shows_Disney.csv" } ' tv_shows.csv
python click_test.py load_data tv_shows_Disney.csv
echo "Disney finish!"
echo ""

for f in `find . -name "tv_shows_*.csv"`
do
   echo $f
   echo `wc -l $f`
   echo ""
done ;
