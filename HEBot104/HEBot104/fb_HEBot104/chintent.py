
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username='9c9ee765-0dc6-4ca6-8dcb-07e20e8e93ec',
  password='KzyE8C2nkabs',
  version='2017-05-26'
)

# Replace with the context obtained from the initial request

def check_intent(msg):
	context = {}

	workspace_id = '3e415e30-1e94-4c0d-98db-6d3f3ae30618'

	response = conversation.message(
  	workspace_id=workspace_id,
  	message_input={'text': msg},
  	context=context
	)

	print(json.dumps(response, indent=2))

	text=(response['output']['text'][0])
	return text