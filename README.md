# Clean Architecture

## Reference
Clean Architecture: A Craftsman's Guide to Software Structure and Design
*Robert C. Martin*
*Kevlin Henney*

[Uncle Bob Blog Post](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)


### Diagram
![Alt text](static/images/clean_architecture_diagram.jpg?raw=true "Clean Architecture Diagram")
### Flow Chart
![Alt text](static/images/clean_architecture_flow_chart.jpeg?raw=true "Clean Architecture Flow Chart")



## Use Cases
------------------
### User Sign In
**input**: name, email, password
**output**: name, email
##### Processing Steps
1. Perform validation of the type of the submitted data.
2. Check if there is any user in the system with the submitted email.
3. If not, create a user in the system and persist it.
------------------
## Commands
#### Run the CLI
``` shell
$ make cli
```

#### Run the Server
``` shell
$ make server
```

#### Make the shell
``` shell
$ make post
```

#### Make an example post request
``` shell
$ make post
```