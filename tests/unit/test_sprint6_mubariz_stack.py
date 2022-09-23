import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint6_mubariz.sprint6_mubariz_stack import Sprint6MubarizStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint6_mubariz/sprint6_mubariz_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint6MubarizStack(app, "sprint6-mubariz")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
