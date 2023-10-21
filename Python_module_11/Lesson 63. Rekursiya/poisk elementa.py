site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

n = input('Insert what you are looking for: ')


def search(zapros, site):
    if zapros in site:
        return site[zapros]
    else:
        z = []
        for i in site:
            if isinstance(site[i], dict):
                z = search(zapros, site[i])
        if z == []:
            return 'Element not found'
        else:
            return z


print(search(n, site))
