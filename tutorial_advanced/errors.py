
# try-except 
try:
    1/0
except Exception as e: # general error 
    print(e)

# here everything is fine
print("I am reachable")


filename = "myfile.txt"
logfile = "log.txt"

try:
    with open("filename", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"File {filename} not found: {e}")

# more practical 
# try-except-else-finally
# TODO Virtual environment for correct home directory
try:
    with open("filename", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"File {filename} not found: {e}")
    successfull = False 
else: # there was no except = try was successfull 
    print("File was read successfully!")
    successfull = True 
finally: # runs independently of try/except 
    with open(logfile, "a" ) as log: # a means Append to the file
        if successfull:
            log.write(f"File {filename} was read successfully\n")
        else:
            log.write(f"File {filename} was not read!\n") 



