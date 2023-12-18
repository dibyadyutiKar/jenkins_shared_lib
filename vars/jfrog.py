import requests
import subprocess

def jFrogUpload():
    url=''
    file_path=''
    username='admin'
    password='U1123456'

    with open(file_path,'rb') as file:
        response=requests.put(url,auth={username,password},data=file)
        
    if response.status_code == 201:
        print("\n PUT request was successful") 
    else:
        print(f"PUT request failed with status code {response.status_code}")  
        print("Response context:")
        print(response.text)  


def main():
    jFrogUpload()

if __name__=="__main__":
    main()

