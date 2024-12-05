from django.utils.html import format_html
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

