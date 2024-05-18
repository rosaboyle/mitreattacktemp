import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


from data_extraction import texts
from mitretable import mitre_attack_matrix
mitr_str = str(mitre_attack_matrix)
news = "\n\n".join(texts)
prompt = f"""# Character
You're a data analyst dedicated to identifying specific hunting patterns through text analysis for real-time threat detection purposes.

## Skills
### Skill 1: Extract Hunting Actions
- Analyze the textual data, identify and extract specific hunting actions that could be potentially automated for real-time threat detection. 
- Utilize text analysis algorithms to systematically identify and extract the relevant hunting actions. 

## Constraints:
- Do not consider images for this analysis, focus only on the textual content.
- Automatic real-time detection is of prime importance.
- The goal is to identify threats and alert the necessary parties in real time.
- The hunting actions extracted will strictly adhere to ethical and legal boundaries.
- Maintain the confidentiality and integrity of the data.

**The News Articles and other reports:**
{news}

I want you to generate report directly without any header, preamble or any other information. 
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
with open("hunting_actions.json", "w") as f:
    json_obj = json.loads(response.choices[0].message.content)
    json.dump(json_obj, f, indent=4)
