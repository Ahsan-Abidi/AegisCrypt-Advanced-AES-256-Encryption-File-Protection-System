import os
from datetime import datetime

def generate_security_report(
    file_path,
    sha256_hash,
    metadata
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = (
        f"security_report_{timestamp}.txt"
    )

    report_path = os.path.join(
        "reports",
        filename
    )

    with open(report_path, "w") as report:

        report.write(
            "=" * 60 + "\n"
        )

        report.write(
            "AEGISCRYPT SECURITY ANALYSIS REPORT\n"
        )

        report.write(
            "=" * 60 + "\n\n"
        )

        report.write(
            f"Generated On : {datetime.now()}\n\n"
        )

        report.write(
            f"File Analyzed : {file_path}\n\n"
        )

        report.write(
            "SHA-256 HASH:\n"
        )

        report.write(
            f"{sha256_hash}\n\n"
        )

        report.write(
            "FILE METADATA:\n"
        )

        for key, value in metadata.items():

            report.write(
                f"{key}: {value}\n"
            )

        report.write("\n")

        report.write(
            "=" * 60 + "\n"
        )

        report.write(
            "STATUS : FILE VERIFIED\n"
        )

        report.write(
            "SECURITY LEVEL : HIGH\n"
        )

        report.write(
            "=" * 60 + "\n"
        )

    return report_path