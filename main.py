import requests

def main():
    print("Hello world")
    print("TEST")
    print("TEST2")
    test()
    
def test():
    print("Hellooooo")
    
API_KEY = "12345-ABCDE-67890-SECRETKEY"

def fetch_data_from_api():
    url = "http://example.com/api/data"  # Onveilige HTTP-verbinding
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # Kwetsbare request met geen timeout (kan leiden tot Denial-of-Service)
    response = requests.get(url, headers=headers)
    
    # Geen controle op de statuscode (kan fouten verbergen)
    return response.text

def save_user_password(password):
    # Slecht idee: wachtwoorden worden in platte tekst opgeslagen
    with open("user_passwords.txt", "a") as f:
        f.write(password + "\n")

main()