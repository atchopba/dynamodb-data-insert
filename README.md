# Overview

Allows to insert data in your [local Dynamodb](https://hub.docker.com/r/amazon/dynamodb-local) based on the PutRequest scripts, presuming that the tables have been created correctly

## Benefits 

* Insert data without stress

* Insert more than 25 items


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

- Rename "init.env" to ".env"
- Edit ".env" file and put the right values.
- Put json in the data folder


### Prerequisites

* Windows 7+ or Linux kernel version 3.10 or higher
* 2.00 GB of RAM
* 3.00 GB of available disk space
* Python 3.7 or higher
* [AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


### Launch the app
```
python app.py
```

Verify the data insert 
```
aws dynamodb scan --table-name table_name --endpoint-url http://host:port
``` 

## License & copyright

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details

Set your account less secure
