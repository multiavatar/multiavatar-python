import sys
sys.path.append("../multiavatar")
from multiavatar import multiavatar

html = '<html><head></head><body>'

avatar = multiavatar('Starcrasher', None, None)
html += avatar
html += '<br>'

avatar = multiavatar('Pandalion', True, None)
html += avatar
html += '<br>'

# Generate a specific version
ver = { "part": "11", "theme": "C" }
avatar = multiavatar('Starcrasher', None, ver)
html += avatar
html += '<br>'

# Generate a specific version
avatar = multiavatar('Starcrasher', None, { "part": "08", "theme": "C" })
html += avatar
html += '<br>'

# Test transparency
avatar = multiavatar('Starcrasher', None, { "part": "15", "theme": "B" })
html += avatar
html += '<br>'

# Test with integer
avatarId = 123456789
avatar = multiavatar(avatarId, None, None)
html += avatar
html += '<br>'


html += '</body></html>'

# print(html)

f = open("other.html", "w")
f.write(html)
f.close()