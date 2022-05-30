#Python program to delete a file
# importing os library...
import os

# main method 
def main():
    # removing file using remove method 
    os.remove("data.txt")
    print("File 'data.txt' is deleted!")

if __name__=="__main__":main()
