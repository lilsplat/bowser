# course_dists_script.sh

echo "The script starts now"
echo "Hi, $USER!"
echo
echo

# ll = "Language and Literature"
FILE=all_courses_fall2014_dists.txt

s=""
# while IFS='#' read -r line
while IFS= read -r line
do
	val=$line
	sqlite3 bowser_db "insert into courses_course_dists values $val ;"
	echo "inserted $val"
	# echo
	# echo
done < $FILE

echo
# echo $s
# sqlite3 test.db  "insert into n (f,l) values ('john','smith');"
echo "Done"
echo