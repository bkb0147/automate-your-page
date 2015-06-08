def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


EXAMPLE_LIST_OF_CONCEPTS = [ ['HTML', 'HTML stands for Hypertext Markup Language.'],
                              ['Tags And Elements', '>HTML documents are made of HTML elements. When writing HTML, we tell browsers the type of each element by using HTML tags.'],
                        ['Why Computers Are Stupid', 'They interpret instructions literally. Small mistakes, like typos or incorrct tags or element construction by a programmer can cause huge problems in a program.'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
