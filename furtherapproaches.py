mitre_attack_matrix = {
    "Reconnaissance": {
        "techniques_count": 10,
        "techniques": [
            {
                "name": "Active Scanning",
                "description": "Actively scanning victim infrastructure for vulnerabilities and exploitable services.",
                "subcategories": [
                    {"name": "Scanning IP Blocks", "description": "Identifying active IP addresses by scanning large address spaces."},
                    {"name": "Vulnerability Scanning", "description": "Using automated tools to detect vulnerabilities in the victim's infrastructure."}
                ]
            },
            {
                "name": "Gather Victim Host Information",
                "description": "Collecting details about victim hosts, including configuration and software details.",
                "subcategories": [
                    {"name": "Host Fingerprinting", "description": "Identifying host details such as OS, version, and network setup."}
                ]
            },
            ...
        ]
    },
    ...
}
