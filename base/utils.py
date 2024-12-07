from django.utils.html import format_html

from exceptions.exception import CustomApiException
from exceptions.error_messages import ErrorCodes


def format_poll_results(data):
    formatted_result = ""

    for poll in data:
        question = poll['question']
        total_responses = poll['total_responses']
        formatted_result += f"<p><b>{question} (response {total_responses})</b></p>\n"

        formatted_result += '<ul style="list-style-type: circle;">\n'
        for answer in poll['answers']:
            answer_text = answer['text']
            percentage = answer['persentage']
            count = answer['count']
            formatted_result += f"<li>{answer_text}, {percentage}% ({count} kishi)</li>\n"
        formatted_result += "</ul>\n"

    return format_html(formatted_result)



def validate_and_extract_sheet_id(sheet_url):
    sheet_id = sheet_url.split("/d/")[1].split("/")[0]
    if sheet_id:
        return sheet_id
    raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)



def is_valid_sheet_data(sheet_data):
    """
    Validates if the sheet data has the minimum required rows and columns.
    """
    return sheet_data and len(sheet_data) >= 2 and all(len(row) > 1 for row in sheet_data)



def process_poll_data(sheet_data):
    """
    Processes Google Sheet data into formatted poll results.
    """
    header = sheet_data[0]
    responses = sheet_data[1:]

    formatted_data = []
    for idx, question in enumerate(header[1:]):
        answers = {}
        for response in responses:
            answer = response[idx + 1]
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1

        total_responses = sum(answers.values())
        formatted_answers = [
            {
                "text": answer,
                "count": count,
                "persentage": round((count / total_responses) * 100, 2),
            }
            for answer, count in answers.items()
        ]
        formatted_data.append({
            "question": question,
            "answers": formatted_answers,
            "total_responses": total_responses,
        })

    return format_poll_results(formatted_data)