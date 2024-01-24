/**
 * .function.ts(함수 코드가 포함된 파일) 과 .ts파일(구문이 포함된 파일) 은 같은 경로에 있다.
 * 여기의 구문은 구문 ID 'hello-world-ts', lambda 핸들러 파일이름 'function' 을 사용해서 함수 코드를 찾는다.
 * 즉 함수 코드가 hello-world-ts.my_fctn.ts 라는 파일에 있다고 하면 hello-world-ts.ts 파일은 
 *  const helloFunction = new NodejsFunction(this, 'my_fctn');
 * 이런 함수 코드를 참조해야하는 것
 */

import { Construct } from 'constructs';
// lambda함수를 생성하는 nodejsfunction 구문
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
// restapi 를 생성하는 lambdaRestAPI 구문
import { LambdaRestApi } from 'aws-cdk-lib/aws-apigateway';

export class HelloWorld extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);
    const helloFunction = new NodejsFunction(this, 'function');
    new LambdaRestApi(this, 'apigw', {
        // handler : 함수 핸들러
      handler: helloFunction,
    });
} }