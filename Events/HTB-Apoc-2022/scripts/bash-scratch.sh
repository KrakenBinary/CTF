
for file in /home/krakenbinary/Downloads/Logs*
do
  cmd strings "$file" >> results.out
done
