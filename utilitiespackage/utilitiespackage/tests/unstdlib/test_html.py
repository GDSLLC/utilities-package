from utilitiespackage.unstdlib.html import tag_builder

def test_tag_builder():
    ul, li = tag_builder(['ul', 'li'])
    assert ul(li(ch) for ch in 'abc') == u'<ul><li>a</li><li>b</li><li>c</li></ul>'
