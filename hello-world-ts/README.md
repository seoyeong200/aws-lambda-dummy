# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

So deploy the application in the directory that `cdk.json` is located using the `cdk deploy` commnand.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template


## history
init app
`cdk init app --language typescript`

개발 종속성 추가
`npm install -D @types/aws-lambda`

add `lib/hello-world-ts.function.ts`, `lib/hello-world-ts.ts`