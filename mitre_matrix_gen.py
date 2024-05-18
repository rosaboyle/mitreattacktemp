import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


from data_extraction import texts
from mitretable import mitre_attack_matrix
mitr_str = str(mitre_attack_matrix)
news = "\n\n".join(texts)
prompt = f"""You are a cybersecurity specialist. Your job is to use the following news articles and then come up with the MITRE ATT&CK Matrix.
**The News Articles:**
{news}

MITRE ATT&CK Matrix:

{mitr_str}

Your response should be a JSON object containing the MITRE ATT&CK Matrix But only the subset of the matrix that is relevant to the given news articles.
"""
response = client.chat.completions.create(
  model="gpt-4o",
  response_format={ "type": "json_object" },

  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": "Generate the output json object based on the given format"}
  ],
  # stream=True
)

# for chunk in response: 
#     print(chunk.choices[0].message['content'])
import json
predicted_matrix = json.loads(response.choices[0].message.content)
json.dump(predicted_matrix, open("predicted_matrix.json", "w"), indent=4)
json.dump(predicted_matrix, open("mitre_matrix.json", "w"), indent=4)
print(predicted_matrix)
