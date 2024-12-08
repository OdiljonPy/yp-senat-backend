import gspread
from google.oauth2.service_account import Credentials
from django.utils.html import format_html
from collections import Counter

from exceptions.error_messages import ErrorCodes
from exceptions.exception import CustomApiException


def get_google_sheet_statistics(sheets_id):
    SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("oceanic_catcher_441013_i5_3b73bd78cd58.json", scopes=SCOPE)
    client = gspread.authorize(creds)
    rows = client.open_by_key(sheets_id).sheet1.get_all_values()

    if not rows:
        raise CustomApiException(error_code=ErrorCodes.NOT_FOUND, message='Data not found')

    header, *data = rows
    total_entries = len(data)

    def process_question(i):
        answers_count = Counter(
            map(lambda row: row[i].strip(), filter(lambda r: len(r) > i and r[i].strip(), data))
        )
        return header[i], answers_count

    question_stats = dict(map(process_question, range(1, len(header))))

    # Helper function to generate HTML for each answer
    def format_answer(answer_data):
        answer, count = answer_data
        percentage = (count / total_entries) * 100
        return f"<li>{answer}: {count} ({round(percentage, 2)}%)</li>"

    # Helper function to generate HTML for each question
    def format_question(question_data):
        question, answers = question_data
        answers_html = "".join(map(format_answer, answers.items()))
        return f"<li><strong>{question}:</strong><ul>{answers_html}</ul></li>"

    question_html = "".join(map(format_question, question_stats.items()))

    content = format_html(
        """
        <h2>Results / Результаты / Natijalar </h2>
        <p><strong>Total Entries / Общее количество участников / Umumiy qatnashganlar soni:</strong> {}</p>
        <h3>Question-wise Answer Results / Результаты ответов по вопросам / Savollar bo'yicha javoblar natijalari</h3>
        <ul>{}</ul>
        """,
        total_entries,
        format_html(question_html),
    )

    return content


