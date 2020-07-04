# activity-model
Activity Model of users

Models:
-- User: User Name and Location
-- ActivityPeriod: User activity

View:
-- UserDetail: Get Method to fetch the details

Directions to install docker and docker-compose
#-----------------------------------------------

1. To Download latest docker-compose

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


2. Install procedure for docker ce

https://docs.docker.com/compose/install/

Follow the linux steps

3. start the project

-- clone the repository
-- go to the project folder and run `docker-compose up --build`

4. Project will start at `0.0.0.0:8001`

5. find the result at : `http://0.0.0.0:8001/api/get-user-detail/`

6. To go to the python container to execute management command to insert dummy data
-- docker ps
-- docker exec -it <container-id> sh
-- python manage.py dummydata