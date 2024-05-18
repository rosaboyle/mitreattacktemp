import numpy as np
from mitretable import mitre_attack_matrix , ground_truth_matrix
# Ground truth matrix
# Predicted matrix
# from openaiprompt import predicted_matrix # Will timeout due to the API call
import json
with open("predicted_matrix.json", "r") as f:
    predicted_matrix = json.load(f)

def flatten_matrix(matrix):
    flattened = []
    for tactic, tactic_data in matrix.items():
        techniques = tactic_data["techniques"]
        flattened.extend(techniques)
    return flattened

def calculate_metrics(ground_truth, predicted):
    ground_truth_flat = set(flatten_matrix(ground_truth))
    predicted_flat = set(flatten_matrix(predicted))

    true_positives = len(ground_truth_flat.intersection(predicted_flat))
    false_positives = len(predicted_flat - ground_truth_flat)
    false_negatives = len(ground_truth_flat - predicted_flat)
    true_negatives = len(set(flatten_matrix(mitre_attack_matrix)) - ground_truth_flat - predicted_flat)

    total_positives = true_positives + false_negatives
    total_negatives = true_negatives + false_positives

    true_positive_rate = true_positives / total_positives if total_positives > 0 else 0
    false_positive_rate = false_positives / total_negatives if total_negatives > 0 else 0
    false_negative_rate = false_negatives / total_positives if total_positives > 0 else 0
    true_negative_rate = true_negatives / total_negatives if total_negatives > 0 else 0

    confusion_matrix = {
        "true_positives": true_positives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "true_negatives": true_negatives
    }

    return {
        "true_positive_rate": true_positive_rate,
        "false_positive_rate": false_positive_rate,
        "false_negative_rate": false_negative_rate,
        "true_negative_rate": true_negative_rate,
        "confusion_matrix": confusion_matrix
    }

all_subtechniques_predict = set()
all_subtechniques_mitre = set()
for tactic, tactic_item in predicted_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_predict.update(techniques)
for tactic, tactic_item in mitre_attack_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_mitre.update(techniques)

# Make sure this is true else remove the entries that do not exist in the MITRE ATT&CK matrix
remove_entries = []
for tech in all_subtechniques_predict:
    if tech not in all_subtechniques_mitre:
        print(tech)
        remove_entries.append(tech)

for tech in remove_entries:
    for tactic, tactic_item in predicted_matrix.items():
        if tech in tactic_item["techniques"]:
            tactic_item["techniques"].remove(tech)
        # if not tactic_item["techniques"]:
        #     del predicted_matrix[tactic]
    # if tech in all_subtechniques_predict:
    #     all_subtechniques_predict.remove(tech)


all_subtechniques_predict = set()
all_subtechniques_mitre = set()
for tactic, tactic_item in predicted_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_predict.update(techniques)
for tactic, tactic_item in mitre_attack_matrix.items():
    techniques = set(tactic_item["techniques"])
    all_subtechniques_mitre.update(techniques)

# Make sure this is true else remove the entries that do not exist in the MITRE ATT&CK matrix
remove_entries = []
for tech in all_subtechniques_predict:
    if tech not in all_subtechniques_mitre:
        print(tech)
        remove_entries.append(tech)

assert(all_subtechniques_predict.issubset(all_subtechniques_mitre))
metrics = calculate_metrics(ground_truth_matrix, predicted_matrix)

print("True Positive Rate:", metrics["true_positive_rate"])
print("False Positive Rate:", metrics["false_positive_rate"])
print("False Negative Rate:", metrics["false_negative_rate"])
print("True Negative Rate:", metrics["true_negative_rate"])
print("Confusion Matrix:", metrics["confusion_matrix"])