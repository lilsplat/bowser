# course_dists_script.sh
# NB: THIS SCRIPT MUST BE RUN WHERE BOWSER_DB IS
echo "The script starts now"
echo "Hi, $USER!"
echo
echo

#replace these

#prof m2m
# FILE=all_courses_fall2014_profs.txt
# sqltable=courses_course_professor

#td m2m
FILE=all_courses_fall2014_tds.txt
sqltable=courses_course_timeanddate

s=""
# while IFS='#' read -r line
while IFS= read -r line
do
	val=$line
	sqlite3 bowser_db "insert into $sqltable values $val ;"
	echo "inserted $val"
	# echo
	# echo
done < $FILE

echo
echo "Done"
echo