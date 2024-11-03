import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    cleaned_text = re.sub(r'<[^>]*>', '', html)


    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]


    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write("\n".join(cleaned_lines))

    print(f"Файл очищено від HTML-тегів і збережено в '{result_file}'.")



delete_html_tags( 'draft.html', 'cleaned.txt')