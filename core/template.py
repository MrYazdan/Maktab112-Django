def link_creator(request, path):
    return "#" if request.path == path else path


def menu_context_processor(request):
    print(request.path)

    return {
        "menu": [
            dict(title="Home", link=link_creator(request, "/")),
            dict(title="About", link=link_creator(request, "/about-us/")),
            dict(title="Products", link=link_creator(request, "/products/")),
            dict(title="Books", link=link_creator(request, "/books/")),
        ]
    }
