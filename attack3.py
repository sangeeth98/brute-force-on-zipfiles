import itertools, zipfile, time
import concurrent.futures

def open_zip_file():
    #driver loop for user's .zip file input#
    while True:
        user_input2 = input("\nEnter zip file name: ")
        try:
            #while file exists attempt opening#
            zip_file = zipfile.ZipFile(user_input2)
            return zip_file
        #if file does not exist, print error message#
        except FileNotFoundError:
            print("\nError: File does not exist!")

def brute_force_attack(zip_file):
    '''
    Uses generated product of alphabet from 1-8 to attempt unlocking .zip file
    Returns either true or false, depending if cracking is succesful
    '''
    from itertools import product
    #alphabet string initialized#
    options = 'abcdefghijklmnopqrstuvwxyz0123456789'
    #combos made to range from 1 character to 8#
    for n in range (6,7):
        #generates tuple of strings of products of all letters in alphabet#
        combos = product((options),repeat = n)
        #for loop for each password created#
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(processthread, letters, zip_file) for letters in combos]
            if(True in results): return True
    #returns false if not succesful#
    return False

def processthread(letters, zip_file):
    password = ''.join(letters)
    print(f"current-password - {password}")
    try:
        #attempts unlocking .zip file with each password created#
        zip_file.extractall(pwd=password.encode())
        #prints password if found#
        print("Brute force password is: ",password)
        #returns true if succesful#
        return True
    except:
        return False

def main():
    #prints welcome message and warning to user#
    print("Cracking zip files")
    print("Warning: Cracking passwords is illegal due to the "\
    "Computer Fraud and Abuse Act and has a prison term of up to 10 years!")
    #asks for user's input of file cracking method to be used#
    print('Brute Force Cracking')
    #uses open zip file function#
    brute_zip = open_zip_file()
    #begins timer#
    start=time.process_time()
    print("Brute-force started")
    #uses brute force attack function to attempt unlocking file#
    brute_force_attack(brute_zip)
    #ends timer#
    end=time.process_time()
    print("Brute-force ended")
    #prints amount of time between start time and end time#
    print("Brute Force Elapsed time (sec)",round((end-start),4))
    #closes .zip file#
    brute_zip.close()

if __name__=="__main__": main()