# CSV to Database - AWS LAMBDA

## 💻 About the project
This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. This function converts a standard CSV file into database records inside AWS ecosystem using PostgreSQL.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

### 🛠 Technologies

The following tools were used in building the project:

- **[Python (Vanilla)](https://www.python.org/)**
- **[PostgreSQL](https://www.postgresql.org/)**
- **[SQLAlchemy (ORM)](https://www.sqlalchemy.org/)**
- **[AWS Lambda](https://aws.amazon.com/en/lambda/)**
- **[AWS S3](https://aws.amazon.com/en/s3/)**
- **[AWS RDS](https://aws.amazon.com/en/rds/)**
- **[AWS CloudWatch (for debugging)](https://styled-components.com/)**

## ⚙️ Data Conversion
	
|CSV Column  |	Database Column
| ----------- | ---------------   
|	      | ID_CESSAO
|Originador	|ORIGINADOR
|Doc Originador|	DOC_ORIGINADOR
|Cedente	|CEDENTE
|Doc Cedente	|DOC_CEDENTE
|CCB	|CCB
|Id	|ID_EXTERNO
|Cliente	|CLIENTE
|PF/CNPJ	|CPF_CNPJ
|Endereço	|ENDERECO
|CEP	|CEP
|Cidade	|CIDADE
|UF	|UF
|Valor do Empréstimo	|VALOR_DO_EMPRESTIMO
|Parcela R$|	VALOR_PARCELA
|Total Parcelas	|TOTAL_PARCELAS
|Parcela	|PARCELA
|Data de Emissão	|DATA_DE_EMISSAO
|Data de Vencimento	|DATA_DE_VENCIMENTO
|Preço de Aquisição	|PRECO_DE_AQUISICAO


## 🚀 How to deploy the project into your own AWS

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

### Prebuild
To build and deploy your application for the first time, run the following in your shell:

```bash
# Clone this repository
$ git clone git@github.com:edufvicentini/aws-lambda-csv-to-database.git

# Access the folder in terminal
$ cd aws-lambda-csv-to-database

# Install all requirements (needed to preload the modules inside AWS)
$ pip install -r ./api/requirements.txt --target=./api --no-user

# Execute the SAM deploy (switch to sam-cmd if you are using gitbash)
$ sam deploy --guided
```

Inside --guided, you will answer the following:
* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Environment Variables
In your function, please use these following environment variables, in order to establish connection with the database:
```bash
  DB_HOST	       # your database host (or URI)
  DB_NAME	       # your database name (default = postgres)
  DB_PASSWORD	 # your database password
  DB_PORT	       # your database port (default = 5432)
  DB_USERNAME	 # your database user
```
