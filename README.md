# fastapi-user-manager
create something CRUDy


## create user
echo '{"username":"peti","password":"secrethehe","email":"example@asd.com"}' > test.json
curl --header "Content-Type: application/json" -d @test.json http://127.0.0.1:8000/v1/users | jq

## get all users
curl --header "Content-Type: application/json" http://127.0.0.1:8000/v1/users | jq
