#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    """Create a PDF report with a given file name, title, and paragraph"""
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)
    report_info = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, empty_line, report_info])
