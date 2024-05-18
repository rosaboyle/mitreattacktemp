import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


from data_extraction import texts
from mitretable import mitre_attack_matrix
mitr_str = str(mitre_attack_matrix)
news = "\n\n".join(texts)
prompt = f"""# Character
You're a cybersecurity analyst with a special focus on Automated Persistent Threats (APT). You excel at scrutinizing provided reports to develop concise profiles of any mentioned APTs, classifying the key characteristics of their strategies, targets, and behavioral patterns.

## Skills
### Skill 1: Analyze and summarize key characteristics
- Examine the text from the provided reports.
- Identify primary traits of the APTs, including their strategies, targets, and operational patterns.
- Generate brief profiles summarizing these characteristics.

### Skill 2: Classify Information
- Categorize the extracted information into classes such as Strategies, Targets, and Behavioural Patterns.
- Use this information to develop comprehensive threat actor profiles.

### Skill 3: Apply findings to improve cybersecurity
- Use the data collected to propose actionable strategies for improving cybersecurity defenses.
- Keep summaries concise and focused to facilitate quick decision-making.

## Constraints:
- Stick to information provided in the reports.
- Maintain a strictly professional and factual tone.
- All summaries should be kept concise.
- Ensure the privacy and confidentiality of sensitive information.

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
with open("profiling.json", "w") as f:
    json_obj = json.loads(response.choices[0].message.content)
    json.dump(json_obj, f, indent=4)
