# Api Rest Mutants AWS Core Python FastApi

![GitHub](https://img.shields.io/github/license/dropbox/dropbox-sdk-java)


This project aims to assist Professor Charles Xavier in identifying mutants based on their DNA sequences, in order to recruit them for his school to combat the Sentinels. The API detects whether a person is a mutant by analyzing their DNA sequence.


License: [MIT](License.txt)





## Built With
* `Programming Language`: Python
* `Cloud Services:`
  * AWS Lambda
  * AWS EventBridge
  * AWS API Gateway
* `Database`: MongoDB Atlas

# Getting Started


## Prerequisites

* **Python** [download](https://www.python.org/downloads/) and install python 3.10
* **Mongodb** To use MongoDB, you need to create a database in the MongoDB Cloud. You can sign up for a free version at the following link: 
[MongoDB Atlas Registration](https://www.mongodb.com/cloud/atlas/register),
generate a mongo uri and configure **Network Access**

* Aws, https://aws.amazon.com/ 

### 1. Deploy an EventBridge Service and Create a Rule:
Go to the AWS Management Console and navigate to the "EventBridge" service.
If you haven't created an event bus yet, you can create a new one.
Next, create a new rule.
Configure the event pattern with the following JSON:
json
```
{
  "source": [
    "my-application"
  ],
  "detail-type": [
    "mutant-detected"
  ]
}
```
Define the target action of the rule as a Lambda function that will process the events.
### 2. Create a Lambda Function:
Go to the AWS Management Console and search for the "Lambda" service.
Create a new Lambda function.
Use the code found in the lambda_function folder of your repository as the source code for the Lambda function.
This code should capture the event it receives from EventBridge and send it to the MongoDB Cloud database.


## 🛠️ Setup  

1. Clone the repository:
```bash
git clone https://github.com/ccasllo/mutantes.git
```

2. Install Python Virtual Environment:
```bash
python3 -m venv venv
```

3. Activate the Virtual Environment:
```bash
source venv/bin/activate
```
4. Install Required Packages:
```bash
pip install -r requirements.txt
```
5. configure variables. 
Create a file named `.env` and add the necessary variables following the format provided in `example.env`
```bash
.env
```
and excute .env
```bash
export $(cat .env)
```


6. execute 
```bash
uvicorn config.main:app --reload
```

# Usage

## Run Unit Tests:
  
1. **Assign Execution Permissions to the Script:**
   ```bash
   chmod +x execute_test.sh
   ```
2. **Execute the Unit Tests:**
   ```bash
   sh execute_test.sh
   ```


# Contact
Carlos Castillo 
Project Link: https://github.com/ccasllo/mutantes.git



