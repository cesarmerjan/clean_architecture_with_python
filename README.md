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
### User Sign Up
**input**: name, email, password
**output**: name, email
##### Processing Steps
1. Receive client data.
2. Persist the data in the system.
3. Inform the client if the sign up was successful.
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