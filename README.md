contaienr: /home

host: /Users/ryan/Desktop/temp

put the index.txt file in the host path (/Users/ryan/Desktop/temp)

docker build -t test01 .

docker run --name=test01 -v /Users/ryan/Desktop/temp:/home test01

after running the above docker command,
the index.txt is virtually under container /home/index.txt
