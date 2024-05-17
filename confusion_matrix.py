import numpy as np
from mitretable import mitre_attack_matrix , ground_truth_matrix
# Ground truth matrix
# Predicted matrix
predicted_matrix = mitre_attack_matrix

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

metrics = calculate_metrics(ground_truth_matrix, predicted_matrix)

print("True Positive Rate:", metrics["true_positive_rate"])
print("False Positive Rate:", metrics["false_positive_rate"])
print("False Negative Rate:", metrics["false_negative_rate"])
print("True Negative Rate:", metrics["true_negative_rate"])
print("Confusion Matrix:", metrics["confusion_matrix"])