def structure(new_phone):
    site = {
        'html': {
            'head': {
                'title': f'Куплю/продам {new_phone} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {new_phone}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }
    return site


new_site = {}


def site_generator(num_sites):
    if num_sites == 0:

        return 0
    else:
        product = input('Insert the product: ')
        site_return = structure(product)
        new_site[product] = site_return
        print(f'New site for {product} :')
        print(new_site)
        return site_generator(num_sites - 1)


n = int(input('How many sites?: '))
print(site_generator(n))
