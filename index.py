# container => /home
# host => /Users/ryan/Desktop/temp/
# store index.txt in the host /Users/ryan/Desktop/temp/
f = open("/home/index.txt", "r")
print(f.read())