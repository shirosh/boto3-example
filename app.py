import boto3, json

# Bedrock Runtime
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)
#models=bedrock_runtime.list_foundation_models().get('modelSummaries')
#print(models)
# Model configuration
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
model_kwargs =  { 
    "max_tokens": 2048, "temperature": 0.1,
    "top_k": 250, "top_p": 1, "stop_sequences": ["\n\nHuman"],
}

# Input configuration
prompt = ""
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "system": "You are a honest and helpful bot.",
    "messages": [
        {"role": "user", "content": [{"type": "text", "text": prompt}]},
    ],
}
body.update(model_kwargs)

# Invoke
response = bedrock_runtime.invoke_model(
    modelId=model_id,
    body=json.dumps(body),
)

# Process and print the response
result = json.loads(response.get("body").read()).get("content", [])[0].get("text", "")
print(result)
