{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"insert","lines":[","],"id":2},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"insert","lines":["i"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"insert","lines":["d"]}],[{"start":{"row":40,"column":41},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":42,"column":0},"action":"insert","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":42,"column":0},"end":{"row":52,"column":41},"action":"insert","lines":["def adjust_cart(request,id):","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","    ","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","        ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"],"id":5}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":15},"action":"remove","lines":["adjust_cart"],"id":6},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["d"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["e"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["l"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["e"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["t"]},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["e"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["_"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["f"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["r"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["m"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":["o"],"id":7},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["m"]}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["o"],"id":8},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["m"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["_"]},{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["c"]},{"start":{"row":42,"column":17},"end":{"row":42,"column":18},"action":"insert","lines":["a"]},{"start":{"row":42,"column":18},"end":{"row":42,"column":19},"action":"insert","lines":["r"]},{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":45,"column":0},"end":{"row":48,"column":9},"action":"remove","lines":["    ","    if quantity > 0:","        cart[id] = quantity","    else:"],"id":9}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["    "],"id":10}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":48},"action":"remove","lines":["    quantity = int(request.POST.get('quantity'))"],"id":11},{"start":{"row":42,"column":33},"end":{"row":43,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":43,"column":42},"end":{"row":44,"column":0},"action":"remove","lines":["",""],"id":12}]]},"ace":{"folds":[],"scrolltop":437,"scrollleft":0,"selection":{"start":{"row":43,"column":42},"end":{"row":43,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1572528869363,"hash":"70371e580b5858f4543acb66f222927df4ea5b9d"}