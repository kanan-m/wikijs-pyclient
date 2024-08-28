from wikijs import WikiJS
import json

old_path= 'old-path-prefix'
new_path = 'new-path-prefix'       # prefix for the new destination
destination_locale = 'en'          # static variable

wiki = WikiJS(
    url="https://wiki.companydomain.xyz",
    token="ey....................Hw"
)

result = WikiJS.list_pages(wiki)
result = result.json()

for item in result:
    if (item['path'].startswith(old_path)):      # might be changed based on need
        id = item['id']
        destination_path = new_path + item['path']
        print(id, destination_path)
        WikiJS.move_page(wiki, id=id, destinationPath=destination_path, destinationLocale=destination_locale)

# In case if the wiki has self-signed/Internal CA issues certificate you can access to the Windows Certificate Store to validate the certificate using the below package
# pip install pip-system-certs
