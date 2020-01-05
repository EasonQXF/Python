import pandas as pd
from flask import Flask,render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Pie,Scatter
from pyecharts.charts import Map, Timeline



app = Flask(__name__)


@app.route('/')
def bar2() -> 'html':
    df = pd.read_csv('nengyuanshengchanniandu.csv')
    bar = (
    Bar()
    .add_xaxis(["2018", "2017", "2016", "2015", "2014"])
    .add_yaxis("能源生产总量(万吨标准煤)", [377000, 358500, 346037.31, 361476, 361866])
    .add_yaxis("能源消费总量(万吨标准煤)", [464000, 448529.14, 435819, 429905, 425806])
    .add_yaxis("原煤生产总量(万吨标准煤)", [261261, 249516, 241534, 260985.67, 266333.38])
    .add_yaxis("煤炭消费总量(万吨标准煤)", [273760, 270911.52, 270207.78, 273849.49, 279328.74])
    .add_yaxis("原油生产总量(万吨标准煤)", [27144, 27246, 28375.06, 30725.46, 30396.74])
    .add_yaxis("石油消费总量(万吨标准煤)", [87696, 84323.45, 80626.52, 78672.62, 74090.24])
    .add_yaxis("天然气生产总量(万吨标准煤)", [20735, 19359, 17993.94, 17350.85, 17007.70])
    .add_yaxis("天然气消费总量(万吨标准煤)", [36192, 31397.03, 27020.78, 25364.40, 24270.94])
    .set_global_opts(title_opts=opts.TitleOpts(title="能源", subtitle="生产-消费对比"))
)
    bar.render("./templates/the_nengyuan.html")
    with open("./templates/the_nengyuan.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('1.html',
                           the_nengyuan=plot_all,
                          )


@app.route('/1',methods=['GET'])
def bar() -> 'html':
    df = pd.read_csv('GDP.csv')
    a = (
        Bar()
        .add_xaxis(["2017", "2016", "2015", "2014"])
        .add_yaxis("国民总收入(亿元)", [820099, 737074, 683390, 642097.6])
        .add_yaxis("治理废气项目完成投资(万元)", [1008, 846, 658, 594])
        .set_global_opts(title_opts=opts.TitleOpts(title="经济关系", subtitle="收入与投资"))
    )
    a.render("./templates/the_gdp.html")
    with open("./templates/the_gdp.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('6.html',
                           the_gdp=plot_all,
                           )

@app.route('/2',methods=['GET'])
def bar1() -> 'html':
    df = pd.read_csv('quanguofeiqi.csv')
    line = (
        Line()
        .add_xaxis(["2017", "2016", "2015", "2014"])
        .add_yaxis("二氧化硫排放量(吨)", [8753975.72, 11028643.04, 18591000, 19744000])
        .add_yaxis("氮氧化物排放量(吨)", [12588323.62, 13943109, 18510241.91, 20780015.34])
        .set_global_opts(title_opts=opts.TitleOpts(title="中国废气主要污染物排放", subtitle="SO2/氮氧化合物"))
)
    line.render("./templates/the_so2.html")
    with open("./templates/the_so2.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('4.html',
                           the_so2=plot_all,
                           )

@app.route('/3',methods=['GET'])
def timeline_map1() -> Timeline:
    df = pd.read_csv('nengyuanxiaohao.csv')
    tl = Timeline()
    for i in range(2017, 2014):
        map0 = (
            Map()
            .add("碳煤石油天然气消耗量（万吨标准煤）", zip(list(df.地区), list(df["{}".format(i)])), "china",is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}国各省碳煤石油天然气消耗量".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(min_=30,max_=6000,is_piecewise=True),
            )
        )
        tl.add(map0, "{}".format(i))
        tl.render("./templates/3.html")
    with open("./templates/3.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
    return render_template('5.html',
                           the_map=plot_all,
                           )

@app.route('/4',methods=['GET'])
def timeline_map2() -> Timeline:
    df = pd.read_csv('fenshenggdp.csv')
    tl = Timeline()
    for i in range(2017, 2014):
        map0 = (
            Map()
            .add("各省GDP（亿元）", zip(list(df.地区), list(df["{}".format(i)])), "china", is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}全国各省GDP".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(min_=900, max_=90000, is_piecewise=True),

            )
        )
        tl.add(map0, "{}".format(i))
        tl.render("./templates/2.html")
    with open("./templates/2.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
    return render_template('the_fenshenggdp.html',
                           the_fenshenggdp=plot_all,
                           )



if __name__ == '__main__':
  app.run(debug=True)