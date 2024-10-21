import requests
import json

class GitHub:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"
    
    def getUser(self, userName):
        response = requests.get(self.api_url + '/users/' + userName)
        # print(response.text)

        #same
        # result = json.loads(response.text)
        # return result

        #same
        return response.json()

    def getRepositories(self, userName):
        response = requests.get(self.api_url + '/users/' + userName + '/repos')
        #print(response.text)
        return response.json()
    
    def createRepository(self):
    #     #Old Version
    #     response = requests.post(self.api_url + '/user/'+ '/repos?access_token=' + self.token, json={
    #         "name":"Hello-World",
    #         "description":"This is your first repo!",
    #         "homepage":"https://mehmetnuribasa.com",
    #         "private":False,
    #         "is_template":True
    #         })

        #New Version
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        data = {
            "name": "Hello-World",
            "description": "This is your first repo!",
            "homepage": "https://mehmetnuribasa.com",
            "private": False,
            "is_template": True
        }
        
        response = requests.post(self.api_url + '/user/repos', headers=headers, json=data)
        
            
        return response.json()
    
    def deleteRepository(self, owner, repository):
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        response = requests.delete(self.api_url + f'/repos/{owner}/{repository}', headers=headers)            
        return response.json()


github = GitHub()
while True:
    choice = input("1-Find User\n2-Get Repositories\n3-Create a New Repository\n4-Delete a Repository\n5-Exit\n")

    if choice == '1':
        name = input("User Name: ")
        result = github.getUser(name)
        print(f"Name: {result['name']}, Public Repositories: {result['public_repos']}, Followers: {result['followers']}")

    elif choice == '2':
        name = input("User Name: ")
        result = github.getRepositories(name)

        print("Repositories:")
        for i in result:
            print(i["name"])

    elif choice == '3':
        result = github.createRepository()
        print(result)

    elif choice == '4':
        name = input("User Name: ")
        repoName = input("Repository name to be deleted: ")

        result = github.deleteRepository(name, repoName)
        print(result)

    elif choice == '5':
        break
    else:
        pass
