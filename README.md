# Group-Project-8
#### Project Description: Builds on [Project 5](https://github.com/Group-0/proj5-flask-api.git). Add new endpoint to API that stores data in a Redis database that is running separately from the API (either in another container or another server). This endpoint should implement the four basic CRUD functions using different [HTTP methods](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/):
- `POST /keyval` The CREATE action: this endpoint should rite a new key-value pair into the Redis database
Input payload: `{ "key": "new-key", "value": "new value" }`
Status codes:     200 Success
                  400 Invalid request (i.e., invalid JSON)
                  409 Key already exists
              
- `GET /keyval/<string>` The READ action: this endpoint will retrieve the value associated with the key supplied in the URL.
 Status codes:    200 Success
                  400 Invalid request (i.e., invalid JSON)
                  404 Key does not exist
               
- `PUT /keyval` THE UPDATE action: this endpoint will overwrite the value on an existing key.
Status codes:     200 Success
                  400 Invalid request (i.e., invalid JSON)
                  404 Key does not exist
 
- `DELETE /keyval/<string>` The DELETE action: this endpoint will delete the key (and value) supplied in the URL.
Status codes:     200 Success
                  400 Invalid request (i.e., invalid JSON)
                  404 Key does not exist
                  
### Installation
```
pip install redis
```

### Usage

# Group-Project-9
## Steps
###    Install [Docker Compose](https://docs.docker.com/compose/install/) plugin
###    Create YAML file using Docker [Compose syntax](https://docs.docker.com/compose/compose-file/)

# Group-Project-12
#### Project Description: Construct an automated testing and deployment pipeline using GitHub Actions CI/CD tool that is able to:
- Watch code repo, and automatically trigger when changes are detected
- Run test suite 
- Build new Docker image from the code
- Push Docker image to Docker Hub account
- Deploy the new image to a live environment in GCP that is available to the Internet
- Use GitHub's Encrypted Secrets feature to remove sensitve information from repo
