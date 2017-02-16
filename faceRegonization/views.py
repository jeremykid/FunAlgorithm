def my_view(request):
    if request.method == 'POST':
        import set_gpio
        #Do your stuff ,calling whatever you want from set_gpio.py

    return "1"#Something, normally a HTTPResponse, using django""