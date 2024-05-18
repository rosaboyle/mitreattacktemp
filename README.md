# mitreattacktemp

Instructions to run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Scripts
```bash
python data_extraction.py
python profiling.py # generates profiling.jsion
python hunting_actions.py # generates hunting_actions.json
python mitre_matrix_gen.py # generates mitre_matrix.json
python generate_report.py # Generates report to final_report.md
python generate_pdf.py # Generates PDF final_report.pdf
python confusion_matrix.py # Generates the confusion matrix on the Generated MITRE ATT&CK matrix
```

### Clean everything

```
rm *.json final_report.md
```

### What this repository has:

1. Each part of the code is modularized and made as independent as possible so it can be parallelized easily or can be used in a distributed system.
2. A mechanism to check the accuracy and false positive rates of the MITRE attack matrix if the ground truth is given.
3. Code to create an attack profile of a threat actor in JSON format, which can be eventually used in the further parts of the code.
4. Code to enlist hunting actions of a threat actor in JSON format, which can be eventually used in the further parts of the code.
5. Code to generate the MITRE Attack of a threat actor in JSON format, which can be eventually used in the further parts of the code.
6. Error handling when the MITRE Attack matrix generated is not in the required format.

What this repository lacks but is essential:

1. Error handling
    1. OpenAI errors of token limits, request rates, etc.
    2. OpenAI responses saying it cannot respond because of security and safety reasons.
2. A JavaScript engine to render JavaScript code of a few webpages - Done manually for now.
