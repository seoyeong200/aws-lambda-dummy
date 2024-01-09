import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import { HelloWorld } from './hello-world-ts';

export class HelloWorldTsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    new HelloWorld(this, 'hello-world');

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'HelloWorldTsQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
