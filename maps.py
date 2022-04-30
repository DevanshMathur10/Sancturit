import gmplot
coords=(26.936549, 75.789425,18)

def map():
    
    gmap=gmplot.GoogleMapPlotter(26.936549, 75.789425,18)
    gmap.marker(26.936549, 75.789425, color='cornflowerblue')

    hospitallats, hospitallngs = zip(*[
    (26.936622, 75.789390),
    (26.936541, 75.789593),
    (26.936487, 75.789489),
    (26.936403, 75.789445)
    ])
    gmap.scatter(hospitallats, hospitallngs, color='#ff0000', size=80)

    policelats,policelngs=zip(*[
    (26.936527, 75.789392),
    (26.9366312,75.7892678),
    (26.936650, 75.789501),
    (26.936395, 75.789473),
    (26.936439, 75.789310)
    ])
    gmap.scatter(policelats,policelngs, color='green', size=80)

    path_two_lats, path_two_longs = zip(
    *[
        (26.936549, 75.789425), (26.936403, 75.789445),
        (26.936395, 75.789473), (26.936541, 75.789593),
    ]
    )  
    gmap.plot(path_two_lats, path_two_longs, "#c1f7b2", edge_width=3.0)
    gmap.draw("C:/Users/DELL/Documents/VS/HACKATHONS/SANCTURIT/map.html")

