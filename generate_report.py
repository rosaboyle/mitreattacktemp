import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


from data_extraction import texts
from mitretable import mitre_attack_matrix
mitr_str = str(mitre_attack_matrix)
news = "\n\n".join(texts)
with open("profiling.json", "r") as f:
    threat_actor_profiling = f.read()

with open("hunting_actions.json", "r") as f:
    hunting_actions = f.read()

with open("mitre_matrix.json", "r") as f:
    mitre_matrix = f.read()


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

**Threat Actor Profiling:**
{threat_actor_profiling}

**Hunting Actions:**
{hunting_actions}

**MITRE ATT&CK Matrix:**
{mitre_matrix}


I want you to generate report directly without any header, preamble or any other information. 
"""
response = client.chat.completions.create(
  model="gpt-4o",

  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": "Generate the output report in the markdown format. There should not be any JSON content in the report."}
  ],
)

huge_markdown = response.choices[0].message.content
if huge_markdown.startswith("```markdown"):
    huge_markdown = huge_markdown[len("```markdown"):].strip()
if huge_markdown.endswith("```\n"):
    huge_markdown = huge_markdown[:-len("```\n")].strip()
with open("final_report.md", "w") as f:
    f.write(huge_markdown)

