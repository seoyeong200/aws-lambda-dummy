// lambda 함수 코드
// import : @types/aws-lambda에서 유형 정의 가져옴. https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda

import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';
export const handler = async (event: APIGatewayEvent, context: Context):
 Promise<APIGatewayProxyResult> => {
    console.log(`Event: ${JSON.stringify(event, null, 2)}`);
    console.log(`Context: ${JSON.stringify(context, null, 2)}`);
    return {
        statusCode: 200,
        body: JSON.stringify({
            message: 'hello world',
        }),
}; };