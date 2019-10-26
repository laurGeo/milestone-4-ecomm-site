{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":46,"position":46,"stack":[[{"start":{"row":5,"column":36},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":10,"column":63},"action":"insert","lines":["paginator = Paginator(contact_list, 25) # Show 25 contacts per page","","    page = request.GET.get('page')","    contacts = paginator.get_page(page)","    return render(request, 'list.html', {'contacts': contacts})"],"id":40}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":38},"action":"remove","lines":["contact_list"],"id":41},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["p"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["r"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["o"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["d"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["u"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["c"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["t"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["5"],"id":42},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["2"]}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["3"],"id":43}],[{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"remove","lines":["5"],"id":44},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["2"]}],[{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["3"],"id":45}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":63},"action":"remove","lines":["    return render(request, 'list.html', {'contacts': contacts})"],"id":46},{"start":{"row":9,"column":39},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":12},"action":"remove","lines":["contacts"],"id":47},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["p"]},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["r"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["o"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["d"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["u"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["c"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["t"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":35},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":48}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":43},"action":"insert","lines":["from django.core.paginator import Paginator"],"id":49}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":34},"action":"remove","lines":["request.GET.get('page')"],"id":50},{"start":{"row":9,"column":11},"end":{"row":9,"column":31},"action":"insert","lines":["paginator.page(page)"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["'"],"id":51}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["'"],"id":52}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["'"],"id":53}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["'"],"id":54}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":31},"action":"remove","lines":["page = paginator.page(page)"],"id":55},{"start":{"row":9,"column":4},"end":{"row":14,"column":51},"action":"insert","lines":["try:","        users = paginator.page(page)","    except PageNotAnInteger:","        users = paginator.page(1)","    except EmptyPage:","        users = paginator.page(paginator.num_pages)"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":13},"action":"remove","lines":["users"],"id":56},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["p"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["r"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["o"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["d"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["s"],"id":57}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"remove","lines":["s"],"id":58}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["s"],"id":59}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":13},"action":"remove","lines":["prods"],"id":60},{"start":{"row":10,"column":8},"end":{"row":10,"column":16},"action":"insert","lines":["products"]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":13},"action":"remove","lines":["users"],"id":61},{"start":{"row":12,"column":8},"end":{"row":12,"column":16},"action":"insert","lines":["products"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":13},"action":"remove","lines":["users"],"id":62},{"start":{"row":14,"column":8},"end":{"row":14,"column":16},"action":"insert","lines":["products"]}],[{"start":{"row":15,"column":1},"end":{"row":15,"column":39},"action":"remove","lines":["   products = paginator.get_page(page)"],"id":63}],[{"start":{"row":2,"column":27},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":64}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":72},"action":"insert","lines":["from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger"],"id":65}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["'"],"id":66}],[{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":["'"],"id":67},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"remove","lines":["s"],"id":68}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["3"],"id":69}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["2"],"id":70}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["2"],"id":71}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["1"],"id":72}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["1"],"id":73}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["3"],"id":74}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["3"],"id":75}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["1"],"id":76}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"remove","lines":["'"],"id":77}],[{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"remove","lines":["'"],"id":78}],[{"start":{"row":11,"column":38},"end":{"row":11,"column":40},"action":"insert","lines":["  "],"id":79}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":80}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":35},"action":"insert","lines":[" page = request.GET.get('page')"],"id":81}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"remove","lines":[" "],"id":82}],[{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"remove","lines":[" "],"id":83},{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"remove","lines":[" "]}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["1"],"id":84}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["3"],"id":85}]]},"ace":{"folds":[],"scrolltop":29,"scrollleft":0,"selection":{"start":{"row":8,"column":37},"end":{"row":8,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1572132669170,"hash":"64b7e4fa69f9dc53815031814905879ce8eccafa"}